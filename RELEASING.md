# Releasing

Published from the `SimianX-AI` organisation by the `simianxai` account. Nothing else on the machine changes: this
repository alone uses the `github-simianxai` SSH alias (`~/.ssh/config`) and a repo-local `user.name` / `user.email`.

## Version carriers

One number, `X.Y.Z`, in every place below. `scripts/check_version.py` refuses a release when any of them differ.

In this repository:

1. `skills/simianx/SKILL.md`: `metadata.version`, the "This file is version `X.Y.Z`" line, both `X-SimianX-Skill: X.Y.Z` lines.
2. `examples/runner/runner.py`: `SKILL_VERSION`.
3. `CHANGELOG.md`: a new `## X.Y.Z - date` section at the top.
4. `.claude-plugin/plugin.json`: `version`.
5. `.claude-plugin/marketplace.json`: `metadata.version` and `plugins[0].version`.
6. `plugin.json` (Agent Plugins, root): `version`.
7. `.cursor-plugin/plugin.json` and `.cursor-plugin/marketplace.json`: same fields as the Claude files.
8. `gemini-extension.json`: `version`.
9. The git tag `vX.Y.Z`.

`.agents/plugins/marketplace.json` (Codex) has no version field; it is checked for validity and the plugin name only.
The READMEs carry no version on purpose (they link `CHANGELOG.md` and `GET /v1/skill`), so a release never touches
the 16 translations.

In the sibling repositories, in the same change:

10. Backend `simianx_api/v1/policy/version.py`: `SKILL_VERSION` and the changelog head (`MIN_SKILL_VERSION` only
    when the old behaviour is gone).
11. Web `public/SKILL.md`: a byte-identical copy of `skills/simianx/SKILL.md`; `public/INSTALL.md` a copy of
    `INSTALL.md`; `public/.well-known/skills/index.json` `version`.

## Steps

1. Bump every carrier above.
2. `python3 scripts/check_version.py --web ../simianx-web-app/public/SKILL.md --backend ../simianx-backend/simianx_api/v1/policy/version.py`
   must print `ok`. `python3 scripts/check_readmes.py` must print `ok` (the 16 READMEs agree on logo, navigation,
   URLs and code blocks).
3. Validate the manifests: `for f in plugin.json gemini-extension.json .claude-plugin/*.json .cursor-plugin/*.json .agents/plugins/marketplace.json; do python3 -m json.tool $f >/dev/null; done`
   and, with Claude Code installed, `claude plugin validate .`.
4. Commit, then tag and push: `git tag vX.Y.Z && git push origin main vX.Y.Z`.
5. The `release` workflow re-runs the checks against the tag, zips `skills/simianx` and publishes a GitHub release
   with the changelog section as its notes. Agents install from the release, the raw files on `main`, or SKILL.md on
   the site; Claude Code plugin users receive the update because `plugin.json` `version` changed.

Breaking changes never edit an endpoint in place: the API adds the new path or field, marks the old one deprecated
with a sunset date, and only raises its minimum skill version once the old behaviour is gone.
