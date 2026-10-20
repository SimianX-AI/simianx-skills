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
  Donnez à n'importe quel agent IA une équipe d'analyse complète. Avec SimianX AI, votre agent peut réunir un comité d'analyse de 8 agents sur n'importe quelle action américaine ou paire crypto puis l'interroger, obtenir une lecture en direct de quatre agents avec entrée, stop et objectif, et garder ouvert un flux d'actualités notées sur vos symboles. Un skill et un serveur MCP distant pour Claude Code, Codex, Cursor, Muse, Grok Bot, dots et tous les autres agents.
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

## Pourquoi donner SimianX à votre agent

Demandez à un agent livré à lui-même *« Faut-il acheter NVDA pour un swing trade ? »* : il cherche sur le web, résume des titres qui datent parfois de plusieurs jours et donne l'avis d'un seul modèle. Il n'a pas de graphique en direct, personne ne défend la thèse inverse, et tout s'arrête à la fin de la conversation.

Avec SimianX, le même agent :

| | Seul | Avec SimianX AI |
|---|---|---|
| Qui s'en charge | Un modèle | Un comité de 8 agents : quatre analystes, un chercheur haussier et un chercheur baissier, un responsable de la recherche, un responsable des risques |
| Ce qu'il lit | Des résultats de recherche web | Bougies en direct, documents réglementaires, transactions d'initiés, flux d'actualités ; données on-chain et de dérivés pour une crypto |
| Ce que vous obtenez | Un avis | Un verdict avec entrée, stop et objectif, et un rapport PDF |
| Ensuite | Repart de zéro | Soumet vos questions de suivi au même comité, ou lance un pilote automatique pour continuer à surveiller |

## Ce que vous pouvez demander

Une fois le skill installé, demandez avec vos propres mots :

- *« Réunis le comité SimianX sur NVDA pour un swing trade. »* Quatre analystes présentent leurs rapports, le haussier et le baissier croisent le fer, et le responsable des risques rend le verdict, le plan et un PDF.
- *« Demande au chercheur baissier ce qui prouverait que la thèse haussière est fausse. »* Les questions de suivi rejoignent la même analyse : la réponse s'appuie sur tout ce que le comité a déjà lu.
- *« Lance le comité sur SOL avec un horizon court. »* Pour une crypto, les analystes lisent aussi les flux on-chain et le marché des dérivés.
- *« Comment se présente BTC sur le graphique 15 minutes en ce moment ? »* Quatre agents en direct répondent, et l'agent de décision dit s'il faut acheter, vendre ou rester à l'écart, avec entrée, stop et objectif.
- *« Préviens-moi dès qu'une actu importante tombe sur TSLA ou ETH. »* Un flux d'actualités notées sur vos symboles, en direct, à mesure que chaque article est noté.
- *« Surveille AAPL en graphique 1 heure et gère une position fictive. »* Un pilote automatique relance les agents à chaque clôture de bougie et consigne chaque signal.
- *« Quelles dates PDUFA tombent dans les 30 prochains jours en biopharma ? »* La Veille sectorielle, à partir de sources primaires.
- *« Qu'est-ce qui a fortement bougé en crypto dans la dernière heure ? »* Le Pouls du Marché : mouvements brutaux, nouveaux plus hauts et plus bas, pics de volume et gaps.

Les comptes gratuits peuvent essayer le comité sur des symboles populaires comme NVDA, AAPL, TSLA, BTC et ETH.

## Ce que fait SimianX

Deux fonctions font l'essentiel du travail.

