# Changelog

The version here, in `skills/simianx/SKILL.md` (`metadata.version`), in `examples/runner/runner.py` (`SKILL_VERSION`),
in every plugin manifest (see `RELEASING.md`) and in the git tag are always the same number; `scripts/check_version.py` refuses a release when they differ. The API
publishes the same number at `GET /v1/skill` and answers `426` to skills older than its minimum.

## 1.2.0 - 2026-10-15

- Sign-in from the agent: `POST /v1/auth/link` (the user approves a link in the browser) or `POST /v1/auth/code` →
  `POST /v1/auth/key` (a 6-digit code by email; a new address gets an account). Both end in an API key for that agent
  only, never a website session. Two-step accounts relay a TOTP or backup code. `references/auth.md`.
- Live multi-agent analysis and the scored news stream (the feed behind Market Pulse) now lead SKILL.md (description,
  Coverage, call map, minimal loop) and every README; autopilots come later as the same agents on a schedule. Shorter
  READMEs; the per-agent install table lives in `INSTALL.md`. `examples/curl` starts with a live run and news and has
  no quote step; JSON is piped with `printf` so the scripts work in macOS `sh`.
- Sector Watch: `GET /v1/sectors`, `/v1/sectors/{sector}` (summary, `stocks`, `stocks/{ticker}`, `calendar`, `events`,
  `events/{slug}`, `assets`, `assets/{slug}`) and follows (`GET`/`POST /v1/sectors/{sector}/follows`,
  `DELETE .../follows/{id}`, Starter and above; the first follow creates a subscription with an email channel).
  Events carry severity 1–4, type, direction and an AI summary; free, trial and Starter see them 30 minutes late.
  Only `biopharma` is live. Documented in `references/sectors.md`; new Calls row in SKILL.md.
- Install adapters for every agent: Agent Plugins `plugin.json` at the root, Codex `.agents/plugins/marketplace.json`,
  Cursor `.cursor-plugin/`, Gemini `gemini-extension.json` + `GEMINI.md`, Codex `agents/openai.yaml` inside the skill;
  Claude plugin manifests gain repository, keywords and category.
- `INSTALL.md`: agent-readable install page (per client directory, raw-file lines, native commands, verification,
  security), also served at https://www.simianx.ai/INSTALL.md.
- `scripts/install.py` (python3, cross-platform), `scripts/install.sh` (POSIX, python3 or plain copy) and
  `scripts/install.ps1`: `--agent <client|all|auto>`, `--scope user|project`, `--link`, `--source`, `--uninstall`,
  `--dry-run`, `--yes`; writes `.installed.json`, never overwrites a foreign folder without `--force`.
- READMEs in the 16 product languages; `scripts/check_readmes.py` keeps them in step and `scripts/check_version.py`
  now covers every manifest (optional `--web` / `--backend` checks against the sibling repositories).
- Stale root `SKILL.md` removed: `skills/simianx/SKILL.md` is the single source. `CONTRIBUTING.md`, `SECURITY.md`,
  issue and pull request templates.

## 1.1.0 - 2026-10-15

- Version check once per session (`GET /v1/skill`), `X-SimianX-Skill` on every request, re-read SKILL.md on HTTP 426.
- Autopilot actions: `POST /v1/autopilots/{id}/actions` (open, add, reduce, close, set_levels, place_order,
  replace_order, cancel_order, set_timeframe) at server prices; `POST /v1/autopilots/{id}/run` for one agent now.
- `PATCH /v1/autopilots/{id}` with `timeframe` or `ai_position_control: false` closes the paper book first, like the live page.
- New event type `autopilot.action`; feedback endpoint `POST /v1/feedback`.
- The runner sends the skill header, checks the published version at start and exits 4 when the API refuses its version.

## 1.0.0 - 2026-10-14

- First release: keys, pricing, quotes, autopilots with an execution-grade event log, deep analysis, one-shot live
  analysis, classified news (list, detail, translate, stream), crypto market data, Market Pulse, runner and curl examples.
