---
name: simianx
description: Use SimianX AI from an agent. Start and follow autopilots on stocks and coins (execution-grade event log with cursors and expiry), run 8-agent deep research with a verdict and plan, run the live agents once, read classified real-time news (symbols, value score, sentiment), crypto candles and indicators, Market Pulse events, Sector Watch catalyst calendars and first-hand sector events (biopharma: PDUFA dates, approvals, CRLs, advisory committees, trial readouts). Billed in points from the account's subscription; handles API keys, quotes, 402 and 429. Use when the user asks for a trading analysis, market research, a view on a ticker or coin, news on a symbol, upcoming catalysts in a sector, or wants to automate monitoring or follow positions.
license: MIT
compatibility: Needs network access to the SimianX API. Optional: python3 for the runner.
metadata:
  author: simianx
  version: "1.2.0"
  api_base: https://service.simianx.ai
  docs: https://www.simianx.ai/agents
  openapi: https://service.simianx.ai/v1/openapi.json
---

# SimianX for agents

Base URL: `https://service.simianx.ai` (every path below starts with `/v1`). Auth: `Authorization: Bearer $SIMIANX_API_KEY`,
plus `X-SimianX-Skill: 1.2.0` (this file's version) on every request.
Responses use `{"code": <http status>, "notify": "<human text>", "data": {...}}`. Every response carries `X-Request-Id`,
`X-SimianX-Skill-Version`, `X-SimianX-Api-Version`, `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`;
paid responses carry `X-Points-Charged` and `X-Points-Remaining`.

## Coverage

- **Markets**: US stocks and ETFs (13,000+ instruments, timeframes `1m 15m 1H 1D 1W 1mo`) and crypto (1,500+ coins,
  4,000+ pairs on OKX, Binance, Bybit and Coinbase; spot and USDT/USD perpetuals, a bare `BTC` means the perpetual;
  timeframes `1m 5m 15m 1H 4H 1D`).
- **Autopilots**: the four live agents on a schedule for one symbol, optionally managing a paper position (market,
  limit and stop entries, scaling, stop-loss / take-profit, timing gate). Every analysis, signal and position change
  is an event behind a cursor; `signal.fired` and `position.changed` carry an expiry. The same book takes manual actions.
- **Deep research**: 8 agents per run. Four analysts (stocks: fundamentals, market, news, timing; crypto: fundamentals,
  market, news, derivatives), a bull and a bear researcher, a research manager, a risk manager who issues the verdict
  and the plan. Horizons `short` / `swing` / `long`, follow-up questions, PDF report.
- **Live analysis**: the four live agents once: indicator (chart), intelligence (news flow), fundamental (financials
  and events, or on-chain and derivatives for a coin), decision (entry, stop, target).
- **News**: every article classified by symbols, value (`low` / `medium` / `high`) and sentiment; list, by id,
  translated into 16 languages, SSE stream.
- **Market Pulse**: price shocks on 1-, 5- and 15-minute windows, 24-hour / 30-day / 52-week highs and lows, day moves
  and gaps, crypto and stocks, severity 1–4.
- **Sector Watch**: primary-source catalysts per sector: calendar (PDUFA dates, advisory committees, trial readouts),
  events with severity 1–4 and direction, constituents, drug assets, follows. Live sector: biopharma (SEC filings,
  FDA and Federal Register releases, ClinicalTrials.gov, openFDA); 30-minute delay below Plus.
- **Models**: tiers `fast` / `standard` / `frontier`; paid plans set any of 50+ models from 7 providers per agent
  (`GET /v1/models`); the crypto leaderboard shows how each model has traded.
- **Plans and languages**: Free, Starter, Plus, Pro (monthly points, per-plan limits). Answers in 16 languages
  (`X-Language`). Paper positions only: SimianX never trades a real account.

## Setup

0. **Version check, once per session.** This file is version `1.2.0` (frontmatter `metadata.version`). Send
   `X-SimianX-Skill: 1.2.0` on every request. Before the first real call, `GET /v1/skill` (public): if `data.version`
   is newer than yours, or `data.minimum_version` is above yours, re-read https://www.simianx.ai/SKILL.md and follow
   the new file. Any response with HTTP 426 (`reason: skill_outdated`) means the same: re-read, then retry.
   `data.deprecations` lists endpoints with a sunset date; stop using them before that date. The authoritative
   contract is always https://service.simianx.ai/v1/openapi.json; this file may lag it.
1. Read `SIMIANX_API_KEY` from the environment. If it is missing, sign the user in from here; both ways end in a key
   for this agent, never in a website session, and never grant `billing:manage` (see `references/auth.md`):
   - **Browser link** (the user is at a computer): `POST /v1/auth/link {"framework": "<this agent>"}` → show
     `data.url`. The user opens it, signs in or signs up on the site and approves with one click; poll
     `GET /v1/auth/link/{link_id}?wait=30` until `status` is `approved` (the token comes once) or `denied` / `expired`.
   - **Email code** (no browser needed): ask for the user's email, `POST /v1/auth/code {"email", "framework"}`, ask
     the user for the 6-digit code from the email, then `POST /v1/auth/key {"email", "code", "framework", "key":
     {"name", "daily_points_budget"}}` → `data.token`. An address without an account becomes one. `mfa_required` →
     ask for the authenticator or backup code and resend with `{"ticket", "mfa": {"method", "code"}}`; a 403
     `too_many_keys` lists the plan's keys: offer to replace one (`key.replace_key_id`) with the same `ticket`.
   Offer both and follow the one the user picks. Store the token where this agent reads its environment (shell
   profile, a git-ignored `.env`, the agent's secret store); never print it in full, never write it into a repository
   or a log. The user can also create a key by hand at https://www.simianx.ai/#api. Never ask for a card number.
2. `GET /v1/me` → plan, points left, this key's budgets and the plan's limits. Keep `data.limits` in mind for pacing.
3. `GET /v1/pricing` → prices in points (public, no key needed). Data endpoints are flat per request; AI endpoints are
   metered on the models used, `data.typical` gives the usual cost per tier (`fast`, `standard`, `frontier`).

## Rules

- Before any AI call: `POST /v1/analysis/quote {"endpoint": "<key>", "tier": "fast", ...}` and compare with the key's
  `budget_left` and the account's points. Never exceed the budget the owner set on the key.
- Prefer `tier: "fast"` unless the user asks for stronger models. Free accounts always run the fast tier. To pick a
  model per agent, send `models: {"<agent>": "<id>"}` with an id from `GET /v1/models` (paid plans); an id that is not
  in the catalogue for that market is refused with 400 and the allowed list.
- A `402` means points or budget are short. `data.reason` is `insufficient_points`, `budget_exceeded` or `call_over_cap`;
  `data.actions` lists the ways out (`renew_now`, `change_plan`, `subscribe`, all web links). Show them to the user; never try
  to pay yourself, there is no top-up and no pay-per-call.
- A `429` means a limit (`data.limit`: requests_per_minute, requests_per_day, heavy_per_minute, points_per_minute,
  ai_concurrency, stream_connections). Wait `Retry-After` seconds and retry; do not tighten the loop.
- Ask the human before: starting an autopilot that manages a paper position, spending more than ~50 points in one call,
  or anything about subscription changes. Never put the key in a repository, a log or a message.
- Analyses are information, not investment advice. Say so when you relay a decision.

## Calls

See `references/auth.md`, `references/autopilots.md`, `references/deep.md`, `references/live.md`, `references/news.md`,
`references/data.md`, `references/sectors.md` and `references/billing.md` in this skill. Short map:

| Need | Call |
|---|---|
| Sign the user in (no key yet) | `POST /v1/auth/link` → `GET /v1/auth/link/{id}?wait=30` (browser approval) · `POST /v1/auth/code` → `POST /v1/auth/key` (email code) |
| Account, points, limits | `GET /v1/me` · `GET /v1/usage?days=7` |
| Price before paying | `POST /v1/analysis/quote` |
| Models you may set per agent | `GET /v1/models` (public): ids, points per million tokens, where each applies, typical points per live call |
| Start / list autopilots | `POST /v1/autopilots` · `GET /v1/autopilots` |
| Follow an autopilot | `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` (long-poll, free) or `&stream=1` (SSE) |
| Autopilot history | `GET /v1/autopilots/{id}/analyses` · `/positions` · `/logs` |
| Stop / restart / archive | `POST /v1/autopilots/{id}/stop` · `/start` · `DELETE /v1/autopilots/{id}` |
| Trade the paper book by hand | `POST /v1/autopilots/{id}/actions` `{"action": "open|add|reduce|close|set_levels|place_order|replace_order|cancel_order|set_timeframe", …}` (server prices) |
| Run one agent now | `POST /v1/autopilots/{id}/run {"agent": "decision"}` → result as `analysis.completed` in the log |
| Deep research | `POST /v1/analysis/deep` → `GET /v1/analysis/deep/{id}` · `/events?wait=30` · `POST .../ask` · `.../pdf` |
| Live agents once | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` |
| News | `GET /v1/news?symbols=BTC,NVDA&since=<iso>` · `GET /v1/news/{id}` · `GET /v1/news/stream` (SSE, Plus+) |
| Crypto data | `GET /v1/quotes?symbols=` · `GET /v1/market/{symbol}/candles` · `/indicators` |
| Market Pulse | `GET /v1/pulse/events` · `GET /v1/pulse/summary` |
| Sector Watch | `GET /v1/sectors` · `GET /v1/sectors/{sector}/calendar` · `/events?min_severity=3` · `/events/{slug}` · `/stocks` · `/assets` · `POST /v1/sectors/{sector}/follows` (see `references/sectors.md`) |
| Search before starting | `GET /v1/instruments/search?q=` (best match first; use `symbol`) · `GET /v1/market/status` |
| Tell us something | `POST /v1/feedback` (read, not answered) |

## Feedback

`POST /v1/feedback {"message": "...", "category": "bug|feature|pricing|docs|data|other", "endpoint": "<key>", "request_id": "<X-Request-Id>"}`
when something is wrong, missing or confusing. We read every message; we do not reply individually for now, so do not
wait for an answer. Keep it civil and factual (abusive text is refused and not stored); never include keys, personal
data or secrets. 20 messages a day per key; `GET /v1/feedback` lists what you already sent.

## Minimal loop (follow an autopilot)

```bash
# 1. quote, then start
curl -s $API/v1/analysis/quote -H "Authorization: Bearer $SIMIANX_API_KEY" -H 'Content-Type: application/json' \
  -d '{"endpoint":"autopilots.create","tier":"fast"}'
curl -s $API/v1/autopilots -H "Authorization: Bearer $SIMIANX_API_KEY" -H 'Content-Type: application/json' \
  -d '{"asset":"crypto","symbol":"BTC","timeframe":"15m","tier":"fast"}'
# → data.autopilot.id and data.cursor

# 2. long-poll; returns at once when an event lands, else after 30 s with an empty list
curl -s "$API/v1/autopilots/$ID/events?after=$CURSOR&wait=30&types=position.changed,signal.fired" \
  -H "Authorization: Bearer $SIMIANX_API_KEY"
# → data.events[] (each with id, type, ts, expires_at, data) and data.cursor to pass back
```

Act on `position.changed` only while `now < expires_at`. `autopilot.paused_budget` / `autopilot.stopped` end the loop.
For an unattended process use `examples/runner/runner.py` from the skills repository.
