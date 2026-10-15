#!/usr/bin/env python3
"""One version everywhere.

    python3 scripts/check_version.py                      # consistency across the repo
    python3 scripts/check_version.py v1.2.0               # also require this tag
    python3 scripts/check_version.py --web ../simianx-web-app/public/SKILL.md \
                                     --backend ../simianx-backend/simianx_api/v1/policy/version.py

Carriers: skills/simianx/SKILL.md (metadata.version, the "This file is version" line, both X-SimianX-Skill lines),
examples/runner/runner.py SKILL_VERSION, the CHANGELOG head, .claude-plugin/plugin.json, .claude-plugin/marketplace.json
(metadata.version and plugins[].version), plugin.json, .cursor-plugin/plugin.json, .cursor-plugin/marketplace.json,
gemini-extension.json. .agents/plugins/marketplace.json has no version field; it is parsed and its plugin name checked.
--web requires the site's public/SKILL.md to be byte-identical to the skill; --backend requires SKILL_VERSION in the
backend's version.py to match.
"""
import argparse
import json
import pathlib
import re
import sys

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
}


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
    ap.add_argument("tag", nargs="?", help="git tag, e.g. v1.2.0")
    ap.add_argument("--web", help="path to the web app's public/SKILL.md (must equal skills/simianx/SKILL.md)")
    ap.add_argument("--backend", help="path to the backend's simianx_api/v1/policy/version.py (SKILL_VERSION must match)")
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
    if args.web:
        web = pathlib.Path(args.web)
        if web.read_bytes() != SKILL.read_bytes():
            sys.exit(f"{web} differs from {SKILL.relative_to(ROOT)}: copy the skill file to the site")
        versions["web public/SKILL.md"] = "identical → " + versions["SKILL.md"]

    width = max(len(k) for k in versions)
    for name, v in versions.items():
        print(f"{name:{width}}  {v}")
    distinct = sorted({v.split("→ ")[-1] for v in versions.values()})
    if len(distinct) != 1:
        sys.exit(f"versions differ: {distinct}")
    print(f"ok: {distinct[0]}")


if __name__ == "__main__":
    main()
