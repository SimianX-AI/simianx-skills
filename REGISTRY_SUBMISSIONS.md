# Listing the SimianX MCP server

What every directory needs, in one place:

| | |
|---|---|
| Server URL | `https://service.simianx.ai/v1/mcp` (Streamable HTTP; MCP 2026-07-28 and 2025-03-26 … 2025-11-25) |
| Auth | `Authorization: Bearer <SimianX API key>` (or `X-API-Key: <key>`). No OAuth. `initialize`, `server/discover` and `tools/list` answer without a key, so scanners can read the tools. |
| Registry name | `io.github.SimianX-AI/simianx` (`server.json`) |
| Server card | `https://service.simianx.ai/v1/mcp/server-card` (also `https://www.simianx.ai/.well-known/mcp/server-card.json`) |
| Agent card (A2A) | `https://www.simianx.ai/.well-known/agent-card.json` · AI Catalog `https://www.simianx.ai/.well-known/ai-catalog.json` |
| Website / docs | `https://www.simianx.ai/agents#mcp` |
| Repository | `https://github.com/SimianX-AI/simianx-skills` |
| Icon | `https://www.simianx.ai/apple-icon-180x180.png` (180×180 PNG) |
| One line | Live multi-agent analysis and scored market news for US stocks and crypto, from SimianX AI. |
| Category | Finance / market data |

Longer description (for forms with room): *SimianX AI runs AI analysts on US stocks and crypto. Four live agents read
the chart, the news flow and the fundamentals and make a call with entry, stop and target; every news article is scored
for the symbols it moves, its value and its sentiment (the feed behind Market Pulse). Also 8-agent deep research,
Market Pulse events, Sector Watch catalysts and autopilots. One tool per API endpoint; calls use the account's points
at the website's rates.*

Never paste a real key into a directory form; scanners only need the public `tools/list`.

## 1. Official MCP Registry (registry.modelcontextprotocol.io) — automatic

Done by `.github/workflows/publish-mcp.yml` on every `vX.Y.Z` tag (GitHub OIDC, no secret). First publication: push
this branch to `main`, then tag the current release (see RELEASING.md). Manual fallback, from this directory:

```sh
curl -fsSL "https://github.com/modelcontextprotocol/registry/releases/latest/download/mcp-publisher_$(uname -s | tr '[:upper:]' '[:lower:]')_$(uname -m | sed 's/x86_64/amd64/;s/aarch64/arm64/').tar.gz" | tar xz mcp-publisher
./mcp-publisher login github      # device flow as simianxai: must be an Owner of the SimianX-AI org
./mcp-publisher publish
curl -s "https://registry.modelcontextprotocol.io/v0/servers?search=io.github.SimianX-AI/simianx"
```

Rules that bite: the namespace `io.github.SimianX-AI/*` is granted only to org Owners (device flow) or to workflows of
repos in the org (OIDC); a remote URL can belong to one server name only; `description` ≤ 100 characters; only
`_meta["io.modelcontextprotocol.registry/publisher-provided"]` survives publishing. To list under the domain instead
(`ai.simianx/simianx`), DNS-verify `simianx.ai` (apex TXT `v=MCPv1; k=ed25519; p=…`, `mcp-publisher login dns`) and
rename in `server.json` and the backend `card.REGISTRY_NAME` together.

## 2. Smithery (smithery.ai)

Remote servers are added by URL; Smithery scans `tools/list` itself. The `Authorization` header is reserved for
Smithery's own OAuth, so the key travels as `X-API-Key` (the backend accepts it), declared in
`smithery.config-schema.json`:

```sh
npx -y @smithery/cli mcp publish "https://service.simianx.ai/v1/mcp" -n @simianx/simianx \
  --config-schema "$(python3 -c 'import json;print(json.dumps(json.load(open("smithery.config-schema.json"))))')"
```

Or the web form at https://smithery.ai/new with the same URL and schema. Needs a Smithery account (GitHub login as
simianxai) and the `@simianx` namespace. If a scan answers 403, check that nothing in front of service.simianx.ai
blocks Smithery's scanner.

## 3. Glama (glama.ai)

Glama lists remote servers as *connectors* and syncs them from the official registry, so step 1 is the submission;
the page appears as `https://glama.ai/mcp/connectors/io.github.SimianX-AI/simianx` with a tool-definition-quality
score. To speed it up or claim it, sign in at https://glama.ai with GitHub (simianxai) and use "Add server" /
claim on that page. The score badge for READMEs is
`https://glama.ai/mcp/connectors/io.github.SimianX-AI/simianx/badges/score.svg`.

## 4. mcp.so

https://mcp.so/submit → type **Remote Server**; name `SimianX AI`; URL `https://service.simianx.ai/v1/mcp`;
repository `https://github.com/SimianX-AI/simianx-skills`; the one-line and long descriptions above. Sign in first
(GitHub). The "Pay and submit automatically" option is not needed.

## 5. PulseMCP

Submissions are paused (October 2026); PulseMCP says it will pick servers up from the official registry when they
reopen. Nothing to do beyond step 1; check https://www.pulsemcp.com/submit later.

## 6. Cursor directory (cursor.directory)

Sign in with GitHub at https://cursor.directory/mcp, choose Submit, and give the name, the URL, the description, the
repository and this install config (`~/.cursor/mcp.json`):

```json
{"mcpServers":{"simianx":{"url":"https://service.simianx.ai/v1/mcp","headers":{"Authorization":"Bearer ${env:SIMIANX_API_KEY}"}}}}
```

"Add to Cursor" deeplink for the listing or our site:
`cursor://anysphere.cursor-deeplink/mcp/install?name=simianx&config=eyJ1cmwiOiJodHRwczovL3NlcnZpY2Uuc2ltaWFueC5haS92MS9tY3AiLCJoZWFkZXJzIjp7IkF1dGhvcml6YXRpb24iOiJCZWFyZXIgJHtlbnY6U0lNSUFOWF9BUElfS0VZfSJ9fQ==`

## 7. awesome-mcp-servers

`punkpeye/awesome-mcp-servers` takes servers you install and run yourself; a hosted URL belongs in
`punkpeye/awesome-remote-mcp-servers` (entries are listed after the URL answers `initialize`). Fork it, add under
**💰 Finance**, in alphabetical order, and open a PR titled "Add SimianX AI":

```markdown
- [SimianX AI](https://www.simianx.ai/agents) `https://service.simianx.ai/v1/mcp`
  🔑 - Live multi-agent analysis (entry, stop, target) and scored market news for US stocks and crypto; deep research, Market Pulse, Sector Watch.
```

Add the Glama connector badge line used by the neighbouring entries once step 3 exists.

## Keeping listings current

Nothing per release: `publish-mcp` publishes the new version, the registry-fed directories follow it, and every
scanner reads the live `tools/list` (generated from the API's endpoint registry, so new endpoints appear on deploy).
Only the name, URL, icon or description changing needs the manual pages above redone.
