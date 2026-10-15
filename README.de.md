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
  Ein einziger Skill, der Claude Code, Codex, Cursor, Copilot, Gemini CLI und jeden anderen Agenten, der Skills liest, zu einem Client des SimianX-Trading-Desks macht:
  Autopiloten mit einem Ereignisprotokoll in Ausführungsqualität, Deep Research mit 8 Agenten, Live-Analyse, klassifizierte Nachrichten und Sektor-Katalysatoren.
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

## Was SimianX abdeckt

Alles Folgende ist über den Skill erreichbar und lebt auf [simianx.ai](https://www.simianx.ai); die Links öffnen die Produktseite hinter jeder Funktion.

**Märkte**

- **US-Aktien und ETFs** — über 13.000 gelistete Instrumente, mit Quartalszahlen, Einreichungen, Finanzreihen und Kenntnis der Handelszeiten. Zeitrahmen `1m 15m 1H 1D 1W 1mo`. → [Aktienanalyse](https://www.simianx.ai/stocks)
- **Krypto** — über 1.500 Coins und 4.000 Paare auf OKX, Binance, Bybit und Coinbase: Spot und USDT/USD-Perpetual-Swaps (ein bloßes Symbol wie `BTC` löst zum Perpetual auf). Zeitrahmen `1m 5m 15m 1H 4H 1D`. → [Kryptoanalyse](https://www.simianx.ai/l)

**Was die Agenten tun**

- **Autopiloten** — die vier Live-Agenten laufen nach Zeitplan auf einem Symbol und verwalten, wenn Sie es zulassen, eine Paper-Position (Market-, Limit- und Stop-Einstiege, Skalierung, Stop-Loss / Take-Profit, ein Timing-Gate). Jede Analyse, jedes Signal und jede Positionsänderung landet in einem Ereignisprotokoll, das Sie mit einem Cursor lesen; `signal.fired` und `position.changed` tragen ein Ablaufdatum. Ihr Agent kann dieses Buch auch von Hand handeln. → [Autopiloten](https://www.simianx.ai/autopilots)
- **Deep Research** — ein Komitee aus 8 Agenten pro Lauf: vier Analysten (Aktien: fundamentals, market, news, timing · Krypto: fundamentals, market, news, derivatives), ein bull researcher (Bulle) und ein bear researcher (Bär), ein research manager, der die Debatte moderiert, und ein risk manager, der Urteil und Plan ausgibt. Horizonte `short`, `swing`, `long`; Nachfragen; ein PDF-Bericht. → [Deep-Analyse](https://www.simianx.ai/c)
- **Live-Analyse** — die vier Live-Agenten, einmalig: **indicator** (Indikator: Trend, Momentum, Struktur im Chart), **intelligence** (Nachrichtenfluss und Narrativ), **fundamental** (Fundamentaldaten: Finanzen und Ereignisse, oder On-Chain und Derivate bei einem Coin) und **decision** (Entscheidung: der Trade-Vorschlag mit Einstieg, Stop und Ziel). → [Live-Analyse](https://www.simianx.ai/l)
- **Klassifizierte Nachrichten** — jeder Artikel wird nach den Symbolen bewertet, die er bewegt, nach seinem Wert (`low` / `medium` / `high`) und seiner Stimmung; als Liste, pro Artikel, übersetzt in 16 Sprachen, oder als Live-Stream. → [Geschichten](https://www.simianx.ai/stories)
- **Market Pulse** — Preisschocks in 1-, 5- und 15-Minuten-Fenstern, 24-Stunden- / 30-Tage- / 52-Wochen-Hochs und -Tiefs, Tagesbewegungen und Gaps, für Krypto und Aktien, mit einer Schwere von 1–4. → [Marktpuls](https://www.simianx.ai/pulse)
- **Sector Watch** — Katalysatoren aus Primärquellen für einen Sektor: ein Kalender (PDUFA-Termine, Beratungsausschüsse, Studienergebnisse), Ereignisse mit Schwere 1–4 und Richtung (Zulassungen, Complete Response Letters, Topline-Ergebnisse, Designationen, Inspektionen, Label-Updates…), Bestandteile, Wirkstoff-Assets und Follows. Heute live: **Biopharma · FDA-Zulassungen**, aufgebaut aus SEC-Einreichungen, Veröffentlichungen von FDA und Federal Register, ClinicalTrials.gov und openFDA. → [Sektor-Watch](https://www.simianx.ai/sectors)
- **Modelle Ihrer Wahl** — drei Stufen (`fast`, `standard`, `frontier`) und über 50 Modelle von 7 Anbietern, die ein bezahlter Tarif pro Agent festlegen kann; ein öffentlicher Katalog mit Preisen in Punkten. → [Punkte & Tarife](https://www.simianx.ai/points)
- **Rangliste** — wie jedes Modell tatsächlich gehandelt hat, damit ein Agent ein Entscheidungsmodell auf Basis von Belegen wählen kann. → [Krypto-KI-Modell-Rangliste](https://www.simianx.ai/crypto-leaderboard)

**Tarife und Sprachen** — die Tarife Free, Starter, Plus und Pro mit monatlichen Punkten, Rate-Limits pro Tarif und einer Datenverzögerung von 30 Minuten unterhalb von Plus ([Preise](https://www.simianx.ai/pricing)). Die API antwortet in 16 Sprachen (`X-Language`). SimianX handelt keine echten Konten: Autopilot-Positionen sind Paper-Positionen, die Sie mit Ihrem eigenen Runner spiegeln können.

## Installation in einem Satz

Fügen Sie das in Ihren Agenten ein. Er holt die Installationsanleitung, legt den Skill dort ab, wo Ihr Agent Skills liest, und fragt Sie nach einem Schlüssel:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Lieber ein Befehl? Beide funktionieren mit jedem Agenten, der Skills liest:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Erstellen Sie dann einen Schlüssel unter **Mein Konto → API-Schlüssel** auf [simianx.ai](https://www.simianx.ai) und exportieren Sie ihn:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Installation für Ihren Agenten

| Agent | Nativer Weg | Wo der Skill landet |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` dann `/plugin install simianx@simianx` | Plugin, oder `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` dann `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (oder `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (oder `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Alles andere | `skills/simianx/` in das Verzeichnis kopieren, das Ihr Agent durchsucht, oder `scripts/install.sh --agent auto` ausführen | siehe [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) nennt das genaue Verzeichnis und die Shell-Zeilen für jeden Client; `scripts/install.sh` (`install.py`, unter Windows: `install.ps1`) erkennt installierte Agenten und kopiert oder verlinkt den Skill für Sie.

## Was Ihr Agent tun kann

| Bedarf | Aufruf | Referenz |
|---|---|---|
| Einen Autopiloten auf einer Aktie oder einem Coin starten und verfolgen | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Das Paper-Buch des Autopiloten von Hand handeln | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Einen Agenten jetzt ausführen | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Deep Research mit 8 Agenten, mit Urteil und Plan | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Die Live-Agenten, einmalig | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Klassifizierte Nachrichten (Symbole, Wert, Stimmung), als Liste oder Stream | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Sektor-Katalysatoren: Kalender, Ereignisse, Bestandteile, Follows | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Krypto-Kerzen, Indikatoren, Kurse, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Modelle, die Sie pro Agent setzen können, Preise, Ihr Konto | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Jedes Ereignis im Autopilot-Protokoll trägt einen Cursor und, für alles, worauf ein Agent reagieren könnte (`signal.fired`, `position.changed`), einen Ablaufstempel, sodass ein Runner nie auf veraltete Informationen reagiert. Ereignisse zu lesen ist kostenlos; Sie zahlen für die Analysen, in den Punkten, die Ihr Tarif ohnehin enthält.

## Eine erste Sitzung

1. `GET https://service.simianx.ai/v1/skill` — öffentlich; bestätigt, dass die Skill-Version Ihres Agenten noch akzeptiert wird.
2. `GET /v1/me` mit `Authorization: Bearer $SIMIANX_API_KEY` — Tarif, verbleibende Punkte, Limits.
3. `POST /v1/analysis/quote` — was ein Aufruf kostet, bevor Sie zahlen.
4. `POST /v1/autopilots` mit `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — dann das Ereignisprotokoll per Long-Polling ab dem Cursor abfragen, den die Antwort zurückgibt.

Die vollständige Schleife als `curl` steht in [examples/curl](examples/curl); ein kleiner, dauerhaft laufender Runner, der bei jeder Positionsänderung Ihren Befehl oder Webhook ausführt, steht in [examples/runner](examples/runner).

## Punkte, keine Credits

- Alles wird in **Punkten** aus dem Abonnement des Kontos abgerechnet. Es gibt keine Aufladungen und keine Bezahlung pro Aufruf.
- KI-Endpunkte werden nach den tatsächlich verwendeten Modellen abgerechnet; `GET /v1/pricing` veröffentlicht die üblichen Kosten je Stufe (`fast`, `standard`, `frontier`) und `GET /v1/models` den Preis jedes Modells, das ein Agent wählen darf.
- Daten-Endpunkte werden pro Anfrage berechnet (ein Bruchteil eines Punkts); das Ereignisprotokoll, `/v1/me`, `/v1/skill`, `/v1/pricing` und `/v1/models` kosten nichts.
- `402` bedeutet, dass Punkte oder das Budget eines Schlüssels aufgebraucht sind, und nennt den Ausweg (`renew_now`, `change_plan`, `subscribe`); `429` ist ein Rate-Limit und trägt `Retry-After`. Nichts anderes ist jemals ein Zahlungsproblem.

## Sicherheit

- Der Schlüssel lebt in der Umgebungsvariable `SIMIANX_API_KEY`. Der Skill fordert einen Agenten nie auf, ihn in ein Repository, ein Log oder einen Prompt zu schreiben.
- Schlüssel tragen Scopes (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), tägliche und monatliche Punktebudgets, eine Obergrenze pro Aufruf und eine optionale IP-Allowlist. Geben Sie einem Agenten den kleinsten Schlüssel, der seine Aufgabe erfüllt.
- Widerrufen Sie jeden Schlüssel unter **Mein Konto → API-Schlüssel**; ein widerrufener Schlüssel wird innerhalb einer Sekunde abgelehnt. Jeder Aufruf wird unter Ihrem Konto mit seinen Kosten protokolliert.
- Der Skill liest nur Ihr eigenes Konto: Ihre Autopiloten, Ihre Läufe, Ihre Schlüssel. Er handelt nie mit einem echten Konto; Autopilot-Positionen sind Paper-Positionen.

## Versionen und Updates

Der Skill meldet seine Version im Header `X-SimianX-Skill`. Akzeptiert die API eine Version nicht mehr, antwortet sie mit `426` und der URL, die neu zu lesen ist, und `GET /v1/skill` zeigt stets die aktuelle und die minimale Version sowie das [Changelog](CHANGELOG.md). Aktualisieren Sie mit dem Befehl Ihres Agenten (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) oder führen Sie den einen Satz von oben erneut aus.

## Aufbau des Repositorys

```
skills/simianx/SKILL.md           the skill (Agent Skills format)
skills/simianx/references/        autopilots · deep · live · news · sectors · data · billing
INSTALL.md                        agent-readable install guide (also served at simianx.ai/INSTALL.md)
scripts/install.{sh,py,ps1}       installer for every agent; check_version.py · check_readmes.py
examples/curl · examples/runner   a first session in curl; the always-on runner
.claude-plugin · .agents/plugins · .cursor-plugin · plugin.json · gemini-extension.json
                                  manifests so marketplaces and plugin commands find the skill
README.<locale>.md                this page in the 16 languages SimianX speaks
```

## Feedback und Support

- Aus einem Agenten: `POST /v1/feedback` (wird vom Team gelesen; beleidigender Text wird abgelehnt und nie gespeichert).
- Von einer Person: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) für den Skill, [simianx.ai/agents](https://www.simianx.ai/agents) für das Produkt.

Lesen Sie [CONTRIBUTING.md](CONTRIBUTING.md), bevor Sie einen Pull Request eröffnen, und [SECURITY.md](SECURITY.md), um eine Schwachstelle zu melden.

## Lizenz

MIT für alles in diesem Repository. Die Nutzung der SimianX-API unterliegt den [Nutzungsbedingungen](https://www.simianx.ai/legal/terms). SimianX-Analysen sind Informationen, keine Anlageberatung; Autopilot-Positionen sind Paper-Positionen.
