#!/usr/bin/env python3
"""Verify a SimianX webhook signature.

    X-SimianX-Signature: t=<unix seconds>,v1=<hex hmac_sha256(secret, f"{t}.{body}")>

    python3 webhook_verify.py <secret> '<header value>' < body.json      # exit 0 valid, 1 invalid

Or import `verify()` into your handler. Bodies older than 300 seconds are refused (replay protection)."""
import hashlib
import hmac
import sys
import time


def verify(secret: str, header: str, body: str, tolerance: int = 300, now=None) -> bool:
    try:
        parts = dict(p.split("=", 1) for p in (header or "").split(","))
        ts, given = int(parts["t"]), parts["v1"]
    except (ValueError, KeyError, AttributeError):
        return False
    if abs((now if now is not None else int(time.time())) - ts) > tolerance:
        return False
    expected = hmac.new(secret.encode("utf-8"), f"{ts}.{body}".encode("utf-8"), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, given)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    ok = verify(sys.argv[1], sys.argv[2], sys.stdin.read())
    print("valid" if ok else "invalid")
    sys.exit(0 if ok else 1)
