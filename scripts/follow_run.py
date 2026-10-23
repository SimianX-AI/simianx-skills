#!/usr/bin/env python3
"""Follow a SimianX run and exit on every new update, so an agent that is woken only when a command exits can relay
progress step by step.

    export SIMIANX_API_KEY=simx_live_...
    python3 follow_run.py updates [--ack ID] [--interval 10] [--max 60] [--until-idle]
    python3 follow_run.py deep <id> [--cursor C]
    python3 follow_run.py quick <id>
    python3 follow_run.py live <id> [--ack ID]
    python3 follow_run.py autopilot <id> [--ack ID]

Standard library only (Python 3.8+). One JSON line per update on stdout (id, kind, say, ask, next_run_at, data), then
a last line `ACK=<id>` to pass back next time. Exit codes:

    0  new updates were printed: tell the user each line, then run again with the printed ACK
    2  nothing new within --max seconds (default 60): run again at once; say "still running" if the user waits
    3  the run is over (deep: done/stopped/error/paused; quick: done/partial/failed; live: ended; autopilot: stopped
       or paused; updates: nothing pending and --until-idle)
    4  auth or plan error (401/403), or the skill is below the API's minimum (426): read the message
    5  bad arguments / network down for the whole wait

Long-polls the API (`wait=30`, twice by default). `--interval 10` polls every 10 seconds exactly instead, for
networks that cut long requests. Never give this command a shorter outer timeout than --max.
"""
import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

API = os.environ.get("SIMIANX_API", "https://service.simianx.ai").rstrip("/")
SKILL_VERSION = "1.0.6"
LONG_POLL = 30
DEEP_TERMINAL = {"done", "stopped", "failed", "error", "paused"}
QUICK_TERMINAL = {"done", "partial", "failed"}
FEED_FIELDS = ("id", "kind", "say", "ask", "next_run_at", "data")


