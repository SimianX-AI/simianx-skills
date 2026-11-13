# Changelog

The version here, in `skills/simianx/SKILL.md` (`metadata.version`), in `examples/runner/runner.py` (`SKILL_VERSION`),
in every plugin manifest (see `RELEASING.md`) and in the git tag is always the same number; `scripts/check_version.py` refuses a release when they differ. The API
publishes the same number at `GET /v1/skill` and answers `426` to skills older than its minimum.

## 1.0.9 - 2026-11-12

- Added: OAuth for MCP apps. An app connected to `https://service.simianx.ai/v1/mcp` that signs users in itself (Claude, ChatGPT, Cursor, VS Code, Codex, Gemini CLI) needs only the URL: a tool call without a key answers HTTP 401 with the protected-resource challenge, the user approves on the same page as the browser link, and the app holds an ordinary agent key (scoped, budgeted, revocable under API keys) with a refresh token that rotates it. Discovery at `/.well-known/oauth-protected-resource/v1/mcp` and `/.well-known/oauth-authorization-server`; Client ID Metadata Documents and dynamic registration; PKCE S256. Tools in `tools/list` carry `securitySchemes`.
- Changed: the browser sign-in link and an approved key that was not collected yet live 24 hours (were 30 minutes). Keep the `link_id` and poll the same link when the user comes back instead of creating a new one. The approval page stays readable after approval.
- Added: `GET /v1/instruments/search?symbols=A,B,C` resolves up to 20 names in one call. Search, candle and batch-list calls get more room per minute on every plan (Free 10, Starter 30, Plus 90, Pro 180).
- Changed: `403 insufficient_scope` carries `data.actions.edit_key`; a key request without `scopes` gets `data:read`, `analysis:run` and `automation:manage`, and the docs no longer recommend `data:read` alone.
- Changed: deep research on a fund or ETF answers `400 deep_not_covered` with the calls to use instead (quick read, live session) rather than `symbol_not_found`.
- Changed: the deprecated one-pass `POST /v1/analysis/live` stays until 2027-06-01 (was 2026-12-01). `get_autopilot_events` lists its event types.

## 1.0.8 - 2026-11-12

- Changed: the stock committee's fourth analyst is the positioning analyst (the next earnings date against the holding period and how the stock moved across past reports, analyst targets and estimate revisions, the options market's implied move, short interest, insiders and institutional holders). It replaces the timing analyst; runs started earlier keep their timing report. The crypto committee is unchanged (derivatives in the fourth seat). Step ids in events follow: `agent:positioning`.

## 1.0.7 - 2026-10-31

- Documented: `timing_gate` on crypto autopilots. While flat, the timing-gate model (`SX-1`, renamed on each retrain) scores each candle before the indicator and decision agents run; a skipped candle answers `analysis.completed` with `skipped: "timing_gate"`, `conclusion.gate` and 0.05 points (once per candle). Manual runs go through the gate; breaking-news decisions do not. `GET /v1/autopilots/{id}/analyses?agent=decision` lists the skipped candles as `agent: "gate"` rows.
- Changed: autopilot `intervals` accept 30 s (fundamental 30 min), as in the web app.

## 1.0.6 - 2026-10-23

