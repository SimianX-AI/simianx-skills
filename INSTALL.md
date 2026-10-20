# Install the SimianX skill

**If you are an agent reading this:** pick your client below, run its lines, then make sure `SIMIANX_API_KEY` is set
in the environment. If it is not, sign the user in from the agent as SKILL.md "Setup" step 1 describes (a link the
user approves in the browser, or a 6-digit code mailed to them; both end in a key for this agent only) and read
https://www.simianx.ai/SKILL.md to learn the API. Never commit the key. Humans: the one sentence to paste to any
agent is

```
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and sign me in.
```

The skill is one folder, `simianx/`, holding `SKILL.md` and `references/*.md`. Every client below reads the
[Agent Skills](https://agentskills.io) format; only the directory differs. Project scope = inside the current
repository (committed and shared); user scope = your home directory (every project).

## Fastest: one command for any client

```sh
npx skills add SimianX-AI/simianx-skills            # picks the agents it finds; -a <agent> for one, -g for user scope
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI; --agent <id>, --scope user
```

Or the install script (python3 if present, plain copy otherwise; `--agent auto` installs for every agent whose
config directory exists):

```sh
curl -fsSL https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main/scripts/install.sh | sh -s -- --agent auto
# Windows: irm https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main/scripts/install.ps1 -OutFile install.ps1; .\install.ps1 -Agent auto
```

## Agents with their own computer (Muse, Grok Bot, dots)

Agents that run on their own cloud computer or VM, and keep secrets in a credential store instead of a shell
profile, install SimianX the same way: connect, sign the user in, save it as a skill.

1. **Connect.** If you can add MCP servers or connectors, add the remote server below
   (`https://service.simianx.ai/v1/mcp`, Streamable HTTP, bearer token). If you build connectors from an API
   instead, build it from `https://service.simianx.ai/v1/openapi.json` with bearer auth. If you can write a skills
   directory, also copy `skills/simianx` there (any route above).
2. **Sign in.** Run SKILL.md "Setup" step 1 over HTTPS: the browser link (`POST /v1/auth/link`) or the emailed
   6-digit code (`POST /v1/auth/code`). Put the token in your secure credential prompt or secret store, never in the
   chat, and give it a daily points budget when you will work while the user is away.
3. **Save the playbook.** Save https://www.simianx.ai/SKILL.md (and its `references/*.md`) as a reusable skill or
   instructions, so later questions about a stock, a coin, news or catalysts go to SimianX: the 8-agent committee
   for a full verdict, the four live agents for a read on a timeframe, the news stream to keep watching.
4. **Test it.** `GET /v1/me`, then one cheap call (`GET /v1/news?symbols=BTC&limit=3`), and show the user the result.

Per agent:

| Agent | What to tell it |
|---|---|
| Muse (Meta) | `Create a custom connector for SimianX AI from https://service.simianx.ai/v1/openapi.json, sign me in as https://www.simianx.ai/INSTALL.md describes, and save it as a skill.` |
| Grok Bot (xAI) | `Connect the SimianX MCP server https://service.simianx.ai/v1/mcp, sign me in as https://www.simianx.ai/INSTALL.md describes, and save the SimianX skill.` |
| dots (OpenAI) | `Install the SimianX skill from https://www.simianx.ai/INSTALL.md and sign me in.` |

## Connect over MCP

No skill needed: an MCP client can use SimianX as tools (live analysis, scored news, deep research, Market Pulse,
Sector Watch, autopilots, account). Remote server `https://service.simianx.ai/v1/mcp` (Streamable HTTP), auth `Authorization: Bearer <key>` (or
`X-API-Key: <key>`), the same key, scopes, limits and points as the REST API. Set `SIMIANX_API_KEY` first.

| Client | Where | Snippet |
|---|---|---|
| Claude Code | terminal | `claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"` |
| Claude Desktop | `claude_desktop_config.json` | `{"mcpServers": {"simianx": {"command": "npx", "args": ["-y", "mcp-remote", "https://service.simianx.ai/v1/mcp", "--header", "Authorization: Bearer ${SIMIANX_API_KEY}"], "env": {"SIMIANX_API_KEY": "simx_live_..."}}}}` |
| Cursor | `~/.cursor/mcp.json` | `{"mcpServers": {"simianx": {"url": "https://service.simianx.ai/v1/mcp", "headers": {"Authorization": "Bearer ${env:SIMIANX_API_KEY}"}}}}` |
| Codex | terminal | `codex mcp add simianx --url https://service.simianx.ai/v1/mcp --bearer-token-env-var SIMIANX_API_KEY` |
| VS Code / Copilot | `.vscode/mcp.json` | `{"inputs": [{"type": "promptString", "id": "simianx-key", "description": "SimianX API key", "password": true}], "servers": {"simianx": {"type": "http", "url": "https://service.simianx.ai/v1/mcp", "headers": {"Authorization": "Bearer ${input:simianx-key}"}}}}` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` | `{"mcpServers": {"simianx": {"serverUrl": "https://service.simianx.ai/v1/mcp", "headers": {"Authorization": "Bearer ${env:SIMIANX_API_KEY}"}}}}` |
| Grok Bot | chat | `Connect the MCP server https://service.simianx.ai/v1/mcp (Streamable HTTP) with my SimianX API key as a bearer token. Ask me for the key in the secure prompt.` |
| Muse | chat | `Create a custom connector from the MCP server https://service.simianx.ai/v1/mcp with bearer auth. Ask me for my SimianX API key in the secure prompt.` |
| Gemini CLI | terminal | `gemini mcp add --transport http --header "Authorization: Bearer $SIMIANX_API_KEY" simianx https://service.simianx.ai/v1/mcp` |

The tool list follows the API (one tool per endpoint), so new endpoints appear after a release without a client
update; list tools again if a call answers "unknown tool". Discovery: server card `https://service.simianx.ai/v1/mcp/server-card`, agent card
`https://www.simianx.ai/.well-known/agent-card.json`, MCP Registry name `io.github.SimianX-AI/simianx`.

## By hand, per client

`FILES` below is the same for every client. Replace `DIR` with the directory from the table and run:

```sh
DIR=~/.agents/skills/simianx   # <- pick from the table
RAW=https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main/skills/simianx
mkdir -p "$DIR/references" "$DIR/agents"
for f in SKILL.md agents/openai.yaml references/auth.md references/autopilots.md references/billing.md \
         references/data.md references/deep.md references/live.md references/news.md references/sectors.md; do
  curl -fsSL "$RAW/$f" -o "$DIR/$f"
done
```

or clone and copy: `git clone https://github.com/SimianX-AI/simianx-skills && cp -R simianx-skills/skills/simianx "$DIR"`.
`~/.agents/skills` (user) and `./.agents/skills` (project) are read by Codex, Cursor, Copilot, Gemini CLI, Devin,
Amp, OpenCode, Zed, Kilo, Roo Code, Goose, Antigravity, Factory and OpenHands, so one copy there serves them all.
Claude Code reads only `~/.claude/skills` and `./.claude/skills`.

| Client | User scope `DIR` | Project scope `DIR` | Native command |
|---|---|---|---|
| Claude Code | `~/.claude/skills/simianx` | `.claude/skills/simianx` | `/plugin marketplace add SimianX-AI/simianx-skills` then `/plugin install simianx@simianx` |
| OpenAI Codex | `~/.agents/skills/simianx` (legacy `~/.codex/skills`) | `.agents/skills/simianx` | `codex plugin marketplace add SimianX-AI/simianx-skills`, then `/plugins` → simianx; or `npx skills add SimianX-AI/simianx-skills -a codex` |
| Cursor | `~/.cursor/skills/simianx` (syncs to Cloud Agents) | `.agents/skills/simianx` or `.cursor/skills/simianx` | Customize → From GitHub Repository → `SimianX-AI/simianx-skills`; or `npx skills add SimianX-AI/simianx-skills -a cursor` |
| GitHub Copilot (CLI, VS Code, cloud agent) | `~/.copilot/skills/simianx` | `.github/skills/simianx` or `.agents/skills/simianx` | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot`; or `copilot plugin marketplace add SimianX-AI/simianx-skills` + `copilot plugin install simianx@simianx` |
| Gemini CLI | `~/.gemini/skills/simianx` | `.agents/skills/simianx` or `.gemini/skills/simianx` | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent`; extension: `gemini extensions install https://github.com/SimianX-AI/simianx-skills` |
| Antigravity | `~/.gemini/config/skills/simianx` | `.agents/skills/simianx` | `agy plugin install https://github.com/SimianX-AI/simianx-skills`; or `npx skills add SimianX-AI/simianx-skills -a antigravity` |
| Windsurf / Devin Desktop | `~/.codeium/windsurf/skills/simianx` | `.devin/skills/simianx` (legacy `.windsurf/skills`) | `npx skills add SimianX-AI/simianx-skills -a windsurf`; Devin cloud reads `.agents/skills` in every connected repo |
| Cline | `~/.cline/skills/simianx` | `.cline/skills/simianx` | `npx skills add SimianX-AI/simianx-skills -a cline` |
| Roo Code | `~/.roo/skills/simianx` | `.roo/skills/simianx` or `.agents/skills/simianx` | `npx skills add SimianX-AI/simianx-skills -a roo` |
| Kilo Code | `~/.kilo/skills/simianx` | `.kilo/skills/simianx` or `.agents/skills/simianx` | `npx skills add SimianX-AI/simianx-skills -a kilo`; or `kilo.jsonc` → `"skills": {"urls": ["https://www.simianx.ai/.well-known/skills/"]}` |
| OpenCode | `~/.config/opencode/skills/simianx` | `.opencode/skills/simianx` or `.agents/skills/simianx` | `npx skills add SimianX-AI/simianx-skills -a opencode`; or tell OpenCode to fetch and follow this file |
| Amp | `~/.config/agents/skills/simianx` | `.agents/skills/simianx` | `amp skill add SimianX-AI/simianx-skills` (`--global` for user scope) |
| Zed | `~/.agents/skills/simianx` | `.agents/skills/simianx` (flat, trusted worktree) | `npx skills add SimianX-AI/simianx-skills -a zed`; or `agent: create skill from url` with the GitHub SKILL.md URL |
| Kiro | `~/.kiro/skills/simianx` | `.kiro/skills/simianx` | Skills panel → Import a skill → `https://github.com/SimianX-AI/simianx-skills/tree/main/skills/simianx`; or `npx skills add SimianX-AI/simianx-skills -a kiro-cli` |
| Factory Droid | `~/.factory/skills/simianx` | `.factory/skills/simianx` or `.agents/skills/simianx` | `droid plugin marketplace add https://github.com/SimianX-AI/simianx-skills` + `droid plugin install simianx@simianx`; or `npx skills add SimianX-AI/simianx-skills -a droid` |
| OpenHands | `~/.agents/skills/simianx` | `.agents/skills/simianx` | `npx skills add SimianX-AI/simianx-skills -a openhands` |
| Goose | `~/.config/goose/skills/simianx` | `.goose/skills/simianx` or `.agents/skills/simianx` | `npx skills add SimianX-AI/simianx-skills -a goose` |
| Trae | `~/.trae/skills/simianx` | `.trae/skills/simianx` | `npx skills add SimianX-AI/simianx-skills -a trae` |
| claude.ai / Claude API | upload `simianx-skill-<version>.zip` from the GitHub release (Customize → Skills → Upload) | — | API: `POST /v1/skills` with the same zip |

Script equivalents: `scripts/install.py --agent <claude|codex|cursor|copilot|gemini|windsurf|cline|roo|kilo|opencode|amp|zed|kiro|factory|openhands|goose|all|auto> [--scope user|project] [--link] [--source <path|url>] [--uninstall] [--dry-run] [--yes]`.

After installing, reload the client if it does not pick up new skills live (Codex: new session; Gemini: `/skills
reload`; Kilo: `/reload`; Cursor plugins: Developer → Reload Window; Claude Code: `/reload-plugins` for the plugin).

## Verify

```sh
curl -s https://service.simianx.ai/v1/skill
# → data.version is the current skill, data.minimum_version the oldest the API still accepts.
# Your copy's version is `metadata.version` in SKILL.md (also in .installed.json when the script installed it).
curl -s https://service.simianx.ai/v1/me -H "Authorization: Bearer $SIMIANX_API_KEY"   # plan, points, limits
```

A copy below `minimum_version` gets HTTP 426 on every call: reinstall (same lines as above) and retry.

## Security

The skill is instructions, not code: it tells the agent which HTTPS endpoints of `service.simianx.ai` to call, how to
quote a price in points before an AI call, and how to read answers. It runs no shell on its own; `examples/` and
`scripts/` are optional and stay in the repository. The only secret is `SIMIANX_API_KEY`, read from the environment
at call time: never commit it, never write it into a prompt, a skill file or a log. Create the key with the
narrowest scopes (`data:read` for research only; `analysis:run` to spend points; `automation:manage` for autopilots
and sector follows) and a daily points budget when the agent runs unattended. Every charge shows in `GET /v1/usage`
and on the site; revoke a key at any time at My Account → API keys. The skill never asks for a card number, never
changes a subscription and never pays on its own; it hands 402 links to the human. Report a problem at
https://github.com/SimianX-AI/simianx-skills/security/advisories/new or `POST /v1/feedback`.
