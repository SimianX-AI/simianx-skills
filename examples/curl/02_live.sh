#!/usr/bin/env sh
# The four live agents on BTC 15m, once: start the run, wait for it, print what each agent concluded.
API=${SIMIANX_API:-https://service.simianx.ai}
H1="Authorization: Bearer $SIMIANX_API_KEY"; H2="Content-Type: application/json"
RUN=$(curl -s "$API/v1/analysis/live" -H "$H1" -H "$H2" -d '{"asset":"crypto","symbol":"BTC","timeframe":"15m"}' \
  | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["run"]["id"])')
[ -n "$RUN" ] || { echo "could not start the run"; exit 1; }
echo "run $RUN"
for _ in $(seq 1 20); do
  OUT=$(curl -s "$API/v1/analysis/live/$RUN?wait=30" -H "$H1")
  STATUS=$(printf "%s" "$OUT" | python3 -c 'import json,sys; print(json.load(sys.stdin)["data"]["run"]["status"])')
  case "$STATUS" in done|partial|failed) break ;; esac
done
printf "%s" "$OUT" | python3 -c 'import json,sys; r=json.load(sys.stdin)["data"]["run"]; [print(a["agent"], json.dumps(a.get("conclusion"))[:200]) for a in r.get("analyses", [])]'
