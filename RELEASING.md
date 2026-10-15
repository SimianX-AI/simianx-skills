# Releasing

Published from the `SimianX-AI` organisation by the `simianxai` account. Nothing else on the machine changes: this
repository alone uses the `github-simianxai` SSH alias (`~/.ssh/config`) and a repo-local `user.name` / `user.email`.

1. Bump the version in three places to the same number: `skills/simianx/SKILL.md` (`metadata.version`, the
   `X-SimianX-Skill:` lines and "This file is version"), `examples/runner/runner.py` (`SKILL_VERSION`) and a new
   `## X.Y.Z - date` section at the top of `CHANGELOG.md`. The backend's `simianx_api/v1/policy/version.py`
   (`SKILL_VERSION`, changelog head) and the web `public/SKILL.md` carry the same number in the same change.
2. `python3 scripts/check_version.py` must print `ok`.
3. Commit, then tag and push: `git tag vX.Y.Z && git push origin main vX.Y.Z`.
4. The `release` workflow checks the tag against the files, zips `skills/simianx`, and publishes a GitHub release with
   the changelog section as its notes. Agents install from the release or read SKILL.md from the site.

Breaking changes never edit an endpoint in place: the API adds the new path or field, marks the old one deprecated
with a sunset date, and only raises its minimum skill version once the old behaviour is gone.
