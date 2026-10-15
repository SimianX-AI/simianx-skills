# SimianX skills

Let your coding agent use SimianX: start and follow autopilots on stocks and coins through an execution-grade event
log, run 8-agent deep research, run the live agents once, read classified real-time news, crypto candles and
indicators, Market Pulse. Everything is billed in points from the SimianX plan the key belongs to.

- Web guide and prices: https://www.simianx.ai/agents
- OpenAPI: https://service.simianx.ai/v1/openapi.json
- The skill: [`skills/simianx/SKILL.md`](skills/simianx/SKILL.md) (also at https://www.simianx.ai/SKILL.md)

## Install

One line for any agent that reads a `SKILL.md` (Claude Code, Codex, Cursor, Gemini CLI, OpenClaw…):

```
Read https://www.simianx.ai/SKILL.md and set up SimianX for this project.
```

Or with the skills CLI / Claude Code plugin marketplace:

```
npx skills add https://www.simianx.ai
/plugin marketplace add astro-ge/simianx-skills
```

Then create an API key in **My Account → API keys** on https://www.simianx.ai and export it as `SIMIANX_API_KEY`.
Give the key a daily budget when the agent runs unattended.

## Setup (for agents)

1. Read `SIMIANX_API_KEY` from the environment; if missing, ask the user to create one (never ask for payment details).
2. `GET https://service.simianx.ai/v1/me` for plan, points and limits; `GET /v1/pricing` for prices.
3. Quote before every paid call (`POST /v1/analysis/quote`). Respect `402` (points) and `429` (limits) as the skill says.

## Runner

`examples/runner/runner.py` is a standard-library Python loop that long-polls an autopilot's event log and runs your
command or webhook on every position change, with cursor persistence, expiry checks, a per-trade cap and a daily loss
cap. It exits when the autopilot stops or pauses for budget.

```
export SIMIANX_API_KEY=simx_live_...
python3 examples/runner/runner.py --autopilot <id> --exec './trade.sh {operation} {side} {symbol} {quantity} {price}'
```

## Layout

```
skills/simianx/SKILL.md              the skill (setup, rules, call map)
skills/simianx/references/*.md       autopilots, deep, live, news, data, billing
examples/runner/runner.py            always-on follower
examples/curl/*.sh                   one call per file
.claude-plugin/                      Claude Code marketplace manifest
```

Skills are MIT licensed. Use of the API is subject to the SimianX terms of service. Analyses are information, not
investment advice.
