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
  Her ABD hissesi ve kripto paritesi için dört yapay zekâ analisti, bir de puanlı haber akışı.
  Claude Code, Codex, Cursor ve skill okuyabilen tüm ajanlarda çalışır.
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

## SimianX neler yapar

İşin büyük kısmını iki özellik üstlenir.

- **Çok ajanlı canlı analiz.** Bir hisse ya da kripto paritesi ve bir zaman dilimi seçin; dört ajan aynı anda analize başlar. Gösterge ajanı grafiği okur. İstihbarat ajanı haber akışını izler. Temel analiz ajanı şirket bildirimlerine ve içeriden öğrenenlerin işlemlerine, coinlerde ise zincir üstü ve türev verilerine bakar. Karar ajanı bu üç görüşü tartıp giriş, zarar durdur ve hedef seviyeleriyle bir işlem önerir. → [Canlı analiz](https://www.simianx.ai/l)
- **Puanlı haber akışı.** Her makale, etkilediği sembollerle, bir önem puanıyla ve yükseliş, düşüş ya da nötr yönlü bir yorumla etiketlenmiş olarak gelir. Piyasa Nabzı da bu akışla çalışır; haberler orada ani fiyat hareketleri, yeni zirve ve dipler ile fiyat boşluklarının yanında yer alır. Ajanınız akışı sayfa sayfa okuyabilir ya da kendi sembolleri için açık tutabilir. → [Piyasa Nabzı](https://www.simianx.ai/pulse)

İhtiyaç duyduğunuzda bunlar da var:

- **Derin araştırma.** Sekiz ajan bir hisse ya da coin üzerine tartışır; sonunda bir karar, bir işlem planı ve bir PDF sunar. Ajanınız ek sorular sorabilir. → [Derin analiz](https://www.simianx.ai/c)
- **Sektör Takibi.** Birincil kaynaklardan derlenen katalizör takvimleri ve olaylar, ilk olarak biyofarma için. → [Sektör Takibi](https://www.simianx.ai/sectors)
- **Otopilotlar.** Aynı dört canlı ajan tek bir sembolde, belirlenen bir zamanlamayla çalışır; sanal bir pozisyonu yönetir ve ajanınızın takip edebileceği bir olay günlüğü tutar. → [Otopilotlar](https://www.simianx.ai/autopilots)
- **Modeli siz seçin.** Her ajanın arkasındaki modeli belirleyin; karar vermeden önce her modelin bugüne kadar nasıl işlem yaptığına bakın. → [Model lider tablosu](https://www.simianx.ai/crypto-leaderboard)

Piyasalar: `1m` ile `1mo` arası mumlarla 13.000'den fazla ABD hissesi ve ETF, `1m` ile `1D` arası mumlarla spot ve vadesiz 4.000'den fazla kripto paritesi. → [Hisse Analizi](https://www.simianx.ai/c) · [Kripto Analizi](https://www.simianx.ai/l)

## Tek cümleyle kurulum

Bunu ajanınıza yapıştırın:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Ajan, skill'i skill'leri aradığı yere koyar ve ardından oturum açmanızı sağlar: tarayıcıda bir bağlantıyı onaylarsınız ya da e-postanıza gönderdiğimiz 6 haneli kodu girersiniz. Yeni bir adres için hesap anında açılır. Sonunda ajanın `SIMIANX_API_KEY` içinde kendine ait bir API anahtarı olur; web sitesi oturumunuza ise hiçbir zaman erişemez.

Terminalden kurmak isterseniz:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

Her ajanın (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline ve diğerleri) komutu ve dizini [INSTALL.md](INSTALL.md) dosyasında.

### Ya da MCP ile bağlanın

MCP destekleyen yapay zekâ ajanları, skill kurmadan SimianX'i araç olarak kullanabilir. Uzak sunucuyu anahtarınızla bir kez ekleyin:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

Claude Desktop, Cursor, Codex, VS Code, Windsurf ve Gemini CLI için aynısı [INSTALL.md](INSTALL.md#connect-over-mcp) dosyasında. Kayıt adı: `io.github.SimianX-AI/simianx`.

## İlk çağrılar

| Ne | Çağrı | Referans |
|---|---|---|
| Tek seferlik canlı analiz | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Sembolleriniz için haberler | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| Haberler geldiği anda | `GET /v1/news/stream` (server-sent events, kaldığı yerden devam eder) | [news](skills/simianx/references/news.md) |
| Piyasa Nabzı | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Derin araştırma | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Sektör Takibi | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Otopilotlar | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Temel URL `https://service.simianx.ai/v1`, başlık `Authorization: Bearer $SIMIANX_API_KEY`. Aynı çağrılar kabuk betiği olarak [examples/curl](examples/curl) klasöründe.

## Planlar

Free, Starter, Plus ve Pro; ayrıntılar için [fiyatlandırma](https://www.simianx.ai/pricing) sayfasına bakın. Ajan çağrıları, planınızdaki puanları web sitesiyle aynı tarifelerle kullanır. Haber akışı Plus ve Pro'da canlıdır; Plus'ın altındaki planlarda haberler 30 dakika gecikmeli gelir. Yanıtlar 16 dilde alınabilir. SimianX hiçbir zaman gerçek bir hesapta işlem yapmaz: otopilot pozisyonları sanal pozisyonlardır.

## Güvenlik

- Anahtar `SIMIANX_API_KEY` içinde kalır. Skill onu asla bir depoya, günlüğe ya da prompt'a yazmaz.
- Ajan hiçbir zaman web sitesi oturumu almaz. Bir ajandan oturum açmak yalnızca o ajan için bir API anahtarı oluşturur ve bu olduğunda size e-posta göndeririz.
- Anahtarların kapsamları, günlük ve aylık bütçeleri ve isteğe bağlı bir IP izin listesi vardır. Her ajana, işini görecek en dar yetkili anahtarı verin.
- Bir anahtarı **Hesabım → API anahtarları** bölümünden iptal edin; bir saniye içinde çalışmaz hale gelir.

## Sürümler

Skill, sürümünü `X-SimianX-Skill` başlığında gönderir. Bir sürüm kullanımdan kaldırıldığında API, yeniden okunacak URL ile birlikte `426` döndürür; `GET /v1/skill` ise güncel ve asgari sürümleri gösterir. Ajanınızın kendi komutuyla güncelleyin ya da yukarıdaki cümleyi yeniden yapıştırın. Nelerin değiştiğini [değişiklik günlüğünde](CHANGELOG.md) bulabilirsiniz.

## Depo düzeni

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

## Geri bildirim

- Bir ajandan: `POST /v1/feedback`.
- Bir kişiden: skill için [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues), ürün için [simianx.ai/agents](https://www.simianx.ai/agents).

Pull request açmadan önce [CONTRIBUTING.md](CONTRIBUTING.md) dosyasını, bir güvenlik açığı bildirmek için de [SECURITY.md](SECURITY.md) dosyasını okuyun.

## Lisans

Bu depodaki her şey MIT lisanslıdır. SimianX API'sinin kullanımı [Hizmet Şartları](https://www.simianx.ai/legal/terms) ile düzenlenir. SimianX analizleri bilgi amaçlıdır, yatırım tavsiyesi değildir.
