#!/usr/bin/env sh
# A quick read (one pass of the four live agents) on BTC 15m, followed through the updates feed; then a live session.
API=${SIMIANX_API:-https://service.simianx.ai}
H1="Authorization: Bearer $SIMIANX_API_KEY"; H2="Content-Type: application/json"; H3="X-SimianX-Skill: 1.0.6"
curl -s "$API/v1/analysis/quick" -H "$H1" -H "$H2" -H "$H3" -d '{"asset":"crypto","symbol":"BTC","timeframe":"15m"}' | python3 -m json.tool
ACK=0
for _ in $(seq 1 20); do
  OUT=$(curl -s "$API/v1/updates?ack=$ACK&wait=30&notify=1" -H "$H1" -H "$H3")
  printf "%s" "$OUT" | python3 -c 'import json,sys; d=json.load(sys.stdin)["data"]; [print(u["id"], u["kind"], u["say"], "|", u.get("ask") or "") for u in d["updates"]]'
  ACK=$(printf "%s" "$OUT" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["cursor"])')
  printf "%s" "$OUT" | python3 -c 'import json,sys; d=json.load(sys.stdin)["data"]; sys.exit(0 if any(u["kind"]=="next_run" for u in d["updates"]) else 1)' && break
done
# keep analysing at every candle close: a live session (stay connected to data.ws_url with the bearer header)
curl -s "$API/v1/live/sessions" -H "$H1" -H "$H2" -H "$H3" -d '{"asset":"crypto","symbol":"BTC","timeframe":"15m"}' | python3 -m json.tool
