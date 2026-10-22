#!/usr/bin/env sh
# Follow everything this key's runs produce: the updates feed, acked with the last id relayed. Usage: 06_follow_events.sh [ack]
API=${SIMIANX_API:-https://service.simianx.ai}
ACK=${1:-0}
while true; do
  OUT=$(curl -s "$API/v1/updates?ack=$ACK&wait=30&notify=1" -H "Authorization: Bearer $SIMIANX_API_KEY" -H "X-SimianX-Skill: 1.0.6")
  printf "%s" "$OUT" | python3 -c 'import json,sys; d=json.load(sys.stdin)["data"]; [print(u["id"], u["kind"], u["say"], "|", u.get("ask") or "") for u in d["updates"]]; print("pending", d["pending"])'
  ACK=$(printf "%s" "$OUT" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["cursor"])')
done
