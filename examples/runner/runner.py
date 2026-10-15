#!/usr/bin/env python3
"""SimianX autopilot runner: long-polls an autopilot's event log and runs a command on every position change.

AI agents are not daemons; this is the small always-on loop between the SimianX event log and your broker,
exchange, notifier or a `claude -p` call. It keeps its cursor on disk, never acts on an expired event, enforces a
per-trade and a daily loss cap, and stops when the autopilot pauses for budget or is stopped.

    export SIMIANX_API_KEY=simx_live_...
    python3 runner.py --autopilot <id> --exec './trade.sh {operation} {side} {symbol} {quantity} {price}'
    python3 runner.py --autopilot <id> --webhook https://example.com/hook --max-trade-usd 500 --daily-loss-usd 200

Standard library only. Exit codes: 0 stopped cleanly, 2 autopilot stopped or paused for budget, 3 auth/plan error,
4 this runner's skill version is below what the API accepts (re-read SKILL.md and update SKILL_VERSION).
"""
import argparse
import json
import os
import shlex
import subprocess
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timezone

API = os.environ.get("SIMIANX_API", "https://service.simianx.ai")
SKILL_VERSION = "1.2.0"  # keep equal to skills/simianx/SKILL.md metadata.version
SKILL_URL = "https://www.simianx.ai/SKILL.md"
STOP_TYPES = {"autopilot.stopped", "autopilot.paused_budget"}


def call(path, key, method="GET", body=None, timeout=45):
    req = urllib.request.Request(API + path, method=method, headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": f"simianx-runner/{SKILL_VERSION}",
        "X-SimianX-Skill": SKILL_VERSION})
    data = json.dumps(body).encode() if body is not None else None
    try:
        with urllib.request.urlopen(req, data=data, timeout=timeout) as res:
            return res.status, json.loads(res.read() or b"{}"), dict(res.headers)
    except urllib.error.HTTPError as exc:
        try:
            payload = json.loads(exc.read() or b"{}")
        except Exception:  # noqa: BLE001
            payload = {}
        return exc.code, payload, dict(exc.headers or {})


def _vt(raw):
    try:
        parts = [int(p) for p in str(raw or "0").split(".")[:3]]
    except ValueError:
        return (0, 0, 0)
    return tuple(parts + [0] * (3 - len(parts)))


def parse_ts(value):
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


class State:
    def __init__(self, path):
        self.path = path
        self.data = {"cursor": None, "day": None, "loss": 0.0, "seen": []}
        if os.path.exists(path):
            with open(path) as f:
                self.data.update(json.load(f))

    def save(self):
        tmp = self.path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(self.data, f)
        os.replace(tmp, self.path)

    def daily_loss(self):
        today = date.today().isoformat()
        if self.data.get("day") != today:
            self.data.update(day=today, loss=0.0)
        return self.data["loss"]


