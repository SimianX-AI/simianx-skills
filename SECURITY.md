# Security

## Reporting

Report a vulnerability privately through
[GitHub security advisories](https://github.com/SimianX-AI/simianx-skills/security/advisories/new) for anything in
this repository, or through `POST /v1/feedback` (category `bug`) for the API itself. Do not open a public issue for a
security problem. We acknowledge reports within three business days.

## What the skill touches

- The skill is Markdown instructions read by your AI agent. It runs no code of its own; `scripts/` and
  `examples/` are optional tools you run deliberately, standard library only, and they never read or write anything
  outside the skill folder they install or the files they are pointed at.
- The agent calls `https://service.simianx.ai/v1/*` over HTTPS and nothing else. It reads `SIMIANX_API_KEY` from the
  environment at call time. The skill never asks the agent to store the key, print it, or send it anywhere but the
  `Authorization` header to that host.
- The install scripts download the skill files from `raw.githubusercontent.com/SimianX-AI/simianx-skills` (or
  `www.simianx.ai`) and copy them into the agent's skills directory. They refuse to overwrite a folder that is not
  this skill unless `--force` is given.
- Keys carry scopes (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`, `billing:manage`), optional
  daily and monthly points budgets, a per-call cap, an expiry and an IP whitelist. Use the narrowest scope and a
  daily budget for unattended agents. Revoke a key at any time at My Account → API keys; `GET /v1/usage` shows every
  charge.
- The skill never asks for card details, never changes a subscription and never pays; a 402 is handed to the human
  as a link.
