#!/bin/sh
# Install the SimianX skill for one or more AI agents (macOS / Linux).
#
#   sh scripts/install.sh --agent claude            # from a checkout
#   curl -fsSL https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main/scripts/install.sh | sh -s -- --agent auto
#
# Runs scripts/install.py when python3 exists (all flags, see `--help`). Without python3 it falls back to a plain
# copy that understands --agent, --scope, --source <dir>, --uninstall, --dry-run, --force, --yes.
set -eu
RAW=https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main
SKILL=simianx
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" 2>/dev/null && pwd) || HERE=.

if command -v python3 >/dev/null 2>&1; then
  if [ -f "$HERE/install.py" ]; then exec python3 "$HERE/install.py" "$@"; fi
  tmp=$(mktemp -d 2>/dev/null || mktemp -d -t simianx)
  if curl -fsSL "$RAW/scripts/install.py" -o "$tmp/install.py"; then exec python3 "$tmp/install.py" "$@"; fi
  echo "could not download install.py; using the plain copy" >&2
fi

# ---- pure-sh fallback -------------------------------------------------------------------------------------------
AGENT=auto SCOPE=user SOURCE= UNINSTALL= DRY= FORCE= YES=
while [ $# -gt 0 ]; do
  case "$1" in
    --agent) AGENT=$2; shift ;; --agent=*) AGENT=${1#*=} ;;
    --scope) SCOPE=$2; shift ;; --scope=*) SCOPE=${1#*=} ;;
    --source) SOURCE=$2; shift ;; --source=*) SOURCE=${1#*=} ;;
    --uninstall) UNINSTALL=1 ;; --dry-run) DRY=1 ;; --force) FORCE=1 ;; --yes|-y) YES=1 ;; --link) echo "--link needs python3; copying" >&2 ;;
    -h|--help) sed -n '2,9p' "$0"; exit 0 ;;
    *) echo "unknown flag $1" >&2; exit 2 ;;
  esac; shift
done

user_dir() { case "$1" in
  claude) echo .claude/skills ;; codex|zed|openhands) echo .agents/skills ;; cursor) echo .cursor/skills ;;
  copilot) echo .copilot/skills ;; gemini) echo .gemini/skills ;; windsurf) echo .codeium/windsurf/skills ;;
  cline) echo .cline/skills ;; roo) echo .roo/skills ;; kilo) echo .kilo/skills ;; opencode) echo .config/opencode/skills ;;
  amp) echo .config/agents/skills ;; kiro) echo .kiro/skills ;; factory) echo .factory/skills ;; goose) echo .config/goose/skills ;;
  *) return 1 ;; esac; }
proj_dir() { case "$1" in
  claude) echo .claude/skills ;; codex|cursor|copilot|gemini|amp|zed|openhands) echo .agents/skills ;; windsurf) echo .devin/skills ;;
  cline) echo .cline/skills ;; roo) echo .roo/skills ;; kilo) echo .kilo/skills ;; opencode) echo .opencode/skills ;;
  kiro) echo .kiro/skills ;; factory) echo .factory/skills ;; goose) echo .goose/skills ;; *) return 1 ;; esac; }
probe() { case "$1" in
  claude) echo .claude ;; codex) echo .codex ;; cursor) echo .cursor ;; copilot) echo .copilot ;; gemini) echo .gemini ;;
  windsurf) echo .codeium/windsurf ;; cline) echo .cline ;; roo) echo .roo ;; kilo) echo .kilo ;; opencode) echo .config/opencode ;;
  amp) echo .config/amp ;; zed) echo .config/zed ;; kiro) echo .kiro ;; factory) echo .factory ;; openhands) echo .openhands ;; goose) echo .config/goose ;; esac; }
ALL="claude codex cursor copilot gemini windsurf cline roo kilo opencode amp zed kiro factory openhands goose"

case "$AGENT" in
  all) AGENTS=$ALL ;;
  auto) AGENTS=; for a in $ALL; do [ -e "$HOME/$(probe $a)" ] && AGENTS="$AGENTS $a"; done
        [ -n "$AGENTS" ] || { echo "no agent config directory found; pass --agent <name>" >&2; exit 1; } ;;
  *) user_dir "$AGENT" >/dev/null || { echo "unknown agent $AGENT" >&2; exit 2; }; AGENTS=$AGENT ;;
