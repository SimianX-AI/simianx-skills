#!/usr/bin/env sh
# Account, points, key budgets and plan limits.
API=${SIMIANX_API:-https://service.simianx.ai}
curl -s "$API/v1/me" -H "Authorization: Bearer $SIMIANX_API_KEY" | python3 -m json.tool
