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
9. `server.json` (the MCP Registry entry for the remote MCP server): `version`. Its `name`
   (`io.github.SimianX-AI/simianx`) never changes; it must equal the backend's `simianx_api/v1/mcp/card.py`
   `REGISTRY_NAME`, which `--backend` checks.
10. The git tag `vX.Y.Z`.

`.agents/plugins/marketplace.json` (Codex) has no version field; it is checked for validity and the plugin name only.
The READMEs carry no version on purpose (they link `CHANGELOG.md` and `GET /v1/skill`), so a release never touches
the 16 translations.

In the sibling repositories, in the same change:

11. Backend `simianx_api/v1/policy/version.py`: `SKILL_VERSION` and the changelog head (`MIN_SKILL_VERSION` only
    when the old behaviour is gone).
12. Web `public/SKILL.md`: a byte-identical copy of `skills/simianx/SKILL.md`; `public/INSTALL.md` a copy of
    `INSTALL.md`; `public/.well-known/skills/index.json` `version` (`--web` checks the index too).

Not carriers, on purpose: the MCP server's `serverInfo.version`, its instructions, `GET /v1/mcp/server-card` and the
A2A agent card (`GET /v1/agent-card`, served on www as `/.well-known/agent-card.json` and `agent.json` by a rewrite)
are all built by the backend from `SKILL_VERSION` at runtime, so carrier 11 moves them. The MCP tool list is generated
from the backend's endpoint registry, so a new endpoint becomes a tool with the backend deploy, with no edit here.

## Steps

1. Bump every carrier above.
2. `python3 scripts/check_version.py --web ../simianx-web-app/public/SKILL.md --backend ../simianx-backend/simianx_api/v1/policy/version.py`
   must print `ok`. `python3 scripts/check_readmes.py` must print `ok` (the 16 READMEs agree on logo, navigation,
   URLs and code blocks).
3. Validate the manifests: `for f in plugin.json gemini-extension.json .claude-plugin/*.json .cursor-plugin/*.json .agents/plugins/marketplace.json; do python3 -m json.tool $f >/dev/null; done`
   and, with Claude Code installed, `claude plugin validate .`.
4. Ship the backend first (its `SKILL_VERSION` is what the MCP server reports), then commit here, tag and push:
   `git tag vX.Y.Z && git push origin main vX.Y.Z`.
5. The `release` workflow re-runs the checks against the tag, zips `skills/simianx` and publishes a GitHub release
   with the changelog section as its notes. Agents install from the release, the raw files on `main`, or SKILL.md on
   the site; Claude Code plugin users receive the update because `plugin.json` `version` changed.
6. The `publish-mcp` workflow publishes `server.json` to the official MCP Registry: it re-checks every carrier
   against the tag, validates `server.json` against the registry schema, waits (up to 20 minutes) until
   `https://service.simianx.ai/v1/mcp/server-card` reports the tag's version and the same name, then runs
   `mcp-publisher login github-oidc` and `mcp-publisher publish` (OIDC from this workflow: no token to store; the
   registry grants the `io.github.SimianX-AI/*` namespace to workflows of this organisation's repositories). If the
   backend is not live with the version yet, the job fails without publishing; rerun it from the Actions tab once
   it is. Other directories (Smithery, Glama, PulseMCP, mcp.so …) re-read the server or the registry on their own;
   see [REGISTRY_SUBMISSIONS.md](REGISTRY_SUBMISSIONS.md).

Old clients: an MCP client or skill that reports a version below the backend's `MIN_SKILL_VERSION`
(`X-SimianX-Skill` header, or `_meta["ai.simianx/skill_version"]` on an MCP tool call) gets `426 skill_outdated` with
the URL to re-read, as a tool error over MCP; a client that reports nothing is never refused. A client holding an old
tool list gets "unknown tool" / `unknown_arguments` with the current catalogue hash and re-lists.

Breaking changes never edit an endpoint in place: the API adds the new path or field, marks the old one deprecated
with a sunset date, and only raises its minimum skill version once the old behaviour is gone.
