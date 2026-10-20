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
  Bigyan ang anumang AI agent ng buong pangkat ng pananaliksik. Sa SimianX AI, kaya ng agent mong tipunin ang komite sa pananaliksik na may 8 agent para sa anumang US stock o crypto pair at tanungin pa ito pagkatapos, kumuha ng live na basa mula sa apat na agent na may entry, stop at target, at panatilihing bukas ang news stream na may score sa mga symbol mo. Isang skill at remote MCP server para sa Claude Code, Codex, Cursor, Muse, Grok Bot, dots at lahat ng iba pang agent.
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

## Bakit dapat bigyan ng SimianX ang agent mo

Tanungin ang isang agent na walang katuwang ng *"Dapat ba akong bumili ng NVDA para sa swing trade?"* at maghahanap ito sa web, magbubuod ng mga ulo ng balita na baka ilang araw nang luma, at magbibigay ng opinyon ng iisang model. Wala itong live na chart, walang kumokontra, at humihinto ito kapag natapos ang usapan.

Kapag may SimianX, ang parehong agent ay:

| | Nang mag-isa | Kasama ang SimianX AI |
|---|---|---|
| Sino ang gumagawa | Iisang model | Komiteng may 8 agent: apat na analyst, isang bull at isang bear na mananaliksik, isang tagapamahala ng pananaliksik, isang tagapamahala ng panganib |
| Ano ang binabasa | Resulta ng paghahanap sa web | Mga live na candle, filing, trade ng insider, daloy ng balita; on-chain at derivatives data para sa coin |
| Ano ang makukuha mo | Isang opinyon | Hatol na may entry, stop at target, at isang PDF na ulat |
| Pagkatapos | Magsisimula ulit | Ipinapasa ang mga karagdagang tanong sa parehong komite, o nagtatakda ng autopilot para patuloy na magbantay |

## Mga puwede mong itanong

Kapag naka-install na ang skill, magtanong sa sarili mong pananalita:

- *"Ipunin ang komite ng SimianX para suriin ang NVDA bilang swing trade."* Nag-uulat ang apat na analyst, nagtatalo nang husto ang bull at ang bear, at ibinabalik ng tagapamahala ng panganib ang hatol, ang plano at isang PDF.
- *"Tanungin ang bear na mananaliksik kung ano ang magpapatunay na mali ang pananaw ng bull."* Napupunta ang mga karagdagang tanong sa parehong pagsusuri, kaya nakabatay ang sagot sa lahat ng nabasa na ng komite.
- *"Ipasuri sa komite ang SOL para sa maikling panahon."* Kapag coin, binabasa rin ng mga analyst ang on-chain na daloy ng pondo at ang derivatives market.
- *"Kumusta ang BTC sa 15-minutong chart ngayon?"* Sumasagot ang apat na live agent, at sinasabi ng Decision agent kung bibili, magbebenta o huwag munang pumasok, na may entry, stop at target.
- *"Sabihan mo ako kapag may mahalagang balita sa TSLA o ETH."* News stream na may score sa mga symbol mo, live sa sandaling ma-score ang bawat balita.
- *"Bantayan ang AAPL sa 1-oras na chart at hawakan ang isang paper position."* Muling pinapatakbo ng autopilot ang mga agent sa bawat pagsara ng candle at itinatala ang bawat signal.
- *"Anong mga PDUFA date sa biopharma ang papatak sa susunod na 30 araw?"* Sector Watch, mula sa mga pangunahing pinagmulan.
- *"Ano ang biglang gumalaw nang malakas sa crypto nitong nakaraang oras?"* Market Pulse: biglaang galaw, mga bagong high at low, pagsipa ng volume at mga gap.

Masusubukan ng mga libreng account ang komite sa mga sikat na symbol gaya ng NVDA, AAPL, TSLA, BTC at ETH.

## Ano ang saklaw ng SimianX

Ito ang dalawang pinakaginagamit.

