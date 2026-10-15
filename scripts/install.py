#!/usr/bin/env python3
"""Install the SimianX skill into the skills directory of one or more AI agents.

    python3 scripts/install.py --agent claude                 # ~/.claude/skills/simianx
    python3 scripts/install.py --agent codex --scope project  # ./.agents/skills/simianx
    python3 scripts/install.py --agent auto                   # every agent whose config directory exists
    python3 scripts/install.py --agent all --dry-run          # show every target, change nothing
    python3 scripts/install.py --agent claude --uninstall

Standard library only; works on macOS, Linux and Windows. By default the skill is copied from the checkout this
script sits in; `--source <path|url>` takes another checkout, a skill folder, or a URL serving SKILL.md
(https://www.simianx.ai/SKILL.md). Run without a checkout (e.g. `curl ... | python3 -`) and the files are fetched
from GitHub main. Never touches SIMIANX_API_KEY or anything outside the target skill folder; refuses to overwrite a
folder that is not ours unless --force.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import shutil
import sys
import tempfile
import urllib.request
from datetime import datetime, timezone

SKILL = "simianx"
RAW = "https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main/skills/simianx/"
SITE_SKILL = "https://www.simianx.ai/SKILL.md"
FILES = ["SKILL.md", "agents/openai.yaml"] + [
    f"references/{n}.md" for n in ("auth", "autopilots", "billing", "data", "deep", "live", "news", "sectors")]
KEY_URL = "https://www.simianx.ai/#api"
WINDOWS = os.name == "nt"

# agent -> (user-scope dir, project-scope dir, detection dirs). Dirs are relative to $HOME (user) or cwd (project).
AGENTS = {
    "claude":    (".claude/skills",          ".claude/skills",   [".claude"]),
    "codex":     (".agents/skills",          ".agents/skills",   [".codex"]),
    "cursor":    (".cursor/skills",          ".agents/skills",   [".cursor"]),
    "copilot":   (".copilot/skills",         ".agents/skills",   [".copilot"]),
    "gemini":    (".gemini/skills",          ".agents/skills",   [".gemini"]),
    "windsurf":  (".codeium/windsurf/skills", ".devin/skills",   [".codeium/windsurf", ".config/devin"]),
    "cline":     (".cline/skills",           ".cline/skills",    [".cline"]),
    "roo":       (".roo/skills",             ".roo/skills",      [".roo"]),
    "kilo":      (".kilo/skills",            ".kilo/skills",     [".kilo"]),
    "opencode":  (".config/opencode/skills", ".opencode/skills", [".config/opencode"]),
    "amp":       (".config/agents/skills",   ".agents/skills",   [".config/amp"]),
    "zed":       (".agents/skills",          ".agents/skills",   [".config/zed", "Library/Application Support/Zed"]),
    "kiro":      (".kiro/skills",            ".kiro/skills",     [".kiro"]),
    "factory":   (".factory/skills",         ".factory/skills",  [".factory"]),
    "openhands": (".agents/skills",          ".agents/skills",   [".openhands"]),
    "goose":     (".config/goose/skills",    ".goose/skills",    [".config/goose"]),
}
CHOICES = list(AGENTS) + ["all", "auto"]


def home() -> pathlib.Path:
    return pathlib.Path(os.environ.get("USERPROFILE" if WINDOWS else "HOME") or pathlib.Path.home())


def log(msg: str) -> None:
    print(msg, flush=True)


def skill_version(skill_dir: pathlib.Path) -> str:
    try:
        head = (skill_dir / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
    except (OSError, IndexError):
        return "unknown"
    for line in head.splitlines():
        if line.strip().startswith("version:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return "unknown"


def is_ours(target: pathlib.Path) -> bool:
    """A folder we may replace: our marker, or a SKILL.md whose frontmatter names this skill."""
    if (target / ".installed.json").exists():
        return True
    try:
        head = (target / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
    except (OSError, IndexError):
        return False
    return any(line.strip() == f"name: {SKILL}" for line in head.splitlines())


def fetch(url: str, dest: pathlib.Path) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": "simianx-install"})
    try:
        with urllib.request.urlopen(req, timeout=30) as res:
            data = res.read()
    except Exception as exc:  # noqa: BLE001
        log(f"  skip {url}: {exc}")
        return False
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    return True


def resolve_source(arg: str | None, tmp: pathlib.Path) -> tuple[pathlib.Path, str]:
    """Return (local skill folder, source label)."""
    if arg and arg.startswith(("http://", "https://", "file://")):
        base = arg if arg.endswith("/") else arg.rsplit("/", 1)[0] + "/"
        dest = tmp / SKILL
        if arg.endswith("SKILL.md"):
            if not fetch(arg, dest / "SKILL.md"):
                sys.exit(f"cannot download {arg}")
            for name in FILES[1:]:
                fetch(base + name, dest / name)
        else:
            for name in FILES:
                fetch(base + name, dest / name)
            if not (dest / "SKILL.md").exists():
                sys.exit(f"no SKILL.md under {base}")
        return dest, arg
    if arg:
        p = pathlib.Path(arg).expanduser().resolve()
        for cand in (p, p / "skills" / SKILL):
            if (cand / "SKILL.md").exists():
                return cand, str(cand)
        sys.exit(f"{arg}: no SKILL.md found (expected a skill folder or a checkout)")
    here = pathlib.Path(__file__).resolve().parent.parent / "skills" / SKILL if "__file__" in globals() else None
    if here and (here / "SKILL.md").exists():
        return here, str(here)
    log(f"no local checkout; downloading from {RAW}")
    dest = tmp / SKILL
    for name in FILES:
        fetch(RAW + name, dest / name)
    if not (dest / "SKILL.md").exists():
        log(f"GitHub unreachable; falling back to {SITE_SKILL}")
        if not fetch(SITE_SKILL, dest / "SKILL.md"):
            sys.exit("cannot download the skill")
        return dest, SITE_SKILL
    return dest, RAW


def targets(agents: list[str], scope: str, project: pathlib.Path) -> list[tuple[str, pathlib.Path]]:
    out: list[tuple[str, pathlib.Path]] = []
    seen: set[pathlib.Path] = set()
    for a in agents:
        user_dir, proj_dir, _ = AGENTS[a]
        base = (home() / user_dir) if scope == "user" else (project / proj_dir)
        t = (base / SKILL).absolute()
        if t in seen:
            out.append((a, t))  # printed as "shared with"
            continue
        seen.add(t)
        out.append((a, t))
    return out


def detect() -> list[str]:
    h = home()
    found = [a for a, (_, _, probes) in AGENTS.items() if any((h / p).exists() for p in probes)]
    return found


def install_one(src: pathlib.Path, target: pathlib.Path, link: bool, force: bool, dry: bool, source: str, version: str) -> str:
    if target.exists() or target.is_symlink():
        if not is_ours(target) and not force:
            return f"refused: {target} exists and is not the SimianX skill (use --force)"
        if dry:
            return f"would replace {target}"
        if target.is_symlink() or target.is_file():
            target.unlink()
        else:
            shutil.rmtree(target)
    elif dry:
        return f"would {'link' if link and not WINDOWS else 'copy'} {src} -> {target}"
    target.parent.mkdir(parents=True, exist_ok=True)
    if link and not WINDOWS:
        os.symlink(src, target, target_is_directory=True)
        return f"linked {target} -> {src}"
    shutil.copytree(src, target, ignore=shutil.ignore_patterns("__pycache__", ".installed.json"))
    (target / ".installed.json").write_text(json.dumps({
        "version": version, "installed_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": source}, indent=2) + "\n", encoding="utf-8")
    return f"installed {version} at {target}"


def uninstall_one(target: pathlib.Path, force: bool, dry: bool) -> str:
    if not (target.exists() or target.is_symlink()):
        return f"not installed: {target}"
    if not is_ours(target) and not force:
        return f"refused: {target} is not the SimianX skill (use --force)"
    if dry:
        return f"would remove {target}"
    if target.is_symlink() or target.is_file():
        target.unlink()
    else:
        shutil.rmtree(target)
    return f"removed {target}"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--agent", choices=CHOICES, default="auto", help="which agent (default: auto = every agent whose config dir exists)")
    ap.add_argument("--scope", choices=["user", "project"], default="user", help="user = home directory, project = current directory")
    ap.add_argument("--link", action="store_true", help="symlink the source folder instead of copying (macOS/Linux)")
    ap.add_argument("--source", help="checkout, skill folder, or URL of SKILL.md (default: this checkout, else GitHub main)")
    ap.add_argument("--uninstall", action="store_true")
    ap.add_argument("--force", action="store_true", help="replace a folder that is not ours")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--yes", "-y", action="store_true", help="do not ask for confirmation")
    ap.add_argument("--project-dir", default=".", help=argparse.SUPPRESS)
    args = ap.parse_args()

    if args.agent == "all":
        agents = list(AGENTS)
    elif args.agent == "auto":
        agents = detect()
        if not agents:
            sys.exit("no agent config directory found in your home; pass --agent <name> (see --help)")
        log("detected: " + ", ".join(agents))
    else:
        agents = [args.agent]
    project = pathlib.Path(args.project_dir).resolve()
    plan = targets(agents, args.scope, project)

    if args.uninstall:
        done: set[pathlib.Path] = set()
        for a, t in plan:
            if t in done:
                continue
            done.add(t)
            log(f"{a:10} {uninstall_one(t, args.force, args.dry_run)}")
        return

    with tempfile.TemporaryDirectory(prefix="simianx-skill-") as tmp:
        src, source = resolve_source(args.source, pathlib.Path(tmp))
        version = skill_version(src)
        log(f"source: {source} (version {version})")
        if args.link and str(src).startswith(tmp):
            log("--link ignored: the source is a download, copying instead")
            args.link = False
        if not args.yes and not args.dry_run and sys.stdin.isatty():
            for a, t in plan:
                log(f"  {a:10} {t}")
            if input("install there? [y/N] ").strip().lower() not in ("y", "yes"):
                sys.exit("aborted")
        done = {}
        for a, t in plan:
            if t in done:
                log(f"{a:10} shares {t}")
                continue
            done[t] = install_one(src, t, args.link, args.force, args.dry_run, source, version)
            log(f"{a:10} {done[t]}")
    log("")
    log("Next: create an API key at " + KEY_URL + " (My Account -> API keys) and export it as SIMIANX_API_KEY.")
    log("Give the key a daily points budget when the agent runs unattended. The agent reads the key from the")
    log("environment only; never paste it into a repository, a prompt or a log. Verify: GET https://service.simianx.ai/v1/skill")


if __name__ == "__main__":
    main()
