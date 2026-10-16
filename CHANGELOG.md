# Changelog

The version here, in `skills/simianx/SKILL.md` (`metadata.version`), in `examples/runner/runner.py` (`SKILL_VERSION`),
in every plugin manifest (see `RELEASING.md`) and in the git tag is always the same number; `scripts/check_version.py` refuses a release when they differ. The API
publishes the same number at `GET /v1/skill` and answers `426` to skills older than its minimum.

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
