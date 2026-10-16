#!/usr/bin/env python3
"""One version everywhere.

    python3 scripts/check_version.py                      # consistency across the repo
    python3 scripts/check_version.py v1.0.0               # also require this tag
    python3 scripts/check_version.py --web ../simianx-web-app/public/SKILL.md \
                                     --backend ../simianx-backend/simianx_api/v1/policy/version.py
    python3 scripts/check_version.py v1.0.1 --live https://service.simianx.ai/v1/mcp/server-card --wait 600

Carriers: skills/simianx/SKILL.md (metadata.version, the "This file is version" line, both X-SimianX-Skill lines),
examples/runner/runner.py SKILL_VERSION, the CHANGELOG head, .claude-plugin/plugin.json, .claude-plugin/marketplace.json
(metadata.version and plugins[].version), plugin.json, .cursor-plugin/plugin.json, .cursor-plugin/marketplace.json,
gemini-extension.json, server.json (MCP Registry entry). .agents/plugins/marketplace.json has no version field; it is parsed and its plugin name checked.
--web requires the site's public/SKILL.md to be byte-identical to the skill; --backend requires SKILL_VERSION in the
backend's version.py to match and the backend's MCP name (simianx_api/v1/mcp/card.py REGISTRY_NAME) to equal
server.json `name`; --web also checks the site's .well-known/skills/index.json `version`. --live fetches the running
MCP server card and requires its version and name to match (retrying up to --wait seconds, for a deploy in progress):
the registry workflow publishes only what the server already runs. The MCP serverInfo, server card and the A2A agent
card are built by the backend from SKILL_VERSION at runtime, so they have no carrier of their own.
"""
import argparse
import json
import pathlib
import re
import sys
import time
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/simianx/SKILL.md"
RUNNER = ROOT / "examples/runner/runner.py"
CHANGELOG = ROOT / "CHANGELOG.md"
SEMVER = r"([0-9]+\.[0-9]+\.[0-9]+)"
JSON_CARRIERS = {
    ".claude-plugin/plugin.json": ["version"],
    ".claude-plugin/marketplace.json": ["metadata.version", "plugins[].version"],
    "plugin.json": ["version"],
    ".cursor-plugin/plugin.json": ["version"],
    ".cursor-plugin/marketplace.json": ["metadata.version", "plugins[].version"],
    "gemini-extension.json": ["version"],
    "server.json": ["version"],
}
SERVER_JSON = ROOT / "server.json"


def registry_name() -> str:
    return json.loads(SERVER_JSON.read_text(encoding="utf-8"))["name"]


