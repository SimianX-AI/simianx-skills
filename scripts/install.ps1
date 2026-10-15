<#
.SYNOPSIS
Install the SimianX skill for one or more AI agents on Windows.

.EXAMPLE
powershell -ExecutionPolicy Bypass -File scripts\install.ps1 -Agent claude
irm https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main/scripts/install.ps1 | iex   # then: Install-SimianXSkill -Agent auto

Runs scripts/install.py when a Python 3 is on PATH (all flags). Without Python it copies the files itself:
-Agent, -Scope user|project, -Source <dir>, -Uninstall, -DryRun, -Force, -Yes.
#>
param(
  [ValidateSet("claude","codex","cursor","copilot","gemini","windsurf","cline","roo","kilo","opencode","amp","zed","kiro","factory","openhands","goose","all","auto")]
  [string]$Agent = "auto",
  [ValidateSet("user","project")] [string]$Scope = "user",
  [string]$Source = "",
  [switch]$Uninstall, [switch]$DryRun, [switch]$Force, [switch]$Yes, [switch]$Link
)
$ErrorActionPreference = "Stop"
$Raw = "https://raw.githubusercontent.com/SimianX-AI/simianx-skills/main"
$Skill = "simianx"
$Here = if ($PSScriptRoot) { $PSScriptRoot } else { "" }

$py = Get-Command python3, python -ErrorAction SilentlyContinue | Where-Object { & $_.Source -c "import sys; sys.exit(0 if sys.version_info >= (3, 8) else 1)" 2>$null; $LASTEXITCODE -eq 0 } | Select-Object -First 1
if ($py) {
  $script = Join-Path $Here "install.py"
  if (-not (Test-Path $script)) {
    $script = Join-Path ([IO.Path]::GetTempPath()) "simianx-install.py"
    Invoke-WebRequest -UseBasicParsing "$Raw/scripts/install.py" -OutFile $script
  }
  $argv = @("--agent", $Agent, "--scope", $Scope)
  if ($Source) { $argv += @("--source", $Source) }
  foreach ($f in @(@($Uninstall, "--uninstall"), @($DryRun, "--dry-run"), @($Force, "--force"), @($Yes, "--yes"), @($Link, "--link"))) { if ($f[0]) { $argv += $f[1] } }
  & $py.Source $script @argv
  exit $LASTEXITCODE
}

# ---- pure PowerShell fallback -----------------------------------------------------------------------------------
$Home_ = $env:USERPROFILE
$UserDir = @{ claude=".claude\skills"; codex=".agents\skills"; cursor=".cursor\skills"; copilot=".copilot\skills"; gemini=".gemini\skills";
  windsurf=".codeium\windsurf\skills"; cline=".cline\skills"; roo=".roo\skills"; kilo=".kilo\skills"; opencode=".config\opencode\skills";
  amp=".config\agents\skills"; zed=".agents\skills"; kiro=".kiro\skills"; factory=".factory\skills"; openhands=".agents\skills"; goose=".config\goose\skills" }
$ProjDir = @{ claude=".claude\skills"; codex=".agents\skills"; cursor=".agents\skills"; copilot=".agents\skills"; gemini=".agents\skills";
  windsurf=".devin\skills"; cline=".cline\skills"; roo=".roo\skills"; kilo=".kilo\skills"; opencode=".opencode\skills"; amp=".agents\skills";
  zed=".agents\skills"; kiro=".kiro\skills"; factory=".factory\skills"; openhands=".agents\skills"; goose=".goose\skills" }
$Probe = @{ claude=".claude"; codex=".codex"; cursor=".cursor"; copilot=".copilot"; gemini=".gemini"; windsurf=".codeium\windsurf"; cline=".cline";
  roo=".roo"; kilo=".kilo"; opencode=".config\opencode"; amp=".config\amp"; zed="AppData\Roaming\Zed"; kiro=".kiro"; factory=".factory"; openhands=".openhands"; goose=".config\goose" }
$All = @("claude","codex","cursor","copilot","gemini","windsurf","cline","roo","kilo","opencode","amp","zed","kiro","factory","openhands","goose")
$Files = @("SKILL.md","agents/openai.yaml","references/autopilots.md","references/billing.md","references/data.md","references/deep.md","references/live.md","references/news.md","references/sectors.md")

