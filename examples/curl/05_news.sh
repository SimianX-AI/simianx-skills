#!/usr/bin/env sh
# Latest classified news for BTC and NVDA, then the live stream (Plus and above).
API=${SIMIANX_API:-https://service.simianx.ai}
curl -s "$API/v1/news?symbols=BTC,NVDA&min_value=medium&limit=10" -H "Authorization: Bearer $SIMIANX_API_KEY" | python3 -m json.tool
curl -N "$API/v1/news/stream?symbols=BTC,NVDA&min_value=medium" -H "Authorization: Bearer $SIMIANX_API_KEY" -H "Accept: text/event-stream"
