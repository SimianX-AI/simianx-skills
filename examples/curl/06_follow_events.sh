#!/usr/bin/env sh
# Long-poll an autopilot's event log. Usage: 06_follow_events.sh <autopilot id> [cursor]
API=${SIMIANX_API:-https://service.simianx.ai}
ID=$1; CURSOR=${2:-0}
while true; do
  OUT=$(curl -s "$API/v1/autopilots/$ID/events?after=$CURSOR&wait=30&types=position.changed,signal.fired,autopilot.stopped" \
    -H "Authorization: Bearer $SIMIANX_API_KEY")
  printf "%s" "$OUT" | python3 -c 'import json,sys; d=json.load(sys.stdin)["data"]; [print(e["ts"], e["type"], json.dumps(e["data"])[:160]) for e in d["events"]]; print("cursor", d["cursor"])'
  CURSOR=$(printf "%s" "$OUT" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["cursor"])')
done