def live_card(url: str, wait: int) -> dict:
    deadline = time.time() + wait
    while True:
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/mcp-server-card+json", "User-Agent": "simianx-release"})
            with urllib.request.urlopen(req, timeout=20) as res:
                return json.loads(res.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001
            if time.time() >= deadline:
                sys.exit(f"{url}: {exc}")
        time.sleep(20)


def skill_version() -> str:
    head = SKILL.read_text(encoding="utf-8").split("---", 2)[1]
    m = re.search(r'^\s*version:\s*"?' + SEMVER + '"?', head, re.M)
    return m.group(1) if m else sys.exit("SKILL.md: no metadata.version in the frontmatter")


def runner_version() -> str:
    m = re.search(r'^SKILL_VERSION\s*=\s*"' + SEMVER + '"', RUNNER.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else sys.exit("runner.py: no SKILL_VERSION")


def changelog_head() -> str:
    m = re.search(r"^## \[?v?" + SEMVER, CHANGELOG.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else sys.exit("CHANGELOG.md: no version heading")


def json_field(doc, path: str):
    """`a.b`, `a[].b` (every element) → list of values present."""
    out = [doc]
    for part in path.split("."):
        nxt = []
        for cur in out:
            if part.endswith("[]"):
                nxt.extend(cur.get(part[:-2], []) if isinstance(cur, dict) else [])
            elif isinstance(cur, dict) and part in cur:
                nxt.append(cur[part])
        out = nxt
    return out


def json_versions() -> dict:
    found = {}
    for rel, paths in JSON_CARRIERS.items():
        p = ROOT / rel
        if not p.exists():
            sys.exit(f"{rel}: missing")
        try:
            doc = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            sys.exit(f"{rel}: invalid JSON ({exc})")
        for path in paths:
            vals = json_field(doc, path)
            if not vals:
                if path == "metadata.version":
                    continue  # optional
                sys.exit(f"{rel}: no {path}")
            for i, v in enumerate(vals):
                found[f"{rel} {path}" + (f"#{i}" if len(vals) > 1 else "")] = str(v)
    codex = ROOT / ".agents/plugins/marketplace.json"
    if not codex.exists():
        sys.exit(".agents/plugins/marketplace.json: missing")
    try:
        doc = json.loads(codex.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        sys.exit(f".agents/plugins/marketplace.json: invalid JSON ({exc})")
    if not any(p.get("name") == "simianx" for p in doc.get("plugins", [])):
        sys.exit(".agents/plugins/marketplace.json: no plugin named simianx")
    return found


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("tag", nargs="?", help="git tag, e.g. v1.0.0")
    ap.add_argument("--web", help="path to the web app's public/SKILL.md (must equal skills/simianx/SKILL.md)")
    ap.add_argument("--backend", help="path to the backend's simianx_api/v1/policy/version.py (SKILL_VERSION must match)")
    ap.add_argument("--live", help="URL of the running MCP server card; its version and name must match")
    ap.add_argument("--wait", type=int, default=0, help="with --live: keep retrying a mismatch for this many seconds")
    args = ap.parse_args()

    versions = {"SKILL.md": skill_version(), "runner.py": runner_version(), "CHANGELOG.md": changelog_head()}
    body = SKILL.read_text(encoding="utf-8")
    mentions = re.findall(r"X-SimianX-Skill: " + SEMVER, body) + re.findall(r"This file is version `" + SEMVER + "`", body)
    if len(re.findall(r"X-SimianX-Skill: " + SEMVER, body)) < 2:
        sys.exit("SKILL.md: expected two X-SimianX-Skill lines in the body")
    for i, v in enumerate(mentions):
        versions[f"SKILL.md body #{i}"] = v
    versions.update(json_versions())
    if args.tag:
        versions["tag"] = args.tag.lstrip("v")
    if args.backend:
        text = pathlib.Path(args.backend).read_text(encoding="utf-8")
        m = re.search(r'^SKILL_VERSION\s*=\s*"' + SEMVER + '"', text, re.M)
        versions["backend version.py"] = m.group(1) if m else sys.exit(f"{args.backend}: no SKILL_VERSION")
        card = pathlib.Path(args.backend).resolve().parent.parent / "mcp" / "card.py"
        if card.exists():
            m = re.search(r'^REGISTRY_NAME\s*=\s*"([^"]+)"', card.read_text(encoding="utf-8"), re.M)
            if not m or m.group(1) != registry_name():
                sys.exit(f"{card}: REGISTRY_NAME {m.group(1) if m else None!r} differs from server.json name {registry_name()!r}")
    if args.web:
        web = pathlib.Path(args.web)
        if web.read_bytes() != SKILL.read_bytes():
            sys.exit(f"{web} differs from {SKILL.relative_to(ROOT)}: copy the skill file to the site")
        versions["web public/SKILL.md"] = "identical → " + versions["SKILL.md"]
        index = web.parent / ".well-known" / "skills" / "index.json"
        if index.exists():
            for i, entry in enumerate(json.loads(index.read_text(encoding="utf-8")).get("skills", [])):
                versions[f"web skills index #{i}"] = str(entry.get("version"))
    if args.live:
        want = versions.get("tag") or versions["SKILL.md"]
        deadline = time.time() + args.wait
        while True:
            card = live_card(args.live, max(0, int(deadline - time.time())))
            if (card.get("version") == want and card.get("name") == registry_name()) or time.time() >= deadline:
                break
            print(f"live card at {card.get('version')} ({card.get('name')}), waiting for {want} ...", flush=True)
            time.sleep(30)
        if card.get("name") != registry_name():
            sys.exit(f"live server card name {card.get('name')!r} differs from server.json {registry_name()!r}")
        versions["live MCP server card"] = str(card.get("version"))

    width = max(len(k) for k in versions)
    for name, v in versions.items():
        print(f"{name:{width}}  {v}")
    distinct = sorted({v.split("→ ")[-1] for v in versions.values()})
    if len(distinct) != 1:
        sys.exit(f"versions differ: {distinct}")
    print(f"ok: {distinct[0]}")


if __name__ == "__main__":
    main()