esac

ours() { [ -f "$1/.installed.json" ] || grep -q "^name: $SKILL$" "$1/SKILL.md" 2>/dev/null; }

# source: --source dir, this checkout, else download
SRC=
if [ -n "$SOURCE" ]; then
  if [ -f "$SOURCE/SKILL.md" ]; then SRC=$SOURCE; elif [ -f "$SOURCE/skills/$SKILL/SKILL.md" ]; then SRC=$SOURCE/skills/$SKILL; else echo "$SOURCE: no SKILL.md" >&2; exit 1; fi
elif [ -f "$HERE/../skills/$SKILL/SKILL.md" ]; then SRC=$HERE/../skills/$SKILL
elif [ -z "$UNINSTALL" ]; then
  SRC=$(mktemp -d 2>/dev/null || mktemp -d -t simianx)/$SKILL; mkdir -p "$SRC/references" "$SRC/agents"
  for f in SKILL.md agents/openai.yaml references/autopilots.md references/billing.md references/data.md references/deep.md references/live.md references/news.md references/sectors.md; do
    curl -fsSL "$RAW/skills/$SKILL/$f" -o "$SRC/$f" || echo "  skip $f" >&2
  done
  [ -f "$SRC/SKILL.md" ] || curl -fsSL https://www.simianx.ai/SKILL.md -o "$SRC/SKILL.md" || { echo "cannot download the skill" >&2; exit 1; }
fi
VERSION=$(sed -n 's/^ *version: *"\{0,1\}\([0-9.]*\)"\{0,1\}.*/\1/p' "${SRC:-/dev/null}/SKILL.md" 2>/dev/null | head -1)
[ -z "$SRC" ] || echo "source: $SRC (version ${VERSION:-unknown})"

DONE=
for a in $AGENTS; do
  if [ "$SCOPE" = project ]; then T=$(pwd)/$(proj_dir $a)/$SKILL; else T=$HOME/$(user_dir $a)/$SKILL; fi
  case " $DONE " in *" $T "*) echo "$a: shares $T"; continue ;; esac; DONE="$DONE $T"
  if [ -n "$UNINSTALL" ]; then
    if [ ! -e "$T" ] && [ ! -L "$T" ]; then echo "$a: not installed"; continue; fi
    if ! ours "$T" && [ -z "$FORCE" ]; then echo "$a: refused, $T is not the SimianX skill (use --force)"; continue; fi
    [ -n "$DRY" ] && { echo "$a: would remove $T"; continue; }
    if [ -L "$T" ]; then rm "$T"; else rm -rf "$T"; fi; echo "$a: removed $T"; continue
  fi
  if [ -e "$T" ] || [ -L "$T" ]; then
    if ! ours "$T" && [ -z "$FORCE" ]; then echo "$a: refused, $T exists and is not the SimianX skill (use --force)"; continue; fi
  fi
  [ -n "$DRY" ] && { echo "$a: would copy $SRC -> $T"; continue; }
  if [ -z "$YES" ] && [ -t 0 ]; then printf '%s: install to %s? [y/N] ' "$a" "$T"; read -r ans; case "$ans" in y|Y|yes) ;; *) echo "skipped"; continue ;; esac; fi
  if [ -L "$T" ]; then rm "$T"; else rm -rf "$T"; fi
  mkdir -p "$(dirname "$T")" && cp -R "$SRC" "$T" && rm -f "$T/.installed.json"
  printf '{\n  "version": "%s",\n  "installed_at": "%s",\n  "source": "%s"\n}\n' "$VERSION" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$SRC" > "$T/.installed.json"
  echo "$a: installed ${VERSION:-?} at $T"
done
[ -n "$UNINSTALL" ] && exit 0
echo
echo "Next: create an API key at https://www.simianx.ai/#api (My Account -> API keys) and export it as SIMIANX_API_KEY."
echo "Give the key a daily points budget when the agent runs unattended; never put the key in a repository or a log."
echo "Verify: GET https://service.simianx.ai/v1/skill"
