<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI for AI agents</h1>

<p align="center">
  One skill that turns Claude Code, Codex, Cursor, Copilot, Gemini CLI and every other agent that reads skills into a client of the SimianX trading desk:
  autopilots with an execution-grade event log, 8-agent deep research, live analysis, classified news and sector catalysts.
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <b>English</b> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## What SimianX covers

Everything below is reachable through the skill and lives on [simianx.ai](https://www.simianx.ai); the links open the product page behind each capability.

**Markets**

- **US stocks and ETFs** — 13,000+ listed instruments, with earnings, filings, financial series and market-hours awareness. Timeframes `1m 15m 1H 1D 1W 1mo`. → [Stock analysis](https://www.simianx.ai/stocks)
- **Crypto** — 1,500+ coins and 4,000+ pairs across OKX, Binance, Bybit and Coinbase: spot and USDT/USD perpetual swaps (a bare symbol such as `BTC` resolves to the perpetual). Timeframes `1m 5m 15m 1H 4H 1D`. → [Crypto analysis](https://www.simianx.ai/l)

**What the agents do**

- **Autopilots** — the four live agents run on a schedule on one symbol and, if you let them, manage a paper position (market, limit and stop entries, scaling, stop-loss / take-profit, a timing gate). Every analysis, signal and position change lands in an event log you read with a cursor; `signal.fired` and `position.changed` carry an expiry. Your agent can also trade that book by hand. → [Autopilots](https://www.simianx.ai/autopilots)
- **Deep research** — a committee of 8 agents per run: four analysts (stocks: fundamentals, market, news, timing · crypto: fundamentals, market, news, derivatives), a bull and a bear researcher, a research manager who moderates the debate and a risk manager who issues the verdict and the plan. Horizons `short`, `swing`, `long`; follow-up questions; a PDF report. → [Deep analysis](https://www.simianx.ai/c)
- **Live analysis** — the four live agents, once: **indicator** (trend, momentum, structure on the chart), **intelligence** (news flow and narrative), **fundamental** (financials and events, or on-chain and derivatives for a coin) and **decision** (the trade proposal with entry, stop and target). → [Live analysis](https://www.simianx.ai/l)
- **Classified news** — every article scored for the symbols it moves, its value (`low` / `medium` / `high`) and its sentiment, as a list, by article, translated into 16 languages, or as a live stream. → [Stories](https://www.simianx.ai/stories)
- **Market Pulse** — price shocks on 1-minute, 5-minute and 15-minute windows, 24-hour / 30-day / 52-week highs and lows, day moves and gaps, for crypto and stocks, with a severity 1–4. → [Market Pulse](https://www.simianx.ai/pulse)
- **Sector Watch** — primary-source catalysts for a sector: a calendar (PDUFA dates, advisory committees, trial readouts), events with severity 1–4 and direction (approvals, complete response letters, topline results, designations, inspections, label updates…), constituents, drug assets and follows. Live today: **Biopharma · FDA approvals**, built from SEC filings, FDA and Federal Register releases, ClinicalTrials.gov and openFDA. → [Sector Watch](https://www.simianx.ai/sectors)
- **Models you choose** — three tiers (`fast`, `standard`, `frontier`) and 50+ models from 7 providers that a paid plan may set per agent; a public catalogue with prices in points. → [Points & rates](https://www.simianx.ai/points)
- **Leaderboard** — how every model has actually traded, so an agent can pick a decision model on evidence. → [Crypto AI model leaderboard](https://www.simianx.ai/crypto-leaderboard)

**Plans and languages** — Free, Starter, Plus and Pro plans with monthly points, per-plan rate limits and a 30-minute data delay below Plus ([pricing](https://www.simianx.ai/pricing)). The API answers in 16 languages (`X-Language`). SimianX does not trade real accounts: autopilot positions are paper positions you can mirror with your own runner.

## Install in one sentence

Paste this to your agent. It fetches the install guide, puts the skill where your agent reads skills, and asks you for a key:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Prefer a command? Both work for every agent that reads skills:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Then say **"Sign me in to SimianX"**. The agent hands you a link to approve in your browser, or mails you a 6-digit code; either way it receives a key of its own, scoped and budgeted, and stores it as `SIMIANX_API_KEY`. No account yet? The email code creates one. You can also create a key by hand at **My Account → API keys** on [simianx.ai](https://www.simianx.ai) and export it:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Install for your agent

| Agent | Native route | Where the skill lands |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` then `/plugin install simianx@simianx` | plugin, or `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` then `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (or `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (or `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Anything else | copy `skills/simianx/` into the directory your agent scans, or run `scripts/install.sh --agent auto` | see [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) lists the exact directory and shell lines for each client; `scripts/install.sh` (or `install.py`; on Windows: `install.ps1`) detects installed agents and copies or links the skill for you.

## What your agent can do

| Need | Call | Reference |
|---|---|---|
| Start and follow an autopilot on a stock or a coin | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Trade the autopilot's paper book by hand | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Run one agent now | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| 8-agent deep research with a verdict and a plan | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| The live agents, once | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Classified news (symbols, value, sentiment), as a list or a stream | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Sector catalysts: calendar, events, constituents, follows | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Crypto candles, indicators, quotes, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Models you may set per agent, prices, your account | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Every event in the autopilot log carries a cursor and, for anything an agent might act on (`signal.fired`, `position.changed`), an expiry stamp, so a runner never acts on stale information. Reading events is free; you pay for the analyses, in the points your plan already includes.

## A first session

1. `GET https://service.simianx.ai/v1/skill` — public; confirms the skill version your agent holds is still accepted.
2. `GET /v1/me` with `Authorization: Bearer $SIMIANX_API_KEY` — plan, points left, limits.
3. `POST /v1/analysis/quote` — what a call will cost, before paying.
4. `POST /v1/autopilots` with `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — then long-poll the event log from the cursor the answer returns.

The full loop, as `curl`, is in [examples/curl](examples/curl); a small always-on runner that executes your command or webhook on every position change is in [examples/runner](examples/runner).

## Points, not credits

- Everything is billed in **points** from the account's subscription. There are no top-ups and no pay-per-call.
- AI endpoints are metered on the models actually used; `GET /v1/pricing` publishes the usual cost per tier (`fast`, `standard`, `frontier`) and `GET /v1/models` the price of every model an agent may choose.
- Data endpoints are priced per request (a fraction of a point); the event log, `/v1/me`, `/v1/skill`, `/v1/pricing` and `/v1/models` cost nothing.
- `402` means points or a key budget ran out and names the way out (`renew_now`, `change_plan`, `subscribe`); `429` is a rate limit and carries `Retry-After`. Nothing else is ever a payment problem.

## Security

- The key lives in the `SIMIANX_API_KEY` environment variable. The skill never asks an agent to write it into a repository, a log or a prompt.
- An agent never gets a website session. Signing in from an agent (browser link or email code) only ever creates an API key for that agent, announced by email and listed in your security activity; the website, billing and security settings stay with you.
- Keys carry scopes (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), daily and monthly point budgets, a per-call cap and an optional IP allowlist. Give an agent the smallest key that does its job.
- Revoke any key at **My Account → API keys**; a revoked key is refused within a second. Every call is logged under your account with its cost.
- The skill reads only your own account: your autopilots, your runs, your keys. It never trades a real account; autopilot positions are paper positions.

## Versions and updates

The skill reports its version in the `X-SimianX-Skill` header. When the API no longer accepts a version it answers `426` with the URL to re-read, and `GET /v1/skill` always shows the current and the minimum version plus the [changelog](CHANGELOG.md). Update with your agent's own command (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) or re-run the one sentence above.

## Repository layout

```
skills/simianx/SKILL.md           the skill (Agent Skills format)
skills/simianx/references/        autopilots · deep · live · news · sectors · data · billing
INSTALL.md                        agent-readable install guide (also served at simianx.ai/INSTALL.md)
scripts/install.{sh,py,ps1}       installer for every agent; check_version.py · check_readmes.py
examples/curl · examples/runner   a first session in curl; the always-on runner
.claude-plugin · .agents/plugins · .cursor-plugin · plugin.json · gemini-extension.json
                                  manifests so marketplaces and plugin commands find the skill
README.<locale>.md                this page in the 16 languages SimianX speaks
```

## Feedback and support

- From an agent: `POST /v1/feedback` (read by the team; abusive text is refused and never stored).
- From a person: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) for the skill, [simianx.ai/agents](https://www.simianx.ai/agents) for the product.

See [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request and [SECURITY.md](SECURITY.md) to report a vulnerability.

## License

MIT for everything in this repository. Use of the SimianX API is governed by the [Terms of Service](https://www.simianx.ai/legal/terms). SimianX analyses are information, not investment advice; autopilot positions are paper positions.
