<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI pour les agents IA</h1>

<p align="center">
  Un seul skill qui fait de Claude Code, Codex, Cursor, Copilot, Gemini CLI et de tout autre agent lisant des skills un client du desk de trading SimianX :
  autopilotes avec un journal d'événements de qualité exécution, recherche approfondie à 8 agents, analyse en direct, actualités classifiées et catalyseurs sectoriels.
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
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <b>Français</b> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## Ce que couvre SimianX

Tout ce qui suit est accessible via le skill et vit sur [simianx.ai](https://www.simianx.ai) ; les liens ouvrent la page produit derrière chaque fonctionnalité.

**Marchés**

- **Actions et ETF américains** — plus de 13 000 instruments cotés, avec résultats, dépôts réglementaires, séries financières et prise en compte des heures de marché. Unités de temps `1m 15m 1H 1D 1W 1mo`. → [Analyse des actions](https://www.simianx.ai/stocks)
- **Crypto** — plus de 1 500 coins et 4 000 paires sur OKX, Binance, Bybit et Coinbase : spot et swaps perpétuels USDT/USD (un symbole nu comme `BTC` renvoie au perpétuel). Unités de temps `1m 5m 15m 1H 4H 1D`. → [Analyse des crypto-monnaies](https://www.simianx.ai/l)

**Ce que font les agents**

- **Autopilotes** — les quatre agents live tournent selon un calendrier sur un symbole et, si vous le leur permettez, gèrent une position papier (entrées au marché, à cours limité et stop, renforcement progressif, stop-loss / take-profit, un filtre de timing). Chaque analyse, signal et changement de position atterrit dans un journal d'événements que vous lisez avec un curseur ; `signal.fired` et `position.changed` portent une expiration. Votre agent peut aussi trader ce portefeuille à la main. → [Pilotes automatiques](https://www.simianx.ai/autopilots)
- **Recherche approfondie** — un comité de 8 agents par exécution : quatre analystes (actions : fundamentals, market, news, timing · crypto : fundamentals, market, news, derivatives), un bull researcher (haussier) et un bear researcher (baissier), un research manager qui modère le débat et un risk manager qui rend le verdict et le plan. Horizons `short`, `swing`, `long` ; questions de suivi ; un rapport PDF. → [Analyse approfondie](https://www.simianx.ai/c)
- **Analyse en direct** — les quatre agents live, une seule fois : **indicator** (indicateur : tendance, momentum, structure sur le graphique), **intelligence** (renseignement : flux d'actualités et narratif), **fundamental** (fondamental : états financiers et événements, ou on-chain et dérivés pour une crypto) et **decision** (décision : la proposition de trade avec entrée, stop et objectif). → [Analyse en direct](https://www.simianx.ai/l)
- **Actualités classifiées** — chaque article est noté selon les symboles qu'il fait bouger, sa valeur (`low` / `medium` / `high`) et son sentiment ; en liste, par article, traduit en 16 langues, ou en flux en direct. → [Histoires](https://www.simianx.ai/stories)
- **Market Pulse** — chocs de prix sur des fenêtres de 1, 5 et 15 minutes, plus hauts et plus bas sur 24 heures / 30 jours / 52 semaines, variations journalières et gaps, pour la crypto et les actions, avec une sévérité de 1–4. → [Pouls du Marché](https://www.simianx.ai/pulse)
- **Sector Watch** — catalyseurs de source primaire pour un secteur : un calendrier (dates PDUFA, comités consultatifs, résultats d'essais), des événements avec sévérité 1–4 et direction (approbations, lettres de réponse complète, résultats topline, désignations, inspections, mises à jour d'étiquetage…), composants, actifs médicamenteux et suivis. Disponible aujourd'hui : **Biopharma · approbations FDA**, construit à partir des dépôts SEC, des publications de la FDA et du Federal Register, de ClinicalTrials.gov et d'openFDA. → [Veille sectorielle](https://www.simianx.ai/sectors)
- **Les modèles que vous choisissez** — trois paliers (`fast`, `standard`, `frontier`) et plus de 50 modèles de 7 fournisseurs qu'un forfait payant peut définir par agent ; un catalogue public avec les prix en points. → [Points & tarifs](https://www.simianx.ai/points)
- **Classement** — comment chaque modèle a réellement tradé, pour qu'un agent choisisse un modèle de décision sur des preuves. → [Classement des modèles IA crypto-monnaies](https://www.simianx.ai/crypto-leaderboard)

**Forfaits et langues** — forfaits Free, Starter, Plus et Pro avec des points mensuels, des limites de débit par forfait et un délai de 30 minutes sur les données en dessous de Plus ([tarification](https://www.simianx.ai/pricing)). L'API répond en 16 langues (`X-Language`). SimianX ne trade pas de comptes réels : les positions des autopilotes sont des positions papier que vous pouvez répliquer avec votre propre runner.

## Installer en une phrase

Collez ceci à votre agent. Il récupère le guide d'installation, place le skill là où votre agent lit les skills et vous demande une clé :

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Vous préférez une commande ? Les deux fonctionnent avec tout agent qui lit des skills :

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Dites ensuite **"Connecte-moi à SimianX"**. L'agent vous remet un lien à approuver dans votre navigateur, ou vous envoie un code à 6 chiffres par e-mail ; dans les deux cas, il reçoit une clé qui lui est propre, avec ses portées et son budget, et la stocke dans `SIMIANX_API_KEY`. Pas encore de compte ? Le code par e-mail en crée un. Vous pouvez aussi créer une clé à la main dans **Mon compte → Clés API** sur [simianx.ai](https://www.simianx.ai) et l'exporter :

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Installer pour votre agent

| Agent | Voie native | Où atterrit le skill |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` puis `/plugin install simianx@simianx` | plugin, ou `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` puis `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (ou `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (ou `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Tout autre agent | copiez `skills/simianx/` dans le répertoire que votre agent parcourt, ou lancez `scripts/install.sh --agent auto` | voir [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) indique le répertoire exact et les lignes shell pour chaque client ; `scripts/install.sh` (`install.py`, sous Windows : `install.ps1`) détecte les agents installés et copie ou lie le skill pour vous.

## Ce que votre agent peut faire

| Besoin | Appel | Référence |
|---|---|---|
| Lancer et suivre un autopilote sur une action ou une crypto | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Trader à la main le portefeuille papier de l'autopilote | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Exécuter un agent maintenant | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Recherche approfondie à 8 agents avec un verdict et un plan | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Les agents live, une seule fois | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Actualités classifiées (symboles, valeur, sentiment), en liste ou en flux | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Catalyseurs sectoriels : calendrier, événements, composants, suivis | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Bougies crypto, indicateurs, cotations, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Modèles configurables par agent, tarifs, votre compte | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Chaque événement du journal de l'autopilote porte un curseur et, pour tout ce sur quoi un agent pourrait agir (`signal.fired`, `position.changed`), une date d'expiration, de sorte qu'un runner n'agit jamais sur une information périmée. Lire les événements est gratuit ; vous payez les analyses, dans les points que votre forfait inclut déjà.

## Une première session

1. `GET https://service.simianx.ai/v1/skill` — public ; confirme que la version du skill détenue par votre agent est toujours acceptée.
2. `GET /v1/me` avec `Authorization: Bearer $SIMIANX_API_KEY` — forfait, points restants, limites.
3. `POST /v1/analysis/quote` — ce qu'un appel coûtera, avant de payer.
4. `POST /v1/autopilots` avec `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — puis interrogez le journal d'événements en long-polling à partir du curseur renvoyé dans la réponse.

La boucle complète, en `curl`, se trouve dans [examples/curl](examples/curl) ; un petit runner toujours actif qui exécute votre commande ou votre webhook à chaque changement de position se trouve dans [examples/runner](examples/runner).

## Des points, pas des crédits

- Tout est facturé en **points** prélevés sur l'abonnement du compte. Pas de recharge, pas de paiement à l'appel.
- Les endpoints IA sont facturés selon les modèles réellement utilisés ; `GET /v1/pricing` publie le coût habituel par palier (`fast`, `standard`, `frontier`) et `GET /v1/models` le prix de chaque modèle qu'un agent peut choisir.
- Les endpoints de données sont facturés à la requête (une fraction de point) ; le journal d'événements, `/v1/me`, `/v1/skill`, `/v1/pricing` et `/v1/models` ne coûtent rien.
- `402` signifie que les points ou le budget d'une clé sont épuisés et indique la marche à suivre (`renew_now`, `change_plan`, `subscribe`) ; `429` est une limite de débit et porte `Retry-After`. Rien d'autre n'est jamais un problème de paiement.

## Sécurité

- La clé vit dans la variable d'environnement `SIMIANX_API_KEY`. Le skill ne demande jamais à un agent de l'écrire dans un dépôt, un journal ou un prompt.
- Un agent n'obtient jamais de session sur le site web. Se connecter depuis un agent (lien dans le navigateur ou code par e-mail) ne fait jamais que créer une clé API pour cet agent, annoncée par e-mail et listée dans votre activité de sécurité ; le site web, la facturation et les paramètres de sécurité restent entre vos mains.
- Les clés portent des scopes (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), des budgets de points quotidiens et mensuels, un plafond par appel et une liste d'adresses IP autorisées facultative. Donnez à un agent la plus petite clé qui suffit à sa tâche.
- Révoquez n'importe quelle clé dans **Mon compte → Clés API** ; une clé révoquée est refusée en moins d'une seconde. Chaque appel est journalisé sous votre compte avec son coût.
- Le skill ne lit que votre propre compte : vos autopilotes, vos exécutions, vos clés. Il ne trade jamais un compte réel ; les positions des autopilotes sont des positions papier.

## Versions et mises à jour

Le skill annonce sa version dans l'en-tête `X-SimianX-Skill`. Lorsque l'API n'accepte plus une version, elle répond `426` avec l'URL à relire, et `GET /v1/skill` affiche toujours la version courante et la version minimale ainsi que le [changelog](CHANGELOG.md). Mettez à jour avec la commande propre à votre agent (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) ou relancez la phrase unique ci-dessus.

## Organisation du dépôt

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

## Retours et support

- Depuis un agent : `POST /v1/feedback` (lu par l'équipe ; tout texte abusif est refusé et jamais stocké).
- Depuis une personne : [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) pour le skill, [simianx.ai/agents](https://www.simianx.ai/agents) pour le produit.

Consultez [CONTRIBUTING.md](CONTRIBUTING.md) avant d'ouvrir une pull request et [SECURITY.md](SECURITY.md) pour signaler une vulnérabilité.

## Licence

MIT pour tout le contenu de ce dépôt. L'utilisation de l'API SimianX est régie par les [Conditions d'utilisation](https://www.simianx.ai/legal/terms). Les analyses SimianX sont de l'information, pas des conseils en investissement ; les positions des autopilotes sont des positions papier.
