#!/usr/bin/env python3
"""One version everywhere: SKILL.md frontmatter, the runner, the changelog head and (when given) the git tag.

    python3 scripts/check_version.py            # consistency only
    python3 scripts/check_version.py v1.2.0     # also require this tag
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills/simianx/SKILL.md"
RUNNER = ROOT / "examples/runner/runner.py"
CHANGELOG = ROOT / "CHANGELOG.md"


def skill_version() -> str:
    text = SKILL.read_text(encoding="utf-8")
    head = text.split("---", 2)[1]
    m = re.search(r'^\s*version:\s*"?([0-9]+\.[0-9]+\.[0-9]+)"?', head, re.M)
    if not m:
        sys.exit("SKILL.md: no metadata.version in the frontmatter")
    return m.group(1)


def runner_version() -> str:
    m = re.search(r'^SKILL_VERSION\s*=\s*"([0-9]+\.[0-9]+\.[0-9]+)"', RUNNER.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else sys.exit("runner.py: no SKILL_VERSION")


def changelog_head() -> str:
    m = re.search(r"^## \[?v?([0-9]+\.[0-9]+\.[0-9]+)", CHANGELOG.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else sys.exit("CHANGELOG.md: no version heading")


def main() -> None:
    versions = {"SKILL.md": skill_version(), "runner.py": runner_version(), "CHANGELOG.md": changelog_head()}
    body = SKILL.read_text(encoding="utf-8")
    mentions = set(re.findall(r"X-SimianX-Skill: ([0-9]+\.[0-9]+\.[0-9]+)", body)) | set(re.findall(r"version `([0-9]+\.[0-9]+\.[0-9]+)`", body))
    for v in mentions:
        versions[f"SKILL.md body ({v})"] = v
    if len(sys.argv) > 1:
        versions["tag"] = sys.argv[1].lstrip("v")
    distinct = sorted(set(versions.values()))
    for name, v in versions.items():
        print(f"{name:28} {v}")
    if len(distinct) != 1:
        sys.exit(f"versions differ: {distinct}")
    print(f"ok: {distinct[0]}")


if __name__ == "__main__":
    main()
