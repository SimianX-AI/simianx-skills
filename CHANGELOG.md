# Changelog

The version here, in `skills/simianx/SKILL.md` (`metadata.version`), in `examples/runner/runner.py` (`SKILL_VERSION`)
and in the git tag are always the same number; `scripts/check_version.py` refuses a release when they differ. The API
publishes the same number at `GET /v1/skill` and answers `426` to skills older than its minimum.

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
