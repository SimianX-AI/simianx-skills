#!/usr/bin/env python3
"""Minimal SimianX client for code: start a live analysis session, read its frames over the WebSocket, ack each one,
hand decisions to your own order code, and fall back to the updates feed after a cut.

    pip install requests websockets
    export SIMIANX_API_KEY=simx_live_...
    python3 python_client.py BTC 15m

SimianX supplies the analysis; `place_order()` is where your broker or exchange integration goes. Positions recorded
inside SimianX are simulated."""
import asyncio
import json
import os
import sys
import uuid

import requests
import websockets

API = os.environ.get("SIMIANX_API", "https://service.simianx.ai")
KEY = os.environ["SIMIANX_API_KEY"]
H = {"Authorization": f"Bearer {KEY}", "X-SimianX-Skill": "1.0.6", "Content-Type": "application/json"}


def place_order(decision: dict) -> None:
    """Your execution code. `decision` is the stable `data` of a decision update."""
    print("DECISION", json.dumps(decision, indent=2))


def start_session(symbol: str, timeframe: str) -> dict:
    res = requests.post(f"{API}/v1/live/sessions", headers={**H, "Idempotency-Key": f"live-{symbol}-{timeframe}-{uuid.uuid4()}"},
                        json={"asset": "crypto", "symbol": symbol, "timeframe": timeframe}, timeout=30)
    res.raise_for_status()
    return res.json()["data"]


def catch_up(ack: int) -> int:
    """After a cut: everything not yet acked, from the feed."""
    res = requests.get(f"{API}/v1/updates", headers=H, params={"ack": ack, "wait": 0, "limit": 100}, timeout=30)
    res.raise_for_status()
    for u in res.json()["data"]["updates"]:
        if u["notify_user"]:
            print(u["kind"], u["say"])
            if u["kind"] == "decision":
                place_order(u["data"])
        ack = u["id"]
    return ack


SESSION_OVER = {4003, 4014}  # refused (no such session for this key) / stopped over the API: do not reconnect
BACKOFF = (2, 5, 10, 20, 30)  # seconds between reconnects; a deploy keeps the server away for a minute or two


def connect(url: str):
    headers = {"Authorization": H["Authorization"]}
    try:
        return websockets.connect(url, additional_headers=headers)  # websockets >= 14
    except TypeError:
        return websockets.connect(url, extra_headers=headers)  # websockets <= 13


async def follow(ws_url: str) -> None:
    ack, attempt = 0, 0
    while True:
        try:
            async with connect(ws_url) as ws:
                attempt = 0
                async for raw in ws:
                    f = json.loads(raw)
                    if not f.get("notify_user"):
                        continue  # heartbeat / tick / ack
                    print(f["kind"], f.get("say"), f.get("next_run_at") or "")
                    if f["kind"] == "decision":
                        place_order(f["data"])
                    ack = f["id"]
                    await ws.send(json.dumps({"ack": ack}))
                    if f["kind"] == "session_end":
                        return
        except websockets.ConnectionClosed as exc:
            if exc.rcvd is not None and exc.rcvd.code in SESSION_OVER:
                print("session over:", exc.rcvd.code, exc.rcvd.reason)  # start a new session if the user still wants one
                return
            print("connection closed, reconnecting:", exc)
        except OSError as exc:  # refused / reset: the server is restarting
            print("server unreachable, retrying:", exc)
        ack = catch_up(ack)  # anything finished while we were away comes from the feed
        await asyncio.sleep(BACKOFF[min(attempt, len(BACKOFF) - 1)])
        attempt += 1


if __name__ == "__main__":
    symbol, timeframe = (sys.argv[1:3] + ["BTC", "15m"])[:2]
    session = start_session(symbol, timeframe)
    print("session", session["session"]["id"], session["ws_url"])
    asyncio.run(follow(session["ws_url"]))
