#!/usr/bin/env sh
# Keep watching: the same four agents on BTC 15m, on every cycle, with a paper position and an event log.
API=${SIMIANX_API:-https://service.simianx.ai}
H1="Authorization: Bearer $SIMIANX_API_KEY"; H2="Content-Type: application/json"
curl -s "$API/v1/autopilots" -H "$H1" -H "$H2" -d '{"asset":"crypto","symbol":"BTC","timeframe":"15m","tier":"fast"}' | python3 -m json.tool
