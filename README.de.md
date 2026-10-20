<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI für KI-Agenten</h1>

<p align="center">
  Echtzeit-KI für Live-Trading. Vier Agenten analysieren jede US-Aktie und jedes Krypto-Paar live und liefern Einstieg, Stop und Ziel, dazu ein Echtzeit-Stream bewerteter News, Market-Pulse-Signale, Deep Research, Sector Watch und Autopilots. Ein Skill und ein Remote-MCP-Server für Claude Code, Codex, Cursor und jeden anderen KI-Agenten.
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <b>Deutsch</b> · <a href="README.tr.md">Türkçe</a>
</p>

---

## Was SimianX kann

Den Großteil der Arbeit erledigen zwei Funktionen.

- **Live-Analyse mit mehreren Agenten.** Wählen Sie eine Aktie oder ein Krypto-Paar und einen Zeitrahmen, und vier Agenten analysieren den Wert gleichzeitig. Der Indikator-Agent liest den Chart. Der Intelligenz-Agent verfolgt den Nachrichtenfluss. Der Fundamental-Agent liest Pflichtmitteilungen und Insidergeschäfte, bei einem Coin On-Chain- und Derivatedaten. Der Entscheidungs-Agent wägt die drei Einschätzungen ab und schlägt einen Trade mit Einstieg, Stop und Kursziel vor. → [Live-Analyse](https://www.simianx.ai/l)
- **Bewertete News als Stream.** Jeder Artikel kommt mit den Symbolen, die er bewegt, einer Relevanzstufe und einer Einordnung als bullisch, bärisch oder neutral. Derselbe Feed speist den Marktpuls, wo die Meldungen neben plötzlichen Kursbewegungen, neuen Hochs und Tiefs und Gaps stehen. Ihr Agent kann ihn Seite für Seite lesen oder für seine Symbole einen Stream offen halten. → [Marktpuls](https://www.simianx.ai/pulse)

Bei Bedarf außerdem:

- **Tiefenanalyse.** Acht Agenten debattieren über eine Aktie oder einen Coin und liefern ein Urteil, einen Handelsplan und ein PDF. Ihr Agent kann Rückfragen stellen. → [Tiefenanalyse](https://www.simianx.ai/c)
- **Sektor-Watch.** Katalysator-Kalender und Ereignisse aus Primärquellen, zuerst für Biopharma. → [Sektor-Watch](https://www.simianx.ai/sectors)
- **Autopiloten.** Dieselben vier Live-Agenten nach Zeitplan auf einem Symbol, mit einer Papierposition und einem Ereignisprotokoll, dem Ihr Agent folgen kann. → [Autopiloten](https://www.simianx.ai/autopilots)
- **Freie Modellwahl.** Wählen Sie das Modell hinter jedem Agenten und sehen Sie sich vorher an, wie jedes Modell bisher gehandelt hat. → [Modell-Rangliste](https://www.simianx.ai/crypto-leaderboard)

Märkte: über 13.000 US-Aktien und ETFs auf Kerzen von `1m` bis `1mo` und über 4.000 Krypto-Paare, Spot und Perpetual, von `1m` bis `1D`. → [Aktienanalyse](https://www.simianx.ai/c) · [Kryptoanalyse](https://www.simianx.ai/l)

## Installation in einem Satz

Schicken Sie Ihrem Agenten diesen Satz:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Er legt den Skill dort ab, wo er nach Skills sucht, und meldet Sie dann an: Sie geben einen Link im Browser frei oder tippen den 6-stelligen Code ein, den wir Ihnen per E-Mail schicken. Für eine neue Adresse wird sofort ein Konto angelegt. Am Ende hat der Agent einen eigenen API-Schlüssel in `SIMIANX_API_KEY`, aber nie Ihren Website-Login.

Lieber im Terminal:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

Befehl und Verzeichnis für jeden Agenten (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline und die übrigen) stehen in [INSTALL.md](INSTALL.md).

### Oder per MCP verbinden

KI-Agenten, die MCP sprechen, nutzen SimianX als Werkzeuge, ganz ohne den Skill zu installieren. Fügen Sie den Remote-Server einmal mit Ihrem Schlüssel hinzu:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

Dasselbe für Claude Desktop, Cursor, Codex, VS Code, Windsurf und Gemini CLI steht in [INSTALL.md](INSTALL.md#connect-over-mcp). Name in der Registry: `io.github.SimianX-AI/simianx`.

## Erste Aufrufe

| Was | Aufruf | Referenz |
|---|---|---|
| Live-Analyse, einmalig | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| News zu Ihren Symbolen | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| News, sobald sie erscheinen | `GET /v1/news/stream` (Server-Sent Events, fortsetzbar) | [news](skills/simianx/references/news.md) |
| Marktpuls | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Tiefenanalyse | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Sektor-Watch | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Autopiloten | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Basis-URL `https://service.simianx.ai/v1`, Header `Authorization: Bearer $SIMIANX_API_KEY`. Dieselben Aufrufe als Shell-Skripte liegen in [examples/curl](examples/curl).

## Pläne

Free, Starter, Plus und Pro, siehe [Preise](https://www.simianx.ai/pricing). Agenten-Aufrufe laufen über die Punkte Ihres Plans, zu denselben Tarifen wie auf der Website. Mit Plus und Pro kommt der News-Stream in Echtzeit, unterhalb von Plus laufen News 30 Minuten hinterher. Antworten gibt es in 16 Sprachen. SimianX handelt nie mit einem echten Konto, Autopiloten führen nur Papierpositionen.

## Sicherheit

- Der Schlüssel bleibt in `SIMIANX_API_KEY`. Der Skill schreibt ihn nie in ein Repository, ein Log oder einen Prompt.
- Ein Agent bekommt nie eine Website-Sitzung. Die Anmeldung über einen Agenten erzeugt nur einen API-Schlüssel für diesen Agenten, und wir schicken Ihnen dazu eine E-Mail.
- Schlüssel haben Berechtigungen, Tages- und Monatsbudgets und auf Wunsch eine Liste erlaubter IP-Adressen. Geben Sie jedem Agenten den kleinsten Schlüssel, der für seine Aufgabe reicht.
- Widerrufen Sie einen Schlüssel unter **Mein Konto → API-Schlüssel**, und er funktioniert innerhalb einer Sekunde nicht mehr.

## Versionen

Der Skill sendet seine Version im Header `X-SimianX-Skill`. Wird eine Version nicht mehr unterstützt, antwortet die API mit `426` und der URL, die Ihr Agent neu lesen soll, und `GET /v1/skill` zeigt die aktuelle und die Mindestversion. Aktualisieren Sie mit dem Befehl Ihres Agenten oder schicken Sie den Satz von oben noch einmal. Was sich geändert hat, steht im [Changelog](CHANGELOG.md).

## Aufbau des Repositorys

```
skills/simianx/SKILL.md           the skill (Agent Skills format)
skills/simianx/references/        live · news · data · deep · sectors · autopilots · billing
INSTALL.md                        agent-readable install guide (also at simianx.ai/INSTALL.md)
scripts/install.{sh,py,ps1}       installer for every agent; check_version.py · check_readmes.py
examples/curl · examples/runner   the first calls in curl; an always-on runner for autopilots
.claude-plugin · .agents/plugins · .cursor-plugin · plugin.json · gemini-extension.json
                                  manifests so marketplaces and plugin commands find the skill
server.json                       MCP Registry entry for the remote MCP server (service.simianx.ai/v1/mcp)
README.<locale>.md                this page in the 16 languages SimianX speaks
```

## Feedback

- Aus einem Agenten: `POST /v1/feedback`.
- Von Menschen: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) für den Skill, [simianx.ai/agents](https://www.simianx.ai/agents) für das Produkt.

Lesen Sie [CONTRIBUTING.md](CONTRIBUTING.md), bevor Sie einen Pull Request öffnen, und [SECURITY.md](SECURITY.md), wenn Sie eine Schwachstelle melden wollen.

## Lizenz

MIT für alles in diesem Repository. Für die Nutzung der SimianX-API gelten die [Nutzungsbedingungen](https://www.simianx.ai/legal/terms). Analysen von SimianX sind Informationen, keine Anlageberatung.