- **Live na multi-agent na pagsusuri.** Pumili ng stock o crypto pair at timeframe, at sabay itong babasahin ng apat na agent. Chart ang binabasa ng Indicator. Ang daloy ng balita naman ang sa Intelligence. Sa Fundamental, mga filing at trade ng insider, o on-chain at derivatives data kung coin. Tinitimbang ng Decision ang tatlo at nagmumungkahi ng trade na may entry, stop at target. → [Live na pagsusuri](https://www.simianx.ai/l)
- **News stream na may score.** Dumarating ang bawat artikulo na may tag ng mga symbol na ginagalaw nito, value score, at bullish, bearish o neutral na basa. Ito ang feed sa likod ng Pulso ng Merkado, kung saan katabi nito ang biglaang galaw ng presyo, mga bagong high at low, at mga gap. Puwede itong i-page ng agent mo, o panatilihing bukas ang stream para sa mga symbol nito. → [Pulso ng Merkado](https://www.simianx.ai/pulse)

Mayroon ding iba kapag kailangan mo:

- **Malalim na research.** Walong agent ang nagdedebate tungkol sa isang stock o coin at nagbabalik ng hatol, trade plan at PDF. Puwedeng magtanong pa ang agent mo. → [Malalim na pagsusuri](https://www.simianx.ai/c)
- **Sector Watch.** Mga catalyst calendar at event mula sa mga pangunahing pinagmulan, simula sa biopharma. → [Sector Watch](https://www.simianx.ai/sectors)
- **Mga autopilot.** Ang parehong apat na live agent, naka-iskedyul para sa isang symbol, may paper position at event log na masusundan ng agent mo. → [Awtomatikong piloto](https://www.simianx.ai/autopilots)
- **Ikaw ang pipili ng model.** Itakda ang model sa likod ng bawat agent, at tingnan muna kung paano nag-trade ang bawat isa. → [Leaderboard ng mga model](https://www.simianx.ai/crypto-leaderboard)

Mga merkado: 13,000+ na US stock at ETF sa `1m` hanggang `1mo` na candle, at 4,000+ na crypto pair, spot at perpetual, sa `1m` hanggang `1D`. → [Pagsusuri ng Stock](https://www.simianx.ai/c) · [Pagsusuri ng Crypto](https://www.simianx.ai/l)

## I-install sa isang pangungusap

I-paste ito sa agent mo:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and sign me in.
```

Ilalagay nito ang skill kung saan naghahanap ng skills ang agent mo, saka ka nito isa-sign in. Aaprubahan mo ang isang link sa browser, o ita-type mo ang 6-digit na code na i-e-email namin. Kung bagong email, gagawan ka agad ng account. Sa huli, may sariling API key ang agent sa `SIMIANX_API_KEY`, at hindi nito kailanman makukuha ang login mo sa website.

Mula sa terminal naman:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

Nasa [INSTALL.md](INSTALL.md) ang command at directory para sa bawat agent (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline at iba pa).

### Muse, Grok Bot, dots at iba pang agent na may sariling computer

Binabasa rin ng mga agent na tumatakbo sa sarili nilang cloud computer ang parehong pangungusap. Kumokonekta sila gamit ang MCP o gumagawa ng pangkonekta mula sa [dokumentong OpenAPI](https://service.simianx.ai/v1/openapi.json), isina-sign in ka, itinatabi ang key sa sarili nilang taguan ng kredensyal, at sine-save ang SimianX bilang skill. Nasa [INSTALL.md](INSTALL.md#agents-with-their-own-computer-muse-grok-bot-dots) ang eksaktong sasabihin sa Muse, Grok Bot at dots.

### O kumonekta gamit ang MCP

Magagamit ng mga AI agent na marunong ng MCP ang SimianX bilang mga tool kahit walang naka-install na skill. Idagdag ang remote server nang isang beses gamit ang key mo:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

Nasa [INSTALL.md](INSTALL.md#connect-over-mcp) ang katumbas para sa Claude Desktop, Cursor, Codex, VS Code, Windsurf, Gemini CLI, Grok Bot at Muse. Pangalan sa registry: `io.github.SimianX-AI/simianx`.

## Mga unang tawag

| Ano | Tawag | Reperensya |
|---|---|---|
| Isang live na pagsusuri | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Balita sa mga symbol mo | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| Balita habang dumarating | `GET /v1/news/stream` (server-sent events, naitutuloy kapag naputol) | [news](skills/simianx/references/news.md) |
| Pulso ng Merkado | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Malalim na research | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Sector Watch | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Mga autopilot | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL `https://service.simianx.ai/v1`, header `Authorization: Bearer $SIMIANX_API_KEY`. Nasa [examples/curl](examples/curl) ang parehong mga tawag bilang shell script.

## Mga plan

Free, Starter, Plus at Pro ang mga plan. Nasa pahina ng [presyo](https://www.simianx.ai/pricing) ang detalye. Ginagamit ng mga tawag ng agent ang puntos ng plan mo, sa parehong rate ng website. Live ang news stream sa Plus at Pro. Sa ibaba ng Plus, 30 minutong huli ang balita. Sumasagot ito sa 16 na wika. Hindi kailanman nagte-trade ang SimianX ng totoong account, at paper position ang lahat ng posisyon ng autopilot.

## Seguridad

- Nasa `SIMIANX_API_KEY` lang ang key. Hindi ito kailanman isusulat ng skill sa repository, log o prompt.
- Hindi kailanman nakakakuha ng website session ang agent. Gumagawa lang ng API key para sa agent na iyon ang pag-sign in mula rito, at ie-email ka namin kapag nangyari ito.
- May scope, araw-araw at buwanang budget, at opsyonal na IP allowlist ang bawat key. Bigyan ang bawat agent ng pinakamaliit na key na sapat sa trabaho nito.
- I-revoke ang key sa **Aking Account → Mga API key** at titigil itong gumana sa loob ng isang segundo.

## Mga bersyon

Ipinapadala ng skill ang bersyon nito sa header na `X-SimianX-Skill`. Kapag retirado na ang isang bersyon, sasagot ang API ng `426` kasama ang URL na dapat basahin muli, at ipinapakita ng `GET /v1/skill` ang kasalukuyan at pinakamababang bersyon. Mag-update gamit ang sariling command ng agent mo, o i-paste ulit ang pangungusap sa itaas. Nasa [changelog](CHANGELOG.md) kung ano ang nagbago.

## Layout ng repository

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

- Mula sa agent: `POST /v1/feedback`.
- Mula sa tao: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) para sa skill, [simianx.ai/agents](https://www.simianx.ai/agents) para sa produkto.

Basahin ang [CONTRIBUTING.md](CONTRIBUTING.md) bago magbukas ng pull request, at ang [SECURITY.md](SECURITY.md) para mag-ulat ng vulnerability.

## Lisensya

MIT ang lahat ng nasa repository na ito. Ang paggamit ng SimianX API ay saklaw ng [Mga Tuntunin ng Serbisyo](https://www.simianx.ai/legal/terms). Impormasyon ang mga pagsusuri ng SimianX, hindi payo sa pamumuhunan.
