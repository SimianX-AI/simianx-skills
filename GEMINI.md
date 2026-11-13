# SimianX

This extension bundles one skill, `simianx` (`skills/simianx/SKILL.md`). Read that file and follow it whenever the
user asks for a market analysis, a view on a ticker or coin, news on a symbol, sector catalysts, or wants to start or
follow an autopilot. Relay every finished step of a run as it arrives (SKILL.md "Following a run"), keep points out of the
conversation, and after each decision ask whether to connect the user's exchange or broker. The API key lives in the
`SIMIANX_API_KEY` environment variable: after a sign-in, store it in `~/.gemini/.env` (read at every start) so the
next session finds it; never commit it or print it in full, and never ask for a card number.