def act(args, ev):
    d = ev.get("data", {})
    fields = {"operation": d.get("operation"), "side": d.get("side"), "symbol": d.get("symbol"), "market": d.get("market"),
              "quantity": d.get("quantity_change") or d.get("quantity"), "price": d.get("execution_price"),
              "stop_loss": d.get("stop_loss"), "take_profit": d.get("take_profit"), "position_id": d.get("position_id"),
              "event_id": ev.get("id"), "autopilot_id": ev.get("autopilot_id")}
    if args.webhook:
        req = urllib.request.Request(args.webhook, method="POST", data=json.dumps(ev).encode(),
                                     headers={"Content-Type": "application/json", "User-Agent": "simianx-runner/1.0"})
        with urllib.request.urlopen(req, timeout=20) as res:
            print(f"[runner] webhook {res.status} for {fields['operation']} {fields['symbol']}", flush=True)
    if args.exec:
        cmd = args.exec.format(**{k: ("" if v is None else v) for k, v in fields.items()})
        print(f"[runner] exec: {cmd}", flush=True)
        env = {**os.environ, "SIMIANX_EVENT": json.dumps(ev)}
        subprocess.run(shlex.split(cmd), check=False, env=env, timeout=args.exec_timeout)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--autopilot", required=True, help="autopilot id")
    p.add_argument("--exec", help="command template; fields: {operation} {side} {symbol} {quantity} {price} {stop_loss} {take_profit}")
    p.add_argument("--webhook", help="POST every acted event here")
    p.add_argument("--types", default="position.changed", help="comma list of event types to act on")
    p.add_argument("--max-trade-usd", type=float, default=0, help="skip operations whose value exceeds this (0 = no cap)")
    p.add_argument("--daily-loss-usd", type=float, default=0, help="stop acting for the day past this realised loss (0 = off)")
    p.add_argument("--state", default=None, help="cursor file (default .simianx-runner-<id>.json)")
    p.add_argument("--from-latest", action="store_true", help="ignore history, start from the newest event")
    p.add_argument("--exec-timeout", type=int, default=60)
    args = p.parse_args()

    key = os.environ.get("SIMIANX_API_KEY")
    if not key:
        print("SIMIANX_API_KEY is not set", file=sys.stderr)
        return 3
    state = State(args.state or f".simianx-runner-{args.autopilot}.json")
    types = [t.strip() for t in args.types.split(",") if t.strip()]

    status, skill, _ = call("/v1/skill", key)
    if status == 200:
        data = skill.get("data", {})
        if _vt(data.get("minimum_version")) > _vt(SKILL_VERSION):
            print(f"[runner] skill {SKILL_VERSION} is below the minimum {data.get('minimum_version')}: re-read {SKILL_URL}", file=sys.stderr)
            return 4
        if _vt(data.get("version")) > _vt(SKILL_VERSION):
            print(f"[runner] a newer skill ({data.get('version')}) is published: {SKILL_URL}", flush=True)
    wanted = ",".join(sorted(set(types) | STOP_TYPES))

    status, me, _ = call("/v1/me", key)
    if status != 200:
        print(f"[runner] cannot read account: {status} {me.get('notify')}", file=sys.stderr)
        return 3
    print(f"[runner] account {me['data']['account']['email']} plan {me['data']['account']['plan']} "
          f"points {me['data']['points']['remaining']}", flush=True)

    cursor = state.data.get("cursor")
    if not cursor or args.from_latest:
        status, body, _ = call(f"/v1/autopilots/{args.autopilot}/events?limit=1", key)
        if status != 200:
            print(f"[runner] cannot read events: {status} {body.get('notify')}", file=sys.stderr)
            return 3
        cursor = body["data"]["cursor"]
        state.data["cursor"] = cursor
        state.save()
    print(f"[runner] following {args.autopilot} from {cursor}", flush=True)

    backoff = 1
    while True:
        status, body, headers = call(f"/v1/autopilots/{args.autopilot}/events?after={cursor}&wait=30&types={wanted}&limit=100", key)
        if status == 429:
            wait = int(headers.get("Retry-After", "5") or 5)
            print(f"[runner] rate limited ({body.get('data', {}).get('limit')}), sleeping {wait}s", flush=True)
            time.sleep(wait)
            continue
        if status in (401, 403):
            print(f"[runner] {status}: {body.get('notify')}", file=sys.stderr)
            return 3
        if status == 426:
            print(f"[runner] skill outdated: {body.get('notify')}", file=sys.stderr)
            return 4
        if status != 200:
            print(f"[runner] {status}: {body.get('notify')}; retry in {backoff}s", flush=True)
            time.sleep(backoff)
            backoff = min(backoff * 2, 60)
            continue
        backoff = 1
        now = datetime.now(timezone.utc)
        for ev in body["data"]["events"]:
            cursor = ev["id"]
            etype = ev["type"]
            if etype in STOP_TYPES:
                print(f"[runner] {etype}: {ev.get('data')}", flush=True)
                state.data["cursor"] = cursor
                state.save()
                return 2
            if ev["id"] in state.data["seen"]:
                continue
            exp = parse_ts(ev.get("expires_at"))
            if exp and exp < now:
                print(f"[runner] skip expired {etype} {ev['id']}", flush=True)
                continue
            d = ev.get("data", {})
            value = abs(float(d.get("position_value") or 0))
            if args.max_trade_usd and value > args.max_trade_usd:
                print(f"[runner] skip {d.get('operation')}: value {value:.0f} over cap", flush=True)
                continue
            if args.daily_loss_usd and state.daily_loss() <= -abs(args.daily_loss_usd):
                print("[runner] daily loss cap reached; not acting until tomorrow", flush=True)
                continue
            try:
                act(args, ev)
            except Exception as exc:  # noqa: BLE001
                print(f"[runner] action failed for {ev['id']}: {exc}", file=sys.stderr)
            pnl = d.get("pnl_at_operation")
            if d.get("operation") in ("close", "close_and_reverse", "reduce") and pnl is not None:
                state.daily_loss()
                state.data["loss"] += float(pnl)
            state.data["seen"] = (state.data["seen"] + [ev["id"]])[-500:]
        state.data["cursor"] = cursor
        state.save()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(0)
