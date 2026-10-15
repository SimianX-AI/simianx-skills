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
  Quatre analystes IA sur n'importe quelle action américaine ou paire crypto, et un flux d'actualités déjà notées,
  dans Claude Code, Codex, Cursor et tout autre agent qui lit les skills.
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
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

L'agent place le skill là où il cherche ses skills, puis vous connecte : vous approuvez un lien dans votre navigateur, ou vous saisissez le code à 6 chiffres que nous vous envoyons par e-mail. Une nouvelle adresse obtient un compte sur-le-champ. Au final, l'agent a sa propre clé API dans `SIMIANX_API_KEY`, et jamais votre connexion au site.

Ou depuis un terminal :

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

La commande et le répertoire de chaque agent (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline et les autres) sont dans [INSTALL.md](INSTALL.md).

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
README.<locale>.md                this page in the 16 languages SimianX speaks
```

## Retours

- Depuis un agent : `POST /v1/feedback`.
- Depuis une personne : [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) pour le skill, [simianx.ai/agents](https://www.simianx.ai/agents) pour le produit.

Lisez [CONTRIBUTING.md](CONTRIBUTING.md) avant d'ouvrir une pull request, et [SECURITY.md](SECURITY.md) pour signaler une vulnérabilité.

## Licence

Tout le contenu de ce dépôt est sous licence MIT. L'utilisation de l'API SimianX est régie par les [Conditions d'utilisation](https://www.simianx.ai/legal/terms). Les analyses SimianX sont de l'information, pas des conseils en investissement.
