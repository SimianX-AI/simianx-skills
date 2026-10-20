# Contributing

Thanks for helping agents use SimianX well. This repository holds instructions, not product code: the skill
(`skills/simianx/`), its install adapters, scripts and examples.

- **Skill text** (`skills/simianx/SKILL.md`, `references/*.md`): keep the voice of the existing files, terse and
  command-first. SKILL.md stays under 500 lines and its `description` under 1024 characters; put detail in
  `references/`, one level deep. Prices and limits must match `GET /v1/pricing` and `GET /v1/me`; when the API
  changes, the backend change and this repository ship together. Say "points", never "credits"; name no data vendors.
- **Execution wording**: users can connect API analysis/signals to their own authorized trading system for real
  orders through their broker or exchange. Positions and position-action tools inside SimianX are simulated.
  Keep this distinction consistent with the frontend skill copies and backend discovery descriptions.
- **READMEs**: `README.md` is English and canonical. Any change to it is applied to all 15 `README.<locale>.md` in the
  same pull request; `python3 scripts/check_readmes.py` must pass (same logo block, navigation line, URLs and code
  blocks). The install sentence stays in English in every language, agents read it.
- **Versions**: do not bump versions in a feature pull request; releases are cut separately (`RELEASING.md`).
- **Scripts**: `scripts/install.py` is standard library only and must keep working on macOS, Linux and Windows;
  test with `--dry-run` for every agent and one real `--scope project` install into a temporary directory.
- Before opening a pull request run `python3 scripts/check_version.py`, `python3 scripts/check_readmes.py`,
  `python3 -m py_compile scripts/*.py examples/runner/runner.py` and `sh -n scripts/install.sh`.
- Product feedback (wrong answer, missing endpoint, pricing) is better sent through the API: `POST /v1/feedback`
  with the `X-Request-Id` of the call. Bugs in this repository go to GitHub issues.

By contributing you agree your work is released under the MIT license in `LICENSE`.