$agents = switch ($Agent) {
  "all"  { $All }
  "auto" { $found = $All | Where-Object { Test-Path (Join-Path $Home_ $Probe[$_]) }; if (-not $found) { throw "no agent config directory found; pass -Agent <name>" }; Write-Host "detected: $($found -join ', ')"; $found }
  default { @($Agent) }
}

function Test-Ours($dir) {
  if (Test-Path (Join-Path $dir ".installed.json")) { return $true }
  $f = Join-Path $dir "SKILL.md"; if (-not (Test-Path $f)) { return $false }
  return (Get-Content $f -First 12) -contains "name: $Skill"
}

$src = $null
if (-not $Uninstall) {
  if ($Source) {
    if (Test-Path (Join-Path $Source "SKILL.md")) { $src = $Source } elseif (Test-Path (Join-Path $Source "skills\$Skill\SKILL.md")) { $src = Join-Path $Source "skills\$Skill" } else { throw "$Source: no SKILL.md" }
  } elseif ($Here -and (Test-Path (Join-Path $Here "..\skills\$Skill\SKILL.md"))) { $src = Resolve-Path (Join-Path $Here "..\skills\$Skill")
  } else {
    $src = Join-Path ([IO.Path]::GetTempPath()) "simianx-skill\$Skill"
    foreach ($f in $Files) { $dest = Join-Path $src $f; New-Item -ItemType Directory -Force (Split-Path $dest) | Out-Null
      try { Invoke-WebRequest -UseBasicParsing "$Raw/skills/$Skill/$f" -OutFile $dest } catch { Write-Host "  skip $f" } }
    if (-not (Test-Path (Join-Path $src "SKILL.md"))) { Invoke-WebRequest -UseBasicParsing "https://www.simianx.ai/SKILL.md" -OutFile (Join-Path $src "SKILL.md") }
  }
  $version = (Select-String -Path (Join-Path $src "SKILL.md") -Pattern '^\s*version:\s*"?([0-9.]+)' | Select-Object -First 1).Matches[0].Groups[1].Value
  Write-Host "source: $src (version $version)"
}

$done = @{}
foreach ($a in $agents) {
  $base = if ($Scope -eq "project") { Join-Path (Get-Location) $ProjDir[$a] } else { Join-Path $Home_ $UserDir[$a] }
  $t = Join-Path $base $Skill
  if ($done.ContainsKey($t)) { Write-Host "$a`: shares $t"; continue }; $done[$t] = $true
  if ($Uninstall) {
    if (-not (Test-Path $t)) { Write-Host "$a`: not installed"; continue }
    if (-not (Test-Ours $t) -and -not $Force) { Write-Host "$a`: refused, $t is not the SimianX skill (use -Force)"; continue }
    if ($DryRun) { Write-Host "$a`: would remove $t"; continue }
    Remove-Item -Recurse -Force $t; Write-Host "$a`: removed $t"; continue
  }
  if ((Test-Path $t) -and -not (Test-Ours $t) -and -not $Force) { Write-Host "$a`: refused, $t exists and is not the SimianX skill (use -Force)"; continue }
  if ($DryRun) { Write-Host "$a`: would copy $src -> $t"; continue }
  if (-not $Yes -and [Environment]::UserInteractive) { if ((Read-Host "$a`: install to $t? [y/N]") -notmatch '^y') { Write-Host "skipped"; continue } }
  if (Test-Path $t) { Remove-Item -Recurse -Force $t }
  New-Item -ItemType Directory -Force $base | Out-Null
  Copy-Item -Recurse $src $t
  Remove-Item -Force (Join-Path $t ".installed.json") -ErrorAction SilentlyContinue
  @{ version = $version; installed_at = (Get-Date).ToUniversalTime().ToString("yyyy-MM-ddTHH:mm:ssZ"); source = "$src" } | ConvertTo-Json | Set-Content (Join-Path $t ".installed.json")
  Write-Host "$a`: installed $version at $t"
}
if ($Uninstall) { exit 0 }
Write-Host ""
Write-Host "Next: create an API key at https://www.simianx.ai/#api (My Account -> API keys) and set it as SIMIANX_API_KEY."
Write-Host "Give the key a daily points budget when the agent runs unattended; never put the key in a repository or a log."
Write-Host "Verify: GET https://service.simianx.ai/v1/skill"
