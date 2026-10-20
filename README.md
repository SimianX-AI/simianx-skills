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
  Give any AI agent a full research desk. With SimianX AI your agent can convene an 8-agent research committee on any US stock or crypto pair and question it afterwards, get a live four-agent read with entry, stop and target, and keep a scored news stream open on your symbols. One skill and a remote MCP server for Claude Code, Codex, Cursor, Muse, Grok Bot, dots and every other agent.
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

## Why give your agent SimianX

Ask an agent on its own *"Should I buy NVDA for a swing trade?"* and it searches the web, summarises headlines that may be days old and gives one model's opinion. It has no live chart, nobody arguing the other side, and it stops when the chat ends.

With SimianX the same agent:

| | On its own | With SimianX AI |
|---|---|---|
| Who works on it | One model | An 8-agent committee: four analysts, a bull and a bear researcher, a research manager, a risk manager |
| What it reads | Web search results | Live candles, filings, insider trades, the news flow; on-chain and derivatives data for a coin |
| What you get | An opinion | A verdict with entry, stop and target, and a PDF report |
| Afterwards | Starts over | Puts follow-up questions to the same committee, or sets an autopilot to keep watching |

## What you can ask

Once the skill is in, ask in your own words:

- *"Convene the SimianX committee on NVDA for a swing trade."* Four analysts report, the bull and the bear argue it out, and the risk manager hands back the verdict, the plan and a PDF.
- *"Ask the bear researcher what would prove the bull case wrong."* Follow-ups go to the same run, so the answer builds on everything the committee already read.
- *"Run the committee on SOL with a short horizon."* For a coin the analysts also read on-chain flows and the derivatives market.
- *"How does BTC look on the 15-minute chart right now?"* Four live agents answer, and the Decision agent says buy, sell or stay out with entry, stop and target.
- *"Tell me when high-value news hits TSLA or ETH."* A scored news stream on your symbols, live as each story is scored.
- *"Watch AAPL on the 1-hour chart and manage a paper position."* An autopilot reruns the agents on every candle close and logs every signal.
- *"Which biopharma PDUFA dates fall in the next 30 days?"* Sector Watch, from primary sources.
- *"What moved sharply in crypto in the last hour?"* Market Pulse: sudden moves, new highs and lows, volume spikes and gaps.

Free accounts can try the committee on popular symbols such as NVDA, AAPL, TSLA, BTC and ETH.

## What SimianX covers

Two things do most of the work.

