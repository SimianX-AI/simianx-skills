# Live analysis session

A live session puts the four live agents (indicator, intelligence, fundamental, decision) on one symbol and one
timeframe and runs them **at every candle close, for as long as you stay connected**: the same engine as the live
analysis room on the website. Each agent's result and each decision reach you the moment they land, as updates with
a `say` sentence; a `next_run` update tells you when the next analysis is. When the user says "watch BTC", "live
analysis", "keep analysing", "盯着", this is what you start. No position is opened: the decision is analysis, and after
each one you ask whether to connect the user's exchange or broker to act on it.

An autopilot is the same engine running server side without you (`references/autopilots.md`); a quick read is one pass
(`references/quick.md`).

## Start

`POST /v1/live/sessions` (scope `analysis:run`, metered per analysis like the website)

```json
{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast",
 "agents": ["indicator", "intelligence", "fundamental", "decision"], "language": "en"}
```

```json
{"code": 201, "notify": "Session created. Connect ws_url now and relay every frame …",
 "data": {"session": {"id": "<uuid>", "status": "waiting", "asset": "crypto", "symbol": "BTC", "timeframe": "15m",
                      "agents": [...], "models": {...}, "created_at": "…"},
          "ws_url": "wss://service.simianx.ai/ws/live/?pair_id=<uuid>&session_id=<uuid>&timeframe=15m",
          "updates_url": "/v1/updates?wait=30", "cursor": 0,
          "next_step": "Connect ws_url with the bearer header and stay connected; relay each frame …"}}
```
<!-- verify: field names of the create answer -->

- `asset`, `symbol`, `timeframe`, `tier`, `models`, `agents`, `language`: as for a quick read.
- `status` is `waiting` until the socket connects, `running` while it is connected (or within the grace window),
  `ended` afterwards (`ended_reason`: `stopped`, `agent_left`, `error`).
- `GET /v1/live/sessions` lists the key's sessions (`?status=running`), `GET /v1/live/sessions/{id}` one of them,
  `DELETE /v1/live/sessions/{id}` stops it (also stops the analysis; the socket receives `session_end`).

## Connect

Open `ws_url` with the same key the session was created with:

```
Authorization: Bearer simx_live_…        (header; no Origin header is needed for a key)
X-SimianX-Skill: 1.0.6
```

Reconnect with `&cursor=<last id you handled>` to receive what you missed. Every frame is JSON:

```json
{"id": 912, "kind": "decision", "notify_user": true,
 "say": "Decision on BTC (15m): open long. Entry 61000–61200, stop 60200, target 63000, confidence 7/10. …",
 "ask": "Do you want me to connect your exchange and place or manage this order for you?",
 "data": {"action": "open", "side": "long", "entry_low": 61000, "entry_high": 61200, "stop": 60200, "target": 63000,
          "confidence": 7, "invalidation": "…", "timeframe": "15m", "expires_at": "…", "market": "crypto", "symbol": "BTC"},
 "next_run_at": "2026-10-23T01:15:00Z", "cursor": 912, "ts": "2026-10-23T01:00:04Z"}
```

| field | meaning |
|---|---|
| `id` / `cursor` | the update id; what you ack and what you reconnect from |
| `kind` | `session_start`, `fundamental_done`, `indicator_done`, `intelligence_done`, `decision`, `next_run`, `session_end`, `heartbeat`, `tick` |
| `notify_user` | `true`: tell the user. `heartbeat` and `tick` are `false`: ignore them |
| `say` | the sentence to relay, in the request language |
| `ask` | a question for the user; a `decision` always carries the exchange / broker question |
| `data` | the structured fields (`references/developers.md`) |
| `next_run_at` | when the next analysis runs: say it in the user's time zone |

Acknowledge what you relayed by sending a frame back: `{"ack": 912}`. Acked ids are never resent, on the socket or
through `/v1/updates`; the same rows also sit in `/v1/updates` until acked, so a cut never loses a result.
<!-- verify: ack frame shape and reconnect query parameter -->

Order per candle: the three analysts (whichever finishes first is sent first), then `decision`, then `next_run`.
Relay each as it comes; on the decision, give the full plan and put the `ask` to the user.

## If you leave

The session needs a connection: that is what "live" means here. When the socket drops, the server keeps the session
for a **grace window of 2 minutes**: reconnect with the cursor and nothing is lost (frames that fell in the gap are
replayed). After 2 minutes without a connection the session ends with `session_end` (`data.reason: agent_left`),
and its `say` tells the user that an autopilot keeps watching even when the agent is away; offer to start one.

Agents woken only when a background command exits (Grok Bot, dots, Muse) run the socket with a wrapper that exits on
every `notify_user: true` frame and reconnects at once with the cursor (well inside the 2 minutes); or they skip the
socket and poll `GET /v1/updates?ack=…&wait=30` (or every 10 s exactly) while a separate process keeps the socket
open for presence. `scripts/follow_run.py live <id>` is the HTTP fallback (`references/following.md`).

## What to say

- On start: "Live analysis on BTC (15m) is running; I will report each agent and each decision as they land."
- On each `*_done`: the `say` line.
- On `decision`: the full plan, "analysis, not investment advice", the next run time, then the `ask`. If the user
  declines the exchange / broker connection for this symbol, do not ask again this session.
- On `session_end`: the `say` line; if the reason is `agent_left`, offer an autopilot.
- Never: points, costs, balances.
