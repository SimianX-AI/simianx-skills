**What changes**

**Checklist**

- [ ] `python3 scripts/check_version.py` passes (no version bump in a feature PR)
- [ ] `python3 scripts/check_readmes.py` passes; a README change is mirrored into all 16 languages
- [ ] Prices, limits and field names match the API (`GET /v1/pricing`, `/v1/openapi.json`)
- [ ] Copy says "points", never "credits"; no data vendor names; no API keys anywhere
- [ ] `scripts/install.py --agent all --dry-run` still works if scripts changed