- **Analyse multi-agents en direct.** Indiquez une action ou une paire crypto et une unité de temps, et quatre agents l'analysent en même temps. L'agent indicateur lit le graphique. L'agent Intelligence suit l'actualité. L'agent fondamental lit les documents réglementaires et les transactions d'initiés ou, pour une crypto, les données on-chain et de dérivés. L'agent de décision pèse les trois avis et propose un trade avec entrée, stop et objectif. → [Analyse en direct](https://www.simianx.ai/l)
- **Un flux d'actualités notées.** Chaque article arrive étiqueté avec les symboles qu'il fait bouger, une note d'importance et une lecture haussière, baissière ou neutre. C'est le flux qui alimente le Pouls du Marché, où il côtoie les mouvements de prix brutaux, les nouveaux plus hauts et plus bas et les gaps. Votre agent peut le parcourir page par page ou garder un flux ouvert sur ses symboles. → [Pouls du Marché](https://www.simianx.ai/pulse)

Et quand vous en avez besoin :

- **Recherche approfondie.** Huit agents débattent d'une action ou d'une crypto et rendent un verdict, un plan de trading et un PDF. Votre agent peut ensuite poser des questions. → [Analyse approfondie](https://www.simianx.ai/c)
- **Veille sectorielle.** Calendriers de catalyseurs et événements tirés des sources primaires, en commençant par la biopharma. → [Veille sectorielle](https://www.simianx.ai/sectors)
- **Pilotes automatiques.** Les quatre mêmes agents en direct tournent selon un calendrier sur un seul symbole, gèrent une position fictive et tiennent un journal d'événements que votre agent peut suivre. → [Pilotes automatiques](https://www.simianx.ai/autopilots)
- **Le modèle de votre choix.** Choisissez le modèle de chaque agent, après avoir vu comment chacun a tradé. → [Classement des modèles](https://www.simianx.ai/crypto-leaderboard)

Marchés : plus de 13 000 actions et ETF américains, en bougies de `1m` à `1mo`, et plus de 4 000 paires crypto, spot et perpétuelles, de `1m` à `1D`. → [Analyse des actions](https://www.simianx.ai/c) · [Analyse des crypto-monnaies](https://www.simianx.ai/l)

## Installer en une phrase

Collez ceci dans votre agent :

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and sign me in.
```

L'agent place le skill là où il cherche ses skills, puis vous connecte : vous approuvez un lien dans votre navigateur, ou vous saisissez le code à 6 chiffres que nous vous envoyons par e-mail. Une nouvelle adresse obtient un compte sur-le-champ. Au final, l'agent a sa propre clé API dans `SIMIANX_API_KEY`, et jamais votre connexion au site.

Ou depuis un terminal :

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

La commande et le répertoire de chaque agent (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline et les autres) sont dans [INSTALL.md](INSTALL.md).

### Muse, Grok Bot, dots et les autres agents dotés de leur propre ordinateur

Les agents qui tournent sur leur propre ordinateur dans le cloud lisent la même phrase. Ils se branchent en MCP ou créent un connecteur à partir du [document OpenAPI](https://service.simianx.ai/v1/openapi.json), vous connectent, gardent la clé dans leur propre coffre d'identifiants et enregistrent SimianX comme skill. Les formulations exactes pour Muse, Grok Bot et dots se trouvent dans [INSTALL.md](INSTALL.md#agents-with-their-own-computer-muse-grok-bot-dots).

### Ou connectez-vous en MCP

Les agents IA qui parlent MCP peuvent utiliser SimianX comme outils, sans installer le skill. Ajoutez le serveur distant une fois avec votre clé :

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

La même chose pour Claude Desktop, Cursor, Codex, VS Code, Windsurf, Gemini CLI, Grok Bot et Muse se trouve dans [INSTALL.md](INSTALL.md#connect-over-mcp). Nom dans le registre : `io.github.SimianX-AI/simianx`.

## Premiers appels

| Quoi | Appel | Référence |
|---|---|---|
| Lancer une analyse en direct | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Les actualités de vos symboles | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| Les actualités dès leur sortie | `GET /v1/news/stream` (server-sent events, reprend après une coupure) | [news](skills/simianx/references/news.md) |
| Pouls du Marché | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Recherche approfondie | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Veille sectorielle | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Pilotes automatiques | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

URL de base `https://service.simianx.ai/v1`, en-tête `Authorization: Bearer $SIMIANX_API_KEY`. Les mêmes appels en scripts shell se trouvent dans [examples/curl](examples/curl).

## Plans

Free, Starter, Plus et Pro, détaillés dans la [tarification](https://www.simianx.ai/pricing). Les appels de l'agent utilisent les points de votre plan, aux mêmes tarifs que sur le site. Le flux d'actualités est en temps réel sur Plus et Pro ; en dessous de Plus, les actualités arrivent avec 30 minutes de retard. L'API répond en 16 langues. SimianX ne trade jamais sur un compte réel : les positions des pilotes automatiques sont fictives.

## Sécurité

- La clé reste dans `SIMIANX_API_KEY`. Le skill ne l'écrit jamais dans un dépôt, un journal ou un prompt.
- Un agent n'obtient jamais de session sur le site. Se connecter depuis un agent crée seulement une clé API pour cet agent, et nous vous prévenons par e-mail quand cela arrive.
- Les clés ont des portées, des budgets quotidiens et mensuels et une liste d'IP autorisées facultative. Donnez à chaque agent la clé la plus restreinte qui suffise à sa tâche.
- Révoquez une clé dans **Mon compte → Clés API** et elle cesse de fonctionner en moins d'une seconde.

## Versions

Le skill envoie sa version dans l'en-tête `X-SimianX-Skill`. Quand une version est retirée, l'API répond `426` avec l'URL à relire, et `GET /v1/skill` indique la version actuelle et la version minimale. Mettez à jour avec la commande de votre agent ou recollez la phrase ci-dessus. Le détail des changements est dans le [journal des modifications](CHANGELOG.md).

## Organisation du dépôt

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

## Retours

- Depuis un agent : `POST /v1/feedback`.
- Depuis une personne : [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) pour le skill, [simianx.ai/agents](https://www.simianx.ai/agents) pour le produit.

Lisez [CONTRIBUTING.md](CONTRIBUTING.md) avant d'ouvrir une pull request, et [SECURITY.md](SECURITY.md) pour signaler une vulnérabilité.

## Licence

Tout le contenu de ce dépôt est sous licence MIT. L'utilisation de l'API SimianX est régie par les [Conditions d'utilisation](https://www.simianx.ai/legal/terms). Les analyses SimianX sont de l'information, pas des conseils en investissement.
