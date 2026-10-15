<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">Yapay zekâ ajanları için SimianX AI</h1>

<p align="center">
  Claude Code, Codex, Cursor, Copilot, Gemini CLI ve skill okuyan diğer tüm ajanları SimianX trading masasının bir istemcisine dönüştüren tek bir skill:
  icra kalitesinde olay günlüğüne sahip otopilotlar, 8 ajanlı derin araştırma, canlı analiz, sınıflandırılmış haberler ve sektör katalizörleri.
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">Değişiklik günlüğü</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <b>Türkçe</b>
</p>

---

## SimianX neleri kapsar

Aşağıdakilerin tümüne skill üzerinden ulaşılır ve hepsi [simianx.ai](https://www.simianx.ai) üzerinde yaşar; bağlantılar her yeteneğin arkasındaki ürün sayfasını açar.

**Piyasalar**

- **ABD hisseleri ve ETF'ler** — 13.000'den fazla kote enstrüman; kazanç raporları, dosyalamalar, finansal seriler ve piyasa saatleri farkındalığıyla. Zaman dilimleri `1m 15m 1H 1D 1W 1mo`. → [Hisse Analizi](https://www.simianx.ai/stocks)
- **Kripto** — OKX, Binance, Bybit ve Coinbase üzerinde 1.500'den fazla coin ve 4.000'den fazla parite: spot ve USDT/USD perpetual swap'ler (`BTC` gibi yalın bir sembol perpetual'a çözümlenir). Zaman dilimleri `1m 5m 15m 1H 4H 1D`. → [Kripto Analizi](https://www.simianx.ai/l)

**Ajanlar ne yapar**

- **Otopilotlar** — dört canlı ajan tek bir sembol üzerinde bir zamanlamaya göre çalışır ve izin verirseniz bir kağıt pozisyonu yönetir (piyasa, limit ve stop girişleri, kademeli ekleme/azaltma, stop-loss / take-profit, bir zamanlama kapısı). Her analiz, sinyal ve pozisyon değişikliği, imleçle okuduğunuz bir olay günlüğüne düşer; `signal.fired` ve `position.changed` bir son kullanma damgası taşır. Ajanınız bu portföyde elle de işlem yapabilir. → [Otopilotlar](https://www.simianx.ai/autopilots)
- **Derin araştırma** — çalıştırma başına 8 ajanlı bir kurul: dört analist (hisseler: fundamentals, market, news, timing · kripto: fundamentals, market, news, derivatives), bir bull researcher (boğa) ve bir bear researcher (ayı), tartışmayı yöneten bir research manager ve kararı ile planı veren bir risk manager. Ufuklar `short`, `swing`, `long`; takip soruları; bir PDF raporu. → [Derin analiz](https://www.simianx.ai/c)
- **Canlı analiz** — dört canlı ajan, tek seferlik: **indicator** (gösterge: grafikte trend, momentum, yapı), **intelligence** (istihbarat: haber akışı ve anlatı), **fundamental** (temel: finansallar ve olaylar, ya da bir coin için on-chain ve türevler) ve **decision** (karar: giriş, stop ve hedefiyle işlem önerisi). → [Canlı analiz](https://www.simianx.ai/l)
- **Sınıflandırılmış haberler** — her makale hareket ettirdiği sembollere, değerine (`low` / `medium` / `high`) ve duygusuna göre puanlanır; liste olarak, makale bazında, 16 dile çevrilmiş olarak ya da canlı akış olarak. → [Hikayeler](https://www.simianx.ai/stories)
- **Market Pulse** — 1, 5 ve 15 dakikalık pencerelerde fiyat şokları, 24 saatlik / 30 günlük / 52 haftalık zirveler ve dipler, günlük hareketler ve gap'ler, kripto ve hisseler için, 1–4 arası şiddetle. → [Piyasa Nabzı](https://www.simianx.ai/pulse)
- **Sector Watch** — bir sektör için birincil kaynaklı katalizörler: bir takvim (PDUFA tarihleri, danışma komiteleri, deneme sonuçları), 1–4 şiddet ve yönle olaylar (onaylar, complete response letter'lar, topline sonuçlar, atamalar, denetimler, etiket güncellemeleri…), bileşenler, ilaç varlıkları ve takipler. Bugün canlı: **Biopharma · FDA onayları**; SEC dosyalamaları, FDA ve Federal Register duyuruları, ClinicalTrials.gov ve openFDA'dan derlenir. → [Sektör Takibi](https://www.simianx.ai/sectors)
- **Seçtiğiniz modeller** — üç kademe (`fast`, `standard`, `frontier`) ve 7 sağlayıcıdan 50'den fazla model; ücretli bir plan bunları ajan başına ayarlayabilir; puan cinsinden fiyatlarla herkese açık bir katalog. → [Puan ve Tarifeler](https://www.simianx.ai/points)
- **Lider tablosu** — her modelin gerçekte nasıl işlem yaptığı, böylece bir ajan karar modelini kanıta dayanarak seçebilir. → [Kripto AI Model Lider Tablosu](https://www.simianx.ai/crypto-leaderboard)

**Planlar ve diller** — aylık puanlar, plan başına hız limitleri ve Plus altında 30 dakikalık veri gecikmesiyle Free, Starter, Plus ve Pro planları ([fiyatlandırma](https://www.simianx.ai/pricing)). API 16 dilde yanıt verir (`X-Language`). SimianX gerçek hesaplarda işlem yapmaz: otopilot pozisyonları, kendi runner'ınızla yansıtabileceğiniz kağıt pozisyonlardır.

## Tek cümleyle kurulum

Bunu ajanınıza yapıştırın. Kurulum kılavuzunu alır, skill'i ajanınızın skill okuduğu yere koyar ve sizden bir anahtar ister:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Komut mu tercih edersiniz? İkisi de skill okuyan her ajanla çalışır:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Ardından [simianx.ai](https://www.simianx.ai) üzerinde **Hesabım → API anahtarları** bölümünden bir anahtar oluşturup dışa aktarın:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Ajanınız için kurulum

| Ajan | Yerel yol | Skill'in konulduğu yer |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` ardından `/plugin install simianx@simianx` | eklenti veya `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` ardından `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (veya `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (veya `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Diğer her şey | `skills/simianx/` dizinini ajanınızın taradığı dizine kopyalayın ya da `scripts/install.sh --agent auto` çalıştırın | bkz. [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) her istemci için tam dizini ve kabuk satırlarını listeler; `scripts/install.sh` (`install.py`, Windows'ta: `install.ps1`) kurulu ajanları algılar ve skill'i sizin için kopyalar ya da bağlar.

## Ajanınız neler yapabilir

| İhtiyaç | Çağrı | Referans |
|---|---|---|
| Bir hisse ya da coin üzerinde otopilot başlatıp takip etmek | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Otopilotun kağıt portföyünde elle işlem yapmak | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Bir ajanı hemen çalıştırmak | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Karar ve planla birlikte 8 ajanlı derin araştırma | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Canlı ajanlar, tek seferlik | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Sınıflandırılmış haberler (semboller, değer, duygu), liste ya da akış olarak | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Sektör katalizörleri: takvim, olaylar, bileşenler, takipler | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Kripto mumları, göstergeler, kotasyonlar, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Ajan başına ayarlayabileceğiniz modeller, fiyatlar, hesabınız | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Otopilot günlüğündeki her olay bir imleç taşır; bir ajanın üzerine hareket edebileceği her şey (`signal.fired`, `position.changed`) ayrıca bir son kullanma damgası taşır, böylece bir runner asla bayat bilgiyle hareket etmez. Olayları okumak ücretsizdir; analizler için planınızın zaten içerdiği puanlarla ödersiniz.

## İlk oturum

1. `GET https://service.simianx.ai/v1/skill` — herkese açık; ajanınızın tuttuğu skill sürümünün hâlâ kabul edildiğini doğrular.
2. `GET /v1/me`, `Authorization: Bearer $SIMIANX_API_KEY` ile — plan, kalan puan, limitler.
3. `POST /v1/analysis/quote` — ödemeden önce bir çağrının ne kadara mal olacağı.
4. `POST /v1/autopilots`, `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` ile — ardından yanıtın döndürdüğü imleçten itibaren olay günlüğünü long-poll edin.

Tam döngü, `curl` olarak, [examples/curl](examples/curl) içinde; her pozisyon değişikliğinde komutunuzu ya da webhook'unuzu çalıştıran küçük, sürekli açık bir runner ise [examples/runner](examples/runner) içinde.

## Puan, kredi değil

- Her şey hesabın aboneliğinden **puan** olarak faturalandırılır. Bakiye yükleme ve çağrı başına ödeme yoktur.
- Yapay zekâ uç noktaları gerçekten kullanılan modellere göre ölçülür; `GET /v1/pricing` kademe başına (`fast`, `standard`, `frontier`) olağan maliyeti, `GET /v1/models` ise bir ajanın seçebileceği her modelin fiyatını yayımlar.
- Veri uç noktaları istek başına fiyatlandırılır (bir puanın kesri); olay günlüğü, `/v1/me`, `/v1/skill`, `/v1/pricing` ve `/v1/models` hiçbir şeye mal olmaz.
- `402`, puanın ya da bir anahtar bütçesinin tükendiği anlamına gelir ve çıkış yolunu adlandırır (`renew_now`, `change_plan`, `subscribe`); `429` bir hız sınırıdır ve `Retry-After` taşır. Bunların dışında hiçbir şey asla bir ödeme sorunu değildir.

## Güvenlik

- Anahtar `SIMIANX_API_KEY` ortam değişkeninde yaşar. Skill, bir ajandan onu asla bir depoya, günlüğe ya da prompt'a yazmasını istemez.
- Anahtarlar kapsamlar (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), günlük ve aylık puan bütçeleri, çağrı başına bir üst sınır ve isteğe bağlı bir IP izin listesi taşır. Bir ajana işini gören en küçük anahtarı verin.
- Herhangi bir anahtarı **Hesabım → API anahtarları** bölümünden iptal edin; iptal edilen anahtar bir saniye içinde reddedilir. Her çağrı maliyetiyle birlikte hesabınız altında kaydedilir.
- Skill yalnızca kendi hesabınızı okur: otopilotlarınız, çalıştırmalarınız, anahtarlarınız. Asla gerçek bir hesapta işlem yapmaz; otopilot pozisyonları kağıt pozisyonlardır.

## Sürümler ve güncellemeler

Skill, sürümünü `X-SimianX-Skill` başlığında bildirir. API bir sürümü artık kabul etmediğinde, yeniden okunacak URL ile birlikte `426` yanıtı verir; `GET /v1/skill` ise her zaman güncel ve asgari sürümü, ayrıca [değişiklik günlüğünü](CHANGELOG.md) gösterir. Ajanınızın kendi komutuyla (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) güncelleyin ya da yukarıdaki tek cümleyi yeniden çalıştırın.

## Depo düzeni

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

## Geri bildirim ve destek

- Bir ajandan: `POST /v1/feedback` (ekip tarafından okunur; hakaret içeren metin reddedilir ve asla saklanmaz).
- Bir kişiden: skill için [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues), ürün için [simianx.ai/agents](https://www.simianx.ai/agents).

Bir pull request açmadan önce [CONTRIBUTING.md](CONTRIBUTING.md) dosyasına, bir güvenlik açığı bildirmek için [SECURITY.md](SECURITY.md) dosyasına bakın.

## Lisans

Bu depodaki her şey için MIT. SimianX API'sinin kullanımı [Hizmet Şartları](https://www.simianx.ai/legal/terms) ile düzenlenir. SimianX analizleri bilgidir, yatırım tavsiyesi değildir; otopilot pozisyonları kağıt pozisyonlardır.
