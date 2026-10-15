#!/usr/bin/env sh
# Quote an autopilot cycle, then start one on BTC 15m with the fast tier.
API=${SIMIANX_API:-https://service.simianx.ai}
H1="Authorization: Bearer $SIMIANX_API_KEY"; H2="Content-Type: application/json"
curl -s "$API/v1/analysis/quote" -H "$H1" -H "$H2" -d '{"endpoint":"autopilots.create","tier":"fast"}' | python3 -m json.tool
curl -s "$API/v1/autopilots" -H "$H1" -H "$H2" -d '{"asset":"crypto","symbol":"BTC","timeframe":"15m","tier":"fast"}' | python3 -m json.tool