- Added: `GET /v1/updates`, one feed of everything the user has not heard yet (finished steps, decisions, matched news), each with a server-written `say` sentence in the request language; ack with `?ack=<id>` on the next request, unacked items are sent again. Every keyed response carries `_pending` while updates wait and `_skill_update` when the reported skill is behind the current version; both prepend a line to `notify`.
- Changed: live analysis is a continuous session. `POST /v1/live/sessions`, then the WebSocket (bearer key, no Origin header needed) or `GET /v1/updates` every 10 seconds; every candle close reports fundamentals, technicals, news flow and the decision with the next run time, and asks whether to connect the user's exchange or broker. A 2-minute grace window covers reconnects. The one-pass run is now the quick read, `POST /v1/analysis/quick`; `POST /v1/analysis/live` is deprecated (sunset 2026-12-01).
- Changed: deep research relays every step: four analysts, two researchers, each debate round's start and end, the verdict, the PDF link. Events carry `say` and `notify_user`.
- Added: news watches (`POST /v1/news/watches`) match stories server side, offline too, cluster one event across sources, merge bursts and deliver through `/v1/updates`; webhooks (`POST /v1/webhooks`) deliver the same updates to a URL with an HMAC signature, retries and dead letters. `references/developers.md` for code clients (Idempotency-Key, WebSocket acks, the stable decision fields, Python and JavaScript clients).
- Changed: the browser sign-in link lives 30 minutes and an approved key waits 30 minutes; the agent polls at once instead of waiting to be told; `/v1/me` reports daily resets for daily plans.
- Changed: agents keep points in the background: no quotes, balances or confirmations unless the user asks or a 402 refuses a call. "Following a run" fixes the numbers (long-poll 30 s, fixed 10 s otherwise, deep 30 min, quick 10 min, sessions until stopped) and `scripts/follow_run.py` exits on every new update for agents woken only when a command exits.

## 1.0.5 - 2026-10-20

- Changed: real trading is stated plainly in SKILL.md, the autopilot reference and all 16 READMEs. Connect SimianX analysis and signals through the API to your own authorized trading system to place real orders through your broker or exchange; positions and position actions recorded inside SimianX stay simulated. (1.0.4 is skipped so every directory carries the same number.)

## 1.0.3 - 2026-10-20

- Changed: the skill leads with the 8-agent research committee for questions that need a full view (buy or not, the case, the risks) and with follow-up questions to the same committee; the four live agents stay the quick read on one timeframe. Descriptions in every manifest and in the MCP Registry entry say so.
- Added: INSTALL.md covers agents on their own computer (Muse, Grok Bot, dots): connect over MCP or a connector built from the OpenAPI document, sign in, keep the key in the agent's credential store, save the skill. The install sentence ends in "and sign me in".

## 1.0.2 - 2026-10-16

- Added: a remote MCP server at `https://service.simianx.ai/v1/mcp` (your SimianX API key as a bearer token) with the /v1 endpoints as tools, an A2A agent card, and the MCP Registry entry `io.github.SimianX-AI/simianx`. Setup for each client is in INSTALL.md.

## 1.0.1 - 2026-10-16

- Fixed: the SKILL.md frontmatter is valid YAML again (the `description` and `compatibility` values are quoted), so `npx skills add SimianX-AI/simianx-skills` and skill directories can read the skill.

## 1.0.0 - 2026-10-15

First release.

- **Live multi-agent analysis.** The four live agents (indicator, intelligence, fundamental, decision) on any US stock
  or crypto pair, once: `POST /v1/analysis/live`, then `GET /v1/analysis/live/{id}?wait=30`. Paid plans can pick the
  model behind each agent (`GET /v1/models`).
- **Scored news, the feed behind Market Pulse.** Every article with its symbols, a value and a sentiment: a list with
  filters, single articles, translated titles, and a resumable server-sent stream (`GET /v1/news/stream`).
- **Deep research** with the 8-agent committee: a verdict, a plan, follow-up questions and a PDF.
- **Market Pulse** events and summary, crypto candles, indicators and quotes, instrument search and market status.
- **Sector Watch**: catalyst calendar, events, constituents, drug assets and follows. Biopharma is live.
- **Autopilots**: the same live agents on a schedule with a paper position, an event log behind a cursor
  (`signal.fired` and `position.changed` carry an expiry), manual actions on the paper book and run-now for one agent.
- **Sign-in from the agent**: a link approved in the browser or a 6-digit code by email. Either way the agent gets an
  API key of its own, never a website session.
- **Keys and limits**: scopes, daily and monthly budgets, a per-call cap and an IP allowlist; `GET /v1/usage`,
  `POST /v1/feedback`, and the `X-SimianX-Skill` header with `GET /v1/skill` to keep the skill current.
- **Install for every agent**: one sentence to paste, `npx skills add` and `gh skill install`, plugin manifests for
  Claude Code, Codex, Cursor and Gemini CLI, install scripts for macOS, Linux and Windows, `INSTALL.md`, READMEs in
  16 languages, curl examples and a runner for autopilots.