- **Live multi-agent analysis.** Name a stock or a crypto pair and a timeframe, and four agents read it at the same time. Indicator reads the chart. Intelligence reads the news flow. Fundamental reads filings and insider trades, or on-chain and derivatives data for a coin. Decision weighs the three and proposes a trade with entry, stop and target. → [Live analysis](https://www.simianx.ai/l)
- **A scored news stream.** Every article comes in tagged with the symbols it moves, a value score and a bullish, bearish or neutral read. It is the feed behind Market Pulse, where it runs next to sudden price moves, new highs and lows and gaps. Your agent can page through it or keep a stream open on its symbols. → [Market Pulse](https://www.simianx.ai/pulse)

Also there when you need it:

- **Deep research.** Eight agents debate a stock or a coin and come back with a verdict, a trade plan and a PDF. Your agent can ask follow-up questions. → [Deep analysis](https://www.simianx.ai/c)
- **Sector Watch.** Catalyst calendars and events taken from primary sources, starting with biopharma. → [Sector Watch](https://www.simianx.ai/sectors)
- **Autopilots.** The same four live agents on a schedule for one symbol, with a paper position and an event log your agent can follow. → [Autopilots](https://www.simianx.ai/autopilots)
- **Your choice of model.** Pick the model behind each agent, and see how each one has traded before you do. → [Model leaderboard](https://www.simianx.ai/crypto-leaderboard)

Markets: 13,000+ US stocks and ETFs on `1m` to `1mo` candles, and 4,000+ crypto pairs, spot and perpetual, on `1m` to `1D`. → [Stock analysis](https://www.simianx.ai/c) · [Crypto analysis](https://www.simianx.ai/l)

## Install in one sentence

Paste this to your agent:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and sign me in.
```

It puts the skill where your agent looks for skills, then signs you in: you approve a link in your browser, or type the 6-digit code we email you. A new address gets an account on the spot. The agent ends up with an API key of its own in `SIMIANX_API_KEY` and never with your website login.

From a terminal instead:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

The command and the directory for each agent (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline and the rest) are in [INSTALL.md](INSTALL.md).

### Muse, Grok Bot, dots and other agents on their own computer

Agents that run on their own cloud computer read the same sentence. They connect over MCP or build a connector from the [OpenAPI document](https://service.simianx.ai/v1/openapi.json), sign you in, keep the key in their own credential store and save SimianX as a skill. The exact words for Muse, Grok Bot and dots are in [INSTALL.md](INSTALL.md#agents-with-their-own-computer-muse-grok-bot-dots).

### Or connect over MCP

AI agents that speak MCP can use SimianX as tools without installing the skill. Add the remote server once with your key:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

The same for Claude Desktop, Cursor, Codex, VS Code, Windsurf, Gemini CLI, Grok Bot and Muse is in [INSTALL.md](INSTALL.md#connect-over-mcp). Registry name: `io.github.SimianX-AI/simianx`.

## First calls

| What | Call | Reference |
|---|---|---|
| Live analysis, once | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| News on your symbols | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| News as it lands | `GET /v1/news/stream` (server-sent events, resumable) | [news](skills/simianx/references/news.md) |
| Market Pulse | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Deep research | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Sector Watch | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Autopilots | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL `https://service.simianx.ai/v1`, header `Authorization: Bearer $SIMIANX_API_KEY`. The same calls as shell scripts are in [examples/curl](examples/curl).

## Plans

Free, Starter, Plus and Pro, see [pricing](https://www.simianx.ai/pricing). Agent calls use your plan's points at the same rates as the website. The news stream is live on Plus and Pro; below Plus, news runs 30 minutes behind. Answers come in 16 languages.

You can use SimianX's API to connect its analysis and signals to your own trading system and place real orders through a broker or exchange you authorize. Positions recorded inside SimianX are simulated; your integration submits and manages real orders in your own account.

## Security

- The key stays in `SIMIANX_API_KEY`. The skill never writes it into a repository, a log or a prompt.
- An agent never gets a website session. Signing in from an agent only creates an API key for that agent, and we email you when it happens.
- Keys have scopes, daily and monthly budgets and an optional IP allowlist. Give each agent the smallest key that does its job.
- Revoke a key at **My Account → API keys** and it stops working within a second.

## Versions

The skill sends its version in the `X-SimianX-Skill` header. When a version is retired, the API answers `426` with the URL to re-read, and `GET /v1/skill` shows the current and minimum versions. Update with your agent's own command or paste the sentence above again. What changed is in the [changelog](CHANGELOG.md).

## Repository layout

```
skills/simianx/SKILL.md           the skill (Agent Skills format)
skills/simianx/references/        live · news · data · deep · sectors · autopilots · billing
INSTALL.md                        agent-readable install guide (also at simianx.ai/INSTALL.md)
scripts/install.{sh,py,ps1}       installer for every agent; check_version.py · check_readmes.py
examples/curl · examples/runner   the first calls in curl; an always-on runner for autopilots
.claude-plugin · .agents/plugins · .cursor-plugin · plugin.json · gemini-extension.json
                                  manifests so marketplaces and plugin commands find the skill
server.json                       MCP Registry entry for the remote MCP server (service.simianx.ai/v1/mcp)
README.<locale>.md                this page in the 16 languages SimianX speaks
```

## Feedback

- From an agent: `POST /v1/feedback`.
- From a person: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) for the skill, [simianx.ai/agents](https://www.simianx.ai/agents) for the product.

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request, and [SECURITY.md](SECURITY.md) to report a vulnerability.

## License

MIT for everything in this repository. Use of the SimianX API is governed by the [Terms of Service](https://www.simianx.ai/legal/terms). SimianX analyses are information, not investment advice.
