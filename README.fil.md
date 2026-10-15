<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI para sa mga AI agent</h1>

<p align="center">
  Isang skill na ginagawang client ng SimianX trading desk ang Claude Code, Codex, Cursor, Copilot, Gemini CLI at lahat ng iba pang agent na nagbabasa ng skills:
  mga autopilot na may execution-grade na event log, 8-agent na deep research, live analysis, classified na balita at mga sector catalyst.
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
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <b>Filipino</b> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## Ano ang saklaw ng SimianX

Lahat ng nasa ibaba ay maaabot sa pamamagitan ng skill at nasa [simianx.ai](https://www.simianx.ai); binubuksan ng mga link ang product page sa likod ng bawat kakayahan.

**Mga merkado**

- **Mga stock at ETF ng US** — 13,000+ nakalistang instrumento, may earnings, mga filing, mga serye ng pinansyal na datos at kamalayan sa oras ng merkado. Mga timeframe `1m 15m 1H 1D 1W 1mo`. → [Pagsusuri ng Stock](https://www.simianx.ai/c)
- **Crypto** — 1,500+ coin at 4,000+ pair sa OKX, Binance, Bybit at Coinbase: spot at USDT/USD perpetual swap (ang simbolong walang kasunod gaya ng `BTC` ay tumutukoy sa perpetual). Mga timeframe `1m 5m 15m 1H 4H 1D`. → [Pagsusuri ng Crypto](https://www.simianx.ai/l)

**Ano ang ginagawa ng mga agent**

- **Mga autopilot** — tumatakbo ang apat na live agent ayon sa iskedyul sa isang simbolo at, kung papayagan mo, namamahala ng paper position (market, limit at stop na entry, scaling, stop-loss / take-profit, isang timing gate). Bawat analysis, signal at pagbabago ng posisyon ay napupunta sa isang event log na binabasa mo gamit ang cursor; may expiry ang `signal.fired` at `position.changed`. Maaari ding i-trade nang mano-mano ng iyong agent ang book na iyon. → [Awtomatikong piloto](https://www.simianx.ai/autopilots)
- **Deep research** — isang komite ng 8 agent bawat run: apat na analyst (mga stock: fundamentals, market, news, timing · crypto: fundamentals, market, news, derivatives), isang bull researcher at isang bear researcher, isang research manager na nagpapatakbo ng debate at isang risk manager na naglalabas ng verdict at plano. Mga horizon `short`, `swing`, `long`; mga follow-up na tanong; isang PDF report. → [Deep analysis](https://www.simianx.ai/c)
- **Live analysis** — ang apat na live agent, isang beses: **indicator** (trend, momentum, istruktura sa chart), **intelligence** (daloy ng balita at naratibo), **fundamental** (mga pinansyal na datos at event, o on-chain at derivatives para sa coin) at **decision** (ang trade proposal na may entry, stop at target). → [Live analysis](https://www.simianx.ai/l)
- **Classified na balita** — bawat artikulo ay binibigyan ng score para sa mga simbolong ginagalaw nito, sa value nito (`low` / `medium` / `high`) at sa sentiment nito; bilang listahan, bawat artikulo, isinalin sa 16 na wika, o bilang live stream. → [Mga Kwento](https://www.simianx.ai/stories)
- **Market Pulse** — mga biglaang galaw ng presyo sa 1-minuto, 5-minuto at 15-minutong window, 24-oras / 30-araw / 52-linggong high at low, mga galaw sa loob ng araw at mga gap, para sa crypto at mga stock, may severity 1–4. → [Pulso ng Merkado](https://www.simianx.ai/pulse)
- **Sector Watch** — mga catalyst mula sa pangunahing pinagmulan para sa isang sektor: kalendaryo (mga petsa ng PDUFA, mga advisory committee, mga resulta ng trial), mga event na may severity 1–4 at direksyon (mga approval, complete response letter, topline result, designation, inspeksyon, pagbabago ng label…), mga constituent, mga drug asset at mga follow. Live ngayon: **Biopharma · FDA approvals**, binuo mula sa mga filing sa SEC, mga release ng FDA at Federal Register, ClinicalTrials.gov at openFDA. → [Sector Watch](https://www.simianx.ai/sectors)
- **Mga model na pipiliin mo** — tatlong tier (`fast`, `standard`, `frontier`) at 50+ model mula sa 7 provider na maaaring itakda ng bayad na plan bawat agent; isang pampublikong katalogo na may mga presyo sa puntos. → [Puntos at Mga Rate](https://www.simianx.ai/points)
- **Leaderboard** — kung paano talaga nag-trade ang bawat model, para makapili ang agent ng decision model batay sa ebidensya. → [Leaderboard ng Crypto AI Model](https://www.simianx.ai/crypto-leaderboard)

**Mga plan at wika** — Mga plan na Free, Starter, Plus at Pro na may buwanang puntos, rate limit bawat plan at 30-minutong pagkaantala ng datos sa ibaba ng Plus ([presyo](https://www.simianx.ai/pricing)). Sumasagot ang API sa 16 na wika (`X-Language`). Hindi nagte-trade ang SimianX ng mga totoong account: ang mga posisyon ng autopilot ay mga paper position na maaari mong i-mirror gamit ang sarili mong runner.

## I-install sa isang pangungusap

I-paste ito sa iyong agent. Kukunin nito ang install guide, ilalagay ang skill kung saan nagbabasa ng skills ang iyong agent, at hihingi sa iyo ng key:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Mas gusto mo ng command? Gumagana ang dalawa sa bawat agent na nagbabasa ng skills:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Pagkatapos, sabihin ang **"I-sign in mo ako sa SimianX"**. Bibigyan ka ng agent ng link na aaprubahan sa iyong browser, o ipapadala nito sa email ang 6-digit na code; sa alinmang paraan, makakatanggap ito ng sarili nitong key, may scope at budget, at itatabi ito bilang `SIMIANX_API_KEY`. Wala pang account? Gagawa ng isa ang email code. Puwede ka ring gumawa ng key nang mano-mano sa **Aking Account → Mga API key** sa [simianx.ai](https://www.simianx.ai) at i-export ito:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## I-install para sa iyong agent

| Agent | Native na paraan | Kung saan mapupunta ang skill |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` pagkatapos `/plugin install simianx@simianx` | plugin, o `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` pagkatapos `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (o `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (o `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Iba pa | kopyahin ang `skills/simianx/` sa directory na ini-scan ng iyong agent, o patakbuhin ang `scripts/install.sh --agent auto` | tingnan ang [INSTALL.md](INSTALL.md) |

Nakalista sa [INSTALL.md](INSTALL.md) ang eksaktong directory at mga shell line para sa bawat client; tinutukoy ng `scripts/install.sh` (`install.py` sa Windows: `install.ps1`) ang mga naka-install na agent at kinokopya o nili-link ang skill para sa iyo.

## Ano ang magagawa ng iyong agent

| Kailangan | Tawag | Reperensya |
|---|---|---|
| Magsimula at sumubaybay ng autopilot sa isang stock o coin | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| I-trade nang mano-mano ang paper book ng autopilot | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Patakbuhin ang isang agent ngayon | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| 8-agent na deep research na may verdict at plano | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Ang mga live agent, isang beses | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Classified na balita (mga symbol, value, sentiment), bilang listahan o stream | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Mga sector catalyst: kalendaryo, mga event, mga constituent, mga follow | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Crypto candles, mga indicator, mga quote, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Mga model na maaari mong itakda bawat agent, mga presyo, ang iyong account | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Bawat event sa autopilot log ay may dalang cursor at, para sa anumang maaaring pagkilusan ng agent (`signal.fired`, `position.changed`), isang expiry stamp, kaya hindi kailanman kikilos ang isang runner batay sa lumang impormasyon. Libre ang pagbabasa ng mga event; ang binabayaran mo ay ang mga analysis, gamit ang mga puntos na kasama na sa iyong plan.

## Unang session

1. `GET https://service.simianx.ai/v1/skill` — pampubliko; kinukumpirma na tinatanggap pa ang bersyon ng skill na hawak ng iyong agent.
2. `GET /v1/me` na may `Authorization: Bearer $SIMIANX_API_KEY` — plan, natitirang puntos, mga limit.
3. `POST /v1/analysis/quote` — magkano ang isang tawag, bago magbayad.
4. `POST /v1/autopilots` na may `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — pagkatapos ay i-long-poll ang event log mula sa cursor na ibinabalik ng sagot.

Ang buong loop, bilang `curl`, ay nasa [examples/curl](examples/curl); ang maliit na laging-bukas na runner na nagpapatakbo ng iyong command o webhook sa bawat pagbabago ng posisyon ay nasa [examples/runner](examples/runner).

## Puntos lang ang bayad

- Lahat ay sinisingil sa **puntos** mula sa subscription ng account. Walang top-up at walang pay-per-call.
- Ang mga AI endpoint ay sinusukat batay sa mga model na aktwal na ginamit; inilalathala ng `GET /v1/pricing` ang karaniwang halaga bawat tier (`fast`, `standard`, `frontier`) at ng `GET /v1/models` ang presyo ng bawat model na maaaring piliin ng agent.
- Ang mga data endpoint ay may presyo bawat request (bahagi ng isang punto); walang bayad ang event log, `/v1/me`, `/v1/skill`, `/v1/pricing` at `/v1/models`.
- Ang `402` ay nangangahulugang naubos na ang puntos o ang budget ng key, at sinasabi nito ang solusyon (`renew_now`, `change_plan`, `subscribe`); ang `429` ay rate limit at may kasamang `Retry-After`. Wala nang iba pang itinuturing na problema sa pagbabayad.

## Seguridad

- Nakatira ang key sa environment variable na `SIMIANX_API_KEY`. Hindi kailanman hihilingin ng skill sa isang agent na isulat ito sa repository, log o prompt.
- Hindi kailanman nakakakuha ng website session ang isang agent. Ang pag-sign in mula sa agent (browser link o email code) ay gumagawa lang ng API key para sa agent na iyon, inaabiso sa email at nakalista sa iyong aktibidad sa seguridad; nananatili sa iyo ang website, billing at mga setting ng seguridad.
- May mga scope ang mga key (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), araw-araw at buwanang budget ng puntos, cap bawat tawag at opsyonal na IP allowlist. Bigyan ang agent ng pinakamaliit na key na sapat sa trabaho nito.
- I-revoke ang anumang key sa **Aking Account → Mga API key**; tinatanggihan ang na-revoke na key sa loob ng isang segundo. Bawat tawag ay nilo-log sa ilalim ng iyong account kasama ang halaga nito.
- Binabasa lang ng skill ang sarili mong account: ang iyong mga autopilot, ang iyong mga run, ang iyong mga key. Hindi ito kailanman nagte-trade sa totoong account; ang mga posisyon ng autopilot ay paper position.

## Mga bersyon at update

Iniuulat ng skill ang bersyon nito sa header na `X-SimianX-Skill`. Kapag hindi na tinatanggap ng API ang isang bersyon, sumasagot ito ng `426` kasama ang URL na dapat basahin muli, at laging ipinapakita ng `GET /v1/skill` ang kasalukuyan at pinakamababang bersyon pati ang [changelog](CHANGELOG.md). Mag-update gamit ang sariling command ng iyong agent (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) o patakbuhin muli ang isang pangungusap sa itaas.

## Layout ng repository

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

## Feedback at suporta

- Mula sa agent: `POST /v1/feedback` (binabasa ng team; tinatanggihan at hindi kailanman iniimbak ang mapang-abusong teksto).
- Mula sa tao: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) para sa skill, [simianx.ai/agents](https://www.simianx.ai/agents) para sa produkto.

Basahin ang [CONTRIBUTING.md](CONTRIBUTING.md) bago magbukas ng pull request at ang [SECURITY.md](SECURITY.md) para mag-ulat ng vulnerability.

## Lisensya

MIT para sa lahat ng nasa repository na ito. Ang paggamit ng SimianX API ay saklaw ng [Mga Tuntunin ng Serbisyo](https://www.simianx.ai/legal/terms). Ang mga analysis ng SimianX ay impormasyon, hindi payo sa pamumuhunan; ang mga posisyon ng autopilot ay paper position.
