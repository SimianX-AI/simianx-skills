#!/usr/bin/env sh
# Start a deep analysis on NVDA and follow it until done.
API=${SIMIANX_API:-https://service.simianx.ai}
H1="Authorization: Bearer $SIMIANX_API_KEY"; H2="Content-Type: application/json"
ID=$(curl -s "$API/v1/analysis/deep" -H "$H1" -H "$H2" -d '{"asset":"stock","symbol":"NVDA","horizon":"swing","tier":"fast"}' | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["id"])')
echo "deep $ID"
CURSOR=0
while true; do
  OUT=$(curl -s "$API/v1/analysis/deep/$ID/events?after=$CURSOR&wait=30" -H "$H1")
  printf "%s" "$OUT" | python3 -c 'import json,sys; d=json.load(sys.stdin)["data"]; [print(e["type"], e.get("step",""), e.get("status","")) for e in d["events"]]'
  CURSOR=$(printf "%s" "$OUT" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["cursor"])')
  BUSY=$(printf "%s" "$OUT" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["busy"])')
  [ "$BUSY" = "False" ] && break
done
curl -s "$API/v1/analysis/deep/$ID" -H "$H1" | python3 -c 'import json,sys; print(json.dumps(json.load(sys.stdin)["data"]["verdict"], indent=2))'
