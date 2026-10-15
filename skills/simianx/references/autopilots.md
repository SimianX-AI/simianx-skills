# Autopilots

An autopilot runs the four live agents (indicator, intelligence, fundamental, decision) on one symbol on a schedule,
optionally managing a paper position. Everything it does lands in an event log you read with a cursor.

## Start

`POST /v1/autopilots` (scope `automation:manage`, metered: each analysis cycle costs the models it uses; `typical_points_per_cycle` in the answer)

```json
{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast",
 "agents": ["indicator", "intelligence", "fundamental", "decision"],
 "intervals": {"indicator": 900, "decision": 900},
 "ai_position_control": true, "timing_gate": false,
 "webhook": {"url": "https://example.com/hook", "secret": "…", "events": ["live_crypto_position_opened"]},
 "language": "en"}
```

- `asset`: `crypto` or `stock`; `symbol`: `BTC`, `BTC-USDT-SWAP`, `NVDA`.
- `timeframe`: crypto `1m 5m 15m 1H 4H 1D`; stock `1m 15m 1H 1D 1W 1mo`.
- `tier` picks a model per agent (`fast | standard | frontier`); `models` `{agent: model_id}` overrides per agent (paid plans).
- `intervals` are seconds per agent (≥ 60). Without them the account's saved defaults apply.
- `ai_position_control` (default true): the decision agent opens, moves and closes a paper position; `position.changed`
  events follow. `webhook` is optional (HMAC-signed `X-SimianX-Signature: sha256=…` over `"<ts>.<body>"` when `secret` is set).
- Answer: `data.autopilot` (id, session_id, status, models, intervals…), `data.cursor` (start reading events here), `data.events_url`.
- Limits: running autopilots per plan (Free 1, Starter 2, Plus 3, Pro 10) and `ai_concurrency`; 429 `autopilot_limit` / `ai_concurrency` when full.

## Read the event log

`GET /v1/autopilots/{id}/events` (free; does not count against points, only against requests)

| Param | Meaning |
|---|---|
| `after` | cursor = `id` of the last event you processed. Omit to get the newest 50 and a cursor. |
| `wait` | 0–30 s: hold the request until something arrives after `after` |
| `types` | comma list to filter |
| `limit` | ≤ 200 |
| `stream=1` | server-sent events instead (`id:` = cursor, `event:` = type; `event: reconnect` → reconnect with the last id) |

Event types: `autopilot.started`, `autopilot.stopped` (`data.reason`: requested | insufficient_points), `autopilot.paused_budget`,
`autopilot.config_updated`, `analysis.completed` (`data.agent`, `data.conclusion`, `data.proposal` for the decision agent, `data.points`),
`analysis.failed`, `signal.fired` (a long/short proposal: side, confidence, entry_price, stop_loss, take_profit; `expires_at` set),
`position.changed` (`data.operation`: open | add | reduce | close | close_and_reverse | update_sl | update_tp | update_both |
place_order | fill_order | cancel_order…, with side, quantity, entry_price, stop_loss, take_profit, pnl, capital; `expires_at` set).

Cursors are stable for 7 days (the stream holds the recent tail; older cursors are served from the table).

## History

- `GET /v1/autopilots/{id}/analyses?agent=decision&limit=20&before=<timestamp>&include=text`
- `GET /v1/autopilots/{id}/positions?status=open|closed&limit=20` (positions with their operations)
- `GET /v1/autopilots/{id}/logs`

## Control

- `GET /v1/autopilots` (`?status=running`, `?archived=1`), `GET /v1/autopilots/{id}`
- `PATCH /v1/autopilots/{id}` with any of `timeframe`, `tier` / `models`, `intervals`, `timing_gate`, `language`, `ai_position_control`
- `POST /v1/autopilots/{id}/stop`, `POST /v1/autopilots/{id}/start` (restart, same checks as create), `DELETE /v1/autopilots/{id}` (archive; must be stopped)

Stops from the web app also appear as `autopilot.stopped` in the log, so a runner always learns about them.