def call(path, key, timeout=45):
    req = urllib.request.Request(API + path, headers={
        "Authorization": f"Bearer {key}", "Accept": "application/json", "X-SimianX-Skill": SKILL_VERSION,
        "User-Agent": f"simianx-follow/{SKILL_VERSION}"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as res:
            return res.status, json.loads(res.read() or b"{}")
    except urllib.error.HTTPError as exc:
        try:
            body = json.loads(exc.read() or b"{}")
        except Exception:  # noqa: BLE001
            body = {}
        return exc.code, body
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return 0, {"notify": str(exc)}


def fatal(status, body):
    if status in (401, 403, 426):
        print(f"[follow] {status}: {body.get('notify') or body.get('data', {}).get('reason')}", file=sys.stderr)
        return 4
    return None


def emit(rows):
    for r in rows:
        print(json.dumps({k: r.get(k) for k in FEED_FIELDS}, ensure_ascii=False, default=str), flush=True)


def finish(code, ack):
    print(f"ACK={ack if ack is not None else 0}", flush=True)
    return code


def wait_param(args):
    return 0 if args.interval else LONG_POLL


def sleep_step(args):
    if args.interval:
        time.sleep(args.interval)


# ---------------------------------------------------------------- the feed
def feed(args, key, source=None, source_id=None, terminal=None):
    """Loop on GET /v1/updates until something new (0), the wait runs out (2) or the run is over (3)."""
    ack = after = int(args.ack) if str(args.ack).isdigit() else 0
    deadline = time.monotonic() + args.max
    acked_once = False
    while True:
        q = {"wait": wait_param(args), "limit": 100, "notify": 1}
        if ack and not acked_once:
            q["ack"] = ack
        if after:
            q["after"] = after
        status, body = call(f"/v1/updates?{urllib.parse.urlencode(q)}", key)
        acked_once = True
        code = fatal(status, body)
        if code:
            return finish(code, ack)
        if status == 429:
            time.sleep(int(body.get("data", {}).get("retry_after") or 5))
        elif status == 200:
            data = body.get("data", {})
            rows = data.get("updates", [])
            if source:
                rows = [r for r in rows if (r.get("source") or {}).get("type") == source and (r.get("source") or {}).get("id") == source_id]
            if rows:
                emit(rows)
                last = rows[-1]["id"]
                over = terminal is not None and any(r.get("kind") in terminal for r in rows)
                return finish(3 if over else 0, last)
            if data.get("pending", 0) == 0 and args.until_idle and not source:
                return finish(3, ack)
            if source and terminal is not None and run_over(args, key, source, source_id):
                return finish(3, ack)
        elif status == 0:
            time.sleep(2)
        if time.monotonic() >= deadline:
            return finish(2, ack)
        sleep_step(args)


def run_over(args, key, source, source_id):
    """Is the run behind a feed filter finished? (The run's own state, in case its last update was already acked.)"""
    if source == "live":
        status, body = call(f"/v1/live/sessions/{source_id}", key, timeout=20)
        return status == 200 and (body.get("data", {}).get("session") or {}).get("status") == "ended"
    if source == "autopilot":
        status, body = call(f"/v1/autopilots/{source_id}", key, timeout=20)
        return status == 200 and (body.get("data", {}).get("autopilot") or {}).get("status") not in ("running", None)
    return False


# ---------------------------------------------------------------- one deep run, by its events
def deep(args, key):
    cursor = args.cursor or "0"
    deadline = time.monotonic() + args.max
    while True:
        q = urllib.parse.urlencode({"after": cursor, "wait": wait_param(args)})
        status, body = call(f"/v1/analysis/deep/{args.id}/events?{q}", key)
        code = fatal(status, body)
        if code:
            return finish(code, cursor)
        if status == 200:
            data = body.get("data", {})
            events = [e for e in data.get("events", []) if e.get("notify_user", e.get("type") in (
                "step_done", "step_start", "topic_done", "paused", "stopped", "error", "done", "pdf"))]
            cursor = data.get("cursor") or cursor
            over = (data.get("status") in DEEP_TERMINAL and not data.get("busy")) or any(
                e.get("type") in ("done", "stopped", "error", "paused") for e in data.get("events", []))
            if events:
                emit([{"id": e.get("id"), "kind": e.get("kind") or e.get("type"), "say": e.get("say"), "ask": e.get("ask"),
                       "next_run_at": None, "data": {k: e.get(k) for k in ("step", "agent", "stance", "verdict", "topic", "index", "result", "url", "reason")
                                                     if e.get(k) is not None}} for e in events])
                return finish(3 if over else 0, cursor)
            if over:
                return finish(3, cursor)
        elif status == 429:
            time.sleep(int(body.get("data", {}).get("retry_after") or 5))
        elif status == 0:
            time.sleep(2)
        if time.monotonic() >= deadline:
            return finish(2, cursor)
        sleep_step(args)


# ---------------------------------------------------------------- one quick read, by its run
def quick(args, key):
    relayed = args.cursor or ("" if str(args.ack).isdigit() else args.ack)  # the ACK= line of the last run, or --cursor
    seen = set((relayed or "").split(",")) - {""}
    deadline = time.monotonic() + args.max
    while True:
        q = urllib.parse.urlencode({"wait": wait_param(args)})
        status, body = call(f"/v1/analysis/quick/{args.id}?{q}", key)
        if status == 404:  # a run started on the old path
            status, body = call(f"/v1/analysis/live/{args.id}?{q}", key)
        code = fatal(status, body)
        if code:
            return finish(code, ",".join(sorted(seen)))
        if status == 200:
            run = body.get("data", {}).get("run", {})
            fresh = [(a, r) for a, r in (run.get("results") or {}).items() if r.get("status") in ("done", "skipped", "failed") and a not in seen]
            over = run.get("status") in QUICK_TERMINAL
            if fresh:
                rows = []
                for agent, r in fresh:
                    seen.add(agent)
                    detail = next((x for x in run.get("analyses", []) if x.get("agent") == agent), {})
                    rows.append({"id": f"{args.id}:{agent}", "kind": "decision" if agent == "decision" else f"{agent}_done",
                                 "say": r.get("say"), "ask": r.get("ask"), "next_run_at": body.get("data", {}).get("next_candle_close_at"),
                                 "data": {"agent": agent, "status": r.get("status"), "conclusion": detail.get("conclusion"),
                                          "symbol": run.get("symbol"), "timeframe": run.get("timeframe")}})
                emit(rows)
                return finish(3 if over else 0, ",".join(sorted(seen)))
            if over:
                return finish(3, ",".join(sorted(seen)))
        elif status == 429:
            time.sleep(int(body.get("data", {}).get("retry_after") or 5))
        elif status == 0:
            time.sleep(2)
        if time.monotonic() >= deadline:
            return finish(2, ",".join(sorted(seen)))
        sleep_step(args)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("what", choices=["updates", "deep", "quick", "live", "autopilot"])
    p.add_argument("id", nargs="?", help="run / session / autopilot id (not for `updates`)")
    p.add_argument("--ack", default="0", help="last update id you relayed (feed-based modes); quick: the agents already relayed")
    p.add_argument("--cursor", default=None, help="deep: event cursor; quick: agents already relayed")
    p.add_argument("--interval", type=int, default=0, help="poll every N seconds exactly instead of long-polling (10 for Grok Bot style tasks)")
    p.add_argument("--max", type=int, default=60, help="longest this invocation waits before exiting 2 (default 60)")
    p.add_argument("--until-idle", action="store_true", help="updates: exit 3 when the feed is empty and nothing is pending")
    args = p.parse_args()
    key = os.environ.get("SIMIANX_API_KEY")
    if not key:
        print("SIMIANX_API_KEY is not set", file=sys.stderr)
        return 5
    if args.what != "updates" and not args.id:
        print(f"{args.what} needs an id", file=sys.stderr)
        return 5
    if args.what == "updates":
        return feed(args, key)
    if args.what == "deep":
        return deep(args, key)
    if args.what == "quick":
        return quick(args, key)
    if args.what == "live":
        return feed(args, key, "live", args.id, {"session_end"})
    return feed(args, key, "autopilot", args.id, {"autopilot.stopped", "autopilot.paused"})


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(2)
