<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">AI एजेंट्स के लिए SimianX AI</h1>

<p align="center">
  एक skill जो Claude Code, Codex, Cursor, Copilot, Gemini CLI और skills पढ़ने वाले हर दूसरे एजेंट को SimianX ट्रेडिंग डेस्क का क्लाइंट बना देती है:
  एक्ज़ीक्यूशन-ग्रेड इवेंट लॉग वाले autopilots, 8-एजेंट डीप रिसर्च, लाइव विश्लेषण, वर्गीकृत समाचार और सेक्टर कैटालिस्ट।
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">चेंजलॉग</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <b>हिन्दी</b> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## SimianX क्या-क्या कवर करता है

नीचे दी गई हर चीज़ skill के ज़रिए पहुँच में है और [simianx.ai](https://www.simianx.ai) पर रहती है; लिंक हर क्षमता के पीछे वाला प्रोडक्ट पेज खोलते हैं।

**बाज़ार**

- **अमेरिकी स्टॉक और ETF** — 13,000+ सूचीबद्ध इंस्ट्रूमेंट, जिनमें अर्निंग्स, फाइलिंग्स, वित्तीय सीरीज़ और बाज़ार के खुलने-बंद होने के समय की समझ शामिल है। टाइमफ़्रेम `1m 15m 1H 1D 1W 1mo`। → [स्टॉक विश्लेषण](https://www.simianx.ai/c)
- **क्रिप्टो** — OKX, Binance, Bybit और Coinbase पर 1,500+ कॉइन और 4,000+ पेयर: स्पॉट और USDT/USD परपेचुअल स्वैप (`BTC` जैसा अकेला सिंबल परपेचुअल पर रिज़ॉल्व होता है)। टाइमफ़्रेम `1m 5m 15m 1H 4H 1D`। → [क्रिप्टोकरेंसी विश्लेषण](https://www.simianx.ai/l)

**एजेंट क्या करते हैं**

- **Autopilots** — चारों लाइव एजेंट एक सिंबल पर तय शेड्यूल से चलते हैं और, अगर आप अनुमति दें, तो एक पेपर पोज़िशन संभालते हैं (मार्केट, लिमिट और स्टॉप एंट्री, स्केलिंग, स्टॉप-लॉस / टेक-प्रॉफ़िट, एक टाइमिंग गेट)। हर विश्लेषण, सिग्नल और पोज़िशन में बदलाव एक इवेंट लॉग में दर्ज होता है जिसे आप cursor से पढ़ते हैं; `signal.fired` और `position.changed` के साथ एक expiry आती है। आपका एजेंट उस बुक को हाथ से भी ट्रेड कर सकता है। → [स्वचालित पायलट](https://www.simianx.ai/autopilots)
- **डीप रिसर्च** — हर रन में 8 एजेंट्स की एक समिति: चार विश्लेषक (स्टॉक: fundamentals, market, news, timing · क्रिप्टो: fundamentals, market, news, derivatives), एक bull researcher और एक bear researcher (तेज़ी और मंदी के पक्ष), एक research manager जो बहस का संचालन करता है, और एक risk manager जो निर्णय और योजना जारी करता है। होराइज़न `short`, `swing`, `long`; फ़ॉलो-अप सवाल; एक PDF रिपोर्ट। → [डीप विश्लेषण](https://www.simianx.ai/c)
- **लाइव विश्लेषण** — चारों लाइव एजेंट, एक बार: **indicator** (इंडिकेटर: चार्ट पर ट्रेंड, मोमेंटम और स्ट्रक्चर), **intelligence** (इंटेलिजेंस: न्यूज़ फ़्लो और नैरेटिव), **fundamental** (फ़ंडामेंटल: वित्तीय आँकड़े और इवेंट, या किसी कॉइन के लिए ऑन-चेन और डेरिवेटिव्स) और **decision** (निर्णय: एंट्री, स्टॉप और टारगेट के साथ ट्रेड प्रस्ताव)। → [लाइव विश्लेषण](https://www.simianx.ai/l)
- **वर्गीकृत समाचार** — हर लेख को उन सिंबल के आधार पर स्कोर किया जाता है जिन पर उसका असर पड़ता है, उसके वैल्यू (`low` / `medium` / `high`) और उसके सेंटिमेंट के आधार पर — सूची के रूप में, लेख-दर-लेख, 16 भाषाओं में अनुवादित, या लाइव स्ट्रीम के रूप में। → [कहानियाँ](https://www.simianx.ai/stories)
- **Market Pulse** — 1-मिनट, 5-मिनट और 15-मिनट की विंडो पर प्राइस शॉक, 24-घंटे / 30-दिन / 52-सप्ताह के हाई और लो, दिन के मूव और गैप, क्रिप्टो और स्टॉक दोनों के लिए, 1–4 की सेवेरिटी के साथ। → [मार्केट पल्स](https://www.simianx.ai/pulse)
- **Sector Watch** — किसी सेक्टर के लिए प्राथमिक-स्रोत कैटालिस्ट: एक कैलेंडर (PDUFA तारीख़ें, सलाहकार समितियाँ, ट्रायल के नतीजे), 1–4 की सेवेरिटी और दिशा वाले इवेंट (मंज़ूरियाँ, complete response letters, टॉपलाइन नतीजे, डेज़िग्नेशन, निरीक्षण, लेबल अपडेट…), घटक कंपनियाँ, ड्रग एसेट और फ़ॉलो। आज लाइव: **Biopharma · FDA मंज़ूरियाँ**, जो SEC फाइलिंग्स, FDA और Federal Register की विज्ञप्तियों, ClinicalTrials.gov और openFDA से बनाया गया है। → [सेक्टर वॉच](https://www.simianx.ai/sectors)
- **आपकी पसंद के मॉडल** — तीन टियर (`fast`, `standard`, `frontier`) और 7 प्रोवाइडर्स के 50+ मॉडल, जिन्हें पेड प्लान में हर एजेंट के लिए अलग से चुना जा सकता है; पॉइंट्स में कीमतों वाला एक सार्वजनिक कैटलॉग। → [पॉइंट्स और दरें](https://www.simianx.ai/points)
- **लीडरबोर्ड** — हर मॉडल ने असल में कैसा ट्रेड किया, ताकि एजेंट सबूत के आधार पर decision मॉडल चुन सके। → [क्रिप्टोकरेंसी AI मॉडल लीडरबोर्ड](https://www.simianx.ai/crypto-leaderboard)

**प्लान और भाषाएँ** — Free, Starter, Plus और Pro प्लान, जिनमें मासिक पॉइंट्स, प्लान के हिसाब से रेट लिमिट और Plus से नीचे के प्लान में 30 मिनट की डेटा देरी शामिल है ([मूल्य निर्धारण](https://www.simianx.ai/pricing))। API 16 भाषाओं में जवाब देता है (`X-Language`)। SimianX असली खातों में ट्रेड नहीं करता: autopilot की पोज़िशन पेपर पोज़िशन हैं जिन्हें आप अपने runner से मिरर कर सकते हैं।

## एक वाक्य में इंस्टॉल

यह अपने एजेंट को पेस्ट करें। यह इंस्टॉल गाइड लाता है, skill को वहाँ रखता है जहाँ से आपका एजेंट skills पढ़ता है, और आपसे एक key माँगता है:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

कमांड पसंद है? दोनों skills पढ़ने वाले हर एजेंट पर काम करते हैं:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

फिर कहें **"मुझे SimianX में साइन इन करो"**। एजेंट आपको ब्राउज़र में मंज़ूरी देने के लिए एक लिंक देता है, या ईमेल से 6 अंकों का कोड भेजता है; दोनों ही तरीकों से उसे अपनी एक key मिलती है, जिसका scope और बजट तय होता है, और वह उसे `SIMIANX_API_KEY` के रूप में सहेज लेता है। अभी खाता नहीं है? ईमेल कोड से खाता बन जाता है। आप [simianx.ai](https://www.simianx.ai) पर **My Account → API keys** में हाथ से भी key बना सकते हैं और उसे export कर सकते हैं:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## अपने एजेंट के लिए इंस्टॉल

| एजेंट | नेटिव तरीका | skill कहाँ जाती है |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` फिर `/plugin install simianx@simianx` | plugin, या `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` फिर `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (या `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (या `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| कोई और | `skills/simianx/` को उस डायरेक्टरी में कॉपी करें जिसे आपका एजेंट स्कैन करता है, या `scripts/install.sh --agent auto` चलाएँ | देखें [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) में हर क्लाइंट की सटीक डायरेक्टरी और shell लाइनें दी हैं; `scripts/install.sh` (Windows पर `install.py`: `install.ps1`) इंस्टॉल किए गए एजेंट पहचानता है और skill को आपके लिए कॉपी या लिंक कर देता है।

## आपका एजेंट क्या कर सकता है

| ज़रूरत | कॉल | संदर्भ |
|---|---|---|
| किसी स्टॉक या कॉइन पर autopilot शुरू करना और उसे फॉलो करना | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| autopilot की पेपर बुक को हाथ से ट्रेड करना | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| एक एजेंट अभी चलाना | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| निर्णय और योजना के साथ 8-एजेंट डीप रिसर्च | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| लाइव एजेंट्स, एक बार | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| वर्गीकृत समाचार (सिंबल, वैल्यू, सेंटिमेंट), सूची या स्ट्रीम के रूप में | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| सेक्टर कैटालिस्ट: कैलेंडर, इवेंट, घटक, फॉलो | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| क्रिप्टो कैंडल, इंडिकेटर, कोट्स, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| हर एजेंट के लिए चुने जा सकने वाले मॉडल, कीमतें, आपका खाता | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

autopilot लॉग का हर इवेंट एक cursor लेकर चलता है और, जिस पर कोई एजेंट कार्रवाई कर सकता है (`signal.fired`, `position.changed`), उस पर एक expiry stamp भी, ताकि कोई runner कभी बासी जानकारी पर काम न करे। इवेंट पढ़ना मुफ़्त है; आप विश्लेषण के लिए भुगतान करते हैं, उन पॉइंट्स से जो आपके प्लान में पहले से शामिल हैं।

## पहला सत्र

1. `GET https://service.simianx.ai/v1/skill` — सार्वजनिक; पुष्टि करता है कि आपके एजेंट के पास मौजूद skill संस्करण अब भी स्वीकार्य है।
2. `GET /v1/me` साथ में `Authorization: Bearer $SIMIANX_API_KEY` — प्लान, बचे हुए पॉइंट्स, सीमाएँ।
3. `POST /v1/analysis/quote` — किसी कॉल की लागत कितनी होगी, भुगतान से पहले।
4. `POST /v1/autopilots` साथ में `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — फिर जवाब में मिले cursor से इवेंट लॉग को long-poll करें।

पूरा लूप, `curl` के रूप में, [examples/curl](examples/curl) में है; एक छोटा हमेशा-चालू runner जो हर पोज़िशन बदलाव पर आपका कमांड या webhook चलाता है, [examples/runner](examples/runner) में है।

## पॉइंट्स, क्रेडिट नहीं

- सब कुछ खाते की सब्सक्रिप्शन के **पॉइंट्स** में बिल होता है। न कोई टॉप-अप है, न प्रति-कॉल भुगतान।
- AI endpoints वास्तव में इस्तेमाल हुए मॉडलों के हिसाब से मीटर होते हैं; `GET /v1/pricing` हर tier (`fast`, `standard`, `frontier`) की सामान्य लागत प्रकाशित करता है और `GET /v1/models` हर उस मॉडल की कीमत जिसे कोई एजेंट चुन सकता है।
- डेटा endpoints की कीमत प्रति अनुरोध है (एक पॉइंट का अंश); इवेंट लॉग, `/v1/me`, `/v1/skill`, `/v1/pricing` और `/v1/models` की कोई लागत नहीं है।
- `402` का मतलब है पॉइंट्स या किसी key का बजट खत्म हो गया, और यह रास्ता भी बताता है (`renew_now`, `change_plan`, `subscribe`); `429` रेट लिमिट है और `Retry-After` साथ लाता है। इनके अलावा कुछ भी कभी भुगतान की समस्या नहीं है।

## सुरक्षा

- key `SIMIANX_API_KEY` environment variable में रहती है। skill कभी किसी एजेंट से उसे रिपॉज़िटरी, लॉग या प्रॉम्प्ट में लिखने को नहीं कहती।
- एजेंट को कभी वेबसाइट सेशन नहीं मिलता। एजेंट से साइन इन करने पर (ब्राउज़र लिंक या ईमेल कोड से) हमेशा सिर्फ उसी एजेंट के लिए एक API key बनती है, जिसकी सूचना ईमेल से दी जाती है और जो आपकी सुरक्षा गतिविधि में दर्ज होती है; वेबसाइट, बिलिंग और सुरक्षा सेटिंग्स आपके पास ही रहती हैं।
- keys में scopes (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), दैनिक और मासिक पॉइंट बजट, प्रति-कॉल सीमा और एक वैकल्पिक IP allowlist होती है। एजेंट को सबसे छोटी key दें जिससे उसका काम चल जाए।
- कोई भी key **My Account → API keys** में रद्द करें; रद्द की गई key एक सेकंड के भीतर अस्वीकार हो जाती है। हर कॉल आपके खाते के तहत उसकी लागत के साथ लॉग होती है।
- skill केवल आपका अपना खाता पढ़ती है: आपके autopilots, आपके runs, आपकी keys। यह कभी किसी असली खाते में ट्रेड नहीं करती; autopilot की पोज़िशनें पेपर पोज़िशनें हैं।

## संस्करण और अपडेट

skill अपना संस्करण `X-SimianX-Skill` header में बताती है। जब API किसी संस्करण को स्वीकार करना बंद कर देता है, तो वह दोबारा पढ़ने वाले URL के साथ `426` लौटाता है, और `GET /v1/skill` हमेशा वर्तमान और न्यूनतम संस्करण के साथ [चेंजलॉग](CHANGELOG.md) दिखाता है। अपने एजेंट के अपने कमांड से अपडेट करें (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) या ऊपर वाला एक वाक्य दोबारा चलाएँ।

## रिपॉज़िटरी की संरचना

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

## फ़ीडबैक और सहायता

- एजेंट से: `POST /v1/feedback` (टीम पढ़ती है; अपमानजनक टेक्स्ट अस्वीकार होता है और कभी स्टोर नहीं किया जाता)।
- व्यक्ति से: skill के लिए [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues), प्रोडक्ट के लिए [simianx.ai/agents](https://www.simianx.ai/agents)।

pull request खोलने से पहले [CONTRIBUTING.md](CONTRIBUTING.md) और किसी vulnerability की रिपोर्ट के लिए [SECURITY.md](SECURITY.md) देखें।

## लाइसेंस

इस रिपॉज़िटरी की हर चीज़ के लिए MIT। SimianX API का उपयोग [सेवा की शर्तों](https://www.simianx.ai/legal/terms) के अधीन है। SimianX के विश्लेषण जानकारी हैं, निवेश सलाह नहीं; autopilot की पोज़िशनें पेपर पोज़िशनें हैं।
