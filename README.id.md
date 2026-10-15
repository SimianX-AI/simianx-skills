<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI untuk agen AI</h1>

<p align="center">
  Satu skill yang mengubah Claude Code, Codex, Cursor, Copilot, Gemini CLI, dan setiap agen lain yang membaca skill menjadi klien meja trading SimianX:
  autopilot dengan log peristiwa kelas eksekusi, riset mendalam 8 agen, analisis live, berita terklasifikasi, dan katalis sektor.
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
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <b>Bahasa Indonesia</b> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## Apa yang dicakup SimianX

Semua yang ada di bawah ini bisa dijangkau lewat skill dan berada di [simianx.ai](https://www.simianx.ai); tautannya membuka halaman produk di balik setiap kemampuan.

**Pasar**

- **Saham dan ETF AS** — 13,000+ instrumen tercatat, dengan laporan laba, filing, deret data keuangan, dan kesadaran akan jam perdagangan. Timeframe `1m 15m 1H 1D 1W 1mo`. → [Analisis Saham](https://www.simianx.ai/stocks)
- **Kripto** — 1,500+ koin dan 4,000+ pasangan di OKX, Binance, Bybit, dan Coinbase: spot dan swap perpetual USDT/USD (simbol polos seperti `BTC` diarahkan ke perpetual). Timeframe `1m 5m 15m 1H 4H 1D`. → [Analisis Kripto](https://www.simianx.ai/l)

**Apa yang dilakukan para agen**

- **Autopilot** — keempat agen live berjalan sesuai jadwal pada satu simbol dan, jika Anda izinkan, mengelola posisi paper (entri market, limit, dan stop, scaling, stop-loss / take-profit, gerbang timing). Setiap analisis, sinyal, dan perubahan posisi masuk ke log peristiwa yang Anda baca dengan cursor; `signal.fired` dan `position.changed` membawa masa kedaluwarsa. Agen Anda juga bisa mengelola buku itu secara manual. → [Pilot otomatis](https://www.simianx.ai/autopilots)
- **Riset mendalam** — sebuah komite 8 agen per eksekusi: empat analis (saham: fundamentals, market, news, timing · kripto: fundamentals, market, news, derivatives), satu bull researcher dan satu bear researcher (tesis naik dan tesis turun), satu research manager yang memoderasi debat, dan satu risk manager yang mengeluarkan verdict beserta rencananya. Horizon `short`, `swing`, `long`; pertanyaan lanjutan; laporan PDF. → [Analisis mendalam](https://www.simianx.ai/c)
- **Analisis live** — keempat agen live, sekali jalan: **indicator** (tren, momentum, dan struktur pada grafik), **intelligence** (arus berita dan narasi), **fundamental** (laporan keuangan dan peristiwa, atau on-chain dan derivatif untuk sebuah koin), dan **decision** (usulan trade dengan entri, stop, dan target). → [Analisis live](https://www.simianx.ai/l)
- **Berita terklasifikasi** — setiap artikel dinilai berdasarkan simbol yang digerakkannya, nilainya (`low` / `medium` / `high`), dan sentimennya, dalam bentuk daftar, per artikel, diterjemahkan ke 16 bahasa, atau sebagai stream live. → [Cerita](https://www.simianx.ai/stories)
- **Market Pulse** — guncangan harga pada jendela 1 menit, 5 menit, dan 15 menit, tertinggi dan terendah 24 jam / 30 hari / 52 minggu, pergerakan harian dan gap, untuk kripto dan saham, dengan tingkat keparahan 1–4. → [Denyut Pasar](https://www.simianx.ai/pulse)
- **Sector Watch** — katalis dari sumber primer untuk satu sektor: kalender (tanggal PDUFA, komite penasihat, hasil uji klinis), peristiwa dengan tingkat keparahan 1–4 dan arah (persetujuan, complete response letter, hasil topline, designasi, inspeksi, pembaruan label…), konstituen, aset obat, dan follow. Sudah tersedia hari ini: **Biopharma · persetujuan FDA**, dibangun dari filing SEC, rilis FDA dan Federal Register, ClinicalTrials.gov, dan openFDA. → [Pantau Sektor](https://www.simianx.ai/sectors)
- **Model pilihan Anda** — tiga tingkatan (`fast`, `standard`, `frontier`) dan 50+ model dari 7 penyedia yang dapat ditetapkan per agen oleh paket berbayar; katalog publik dengan harga dalam poin. → [Poin & Tarif](https://www.simianx.ai/points)
- **Papan peringkat** — bagaimana setiap model benar-benar melakukan trading, sehingga agen bisa memilih model decision berdasarkan bukti. → [Papan Peringkat Model AI Kripto](https://www.simianx.ai/crypto-leaderboard)

**Paket dan bahasa** — paket Free, Starter, Plus, dan Pro dengan poin bulanan, batas laju per paket, dan jeda data 30 menit untuk paket di bawah Plus ([harga](https://www.simianx.ai/pricing)). API menjawab dalam 16 bahasa (`X-Language`). SimianX tidak melakukan trading di akun sungguhan: posisi autopilot adalah posisi paper yang bisa Anda tiru dengan runner Anda sendiri.

## Instal dalam satu kalimat

Tempel ini ke agen Anda. Ia mengambil panduan instalasi, menaruh skill di tempat agen Anda membaca skill, dan meminta sebuah key:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Lebih suka perintah? Keduanya berfungsi untuk setiap agen yang membaca skill:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Lalu katakan **"Masukkan saya ke SimianX"**. Agen memberi Anda tautan untuk disetujui di browser, atau mengirim kode 6 digit lewat email; dengan cara mana pun ia menerima key miliknya sendiri, dengan scope dan anggaran, lalu menyimpannya sebagai `SIMIANX_API_KEY`. Belum punya akun? Kode email akan membuatkannya. Anda juga bisa membuat key secara manual di **My Account → API keys** pada [simianx.ai](https://www.simianx.ai) dan mengekspornya:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Instal untuk agen Anda

| Agen | Jalur native | Lokasi skill |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` lalu `/plugin install simianx@simianx` | plugin, atau `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` lalu `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (atau `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (atau `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Lainnya | salin `skills/simianx/` ke direktori yang dipindai agen Anda, atau jalankan `scripts/install.sh --agent auto` | lihat [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) mencantumkan direktori persis dan baris shell untuk setiap klien; `scripts/install.sh` (`install.py` di Windows: `install.ps1`) mendeteksi agen yang terpasang dan menyalin atau menautkan skill untuk Anda.

## Apa yang bisa dilakukan agen Anda

| Kebutuhan | Panggilan | Referensi |
|---|---|---|
| Memulai dan mengikuti autopilot pada saham atau koin | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Mengelola buku paper autopilot secara manual | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Menjalankan satu agen sekarang | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Riset mendalam 8 agen dengan verdict dan rencana | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Agen live, sekali jalan | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Berita terklasifikasi (simbol, nilai, sentimen), sebagai daftar atau stream | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Katalis sektor: kalender, peristiwa, konstituen, follow | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Candle kripto, indikator, kuotasi, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Model yang bisa Anda tetapkan per agen, harga, akun Anda | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Setiap peristiwa di log autopilot membawa cursor dan, untuk apa pun yang mungkin ditindaklanjuti agen (`signal.fired`, `position.changed`), sebuah stempel kedaluwarsa, sehingga runner tidak pernah bertindak atas informasi basi. Membaca peristiwa gratis; Anda membayar analisisnya, dengan poin yang sudah termasuk dalam paket Anda.

## Sesi pertama

1. `GET https://service.simianx.ai/v1/skill` — publik; memastikan versi skill yang dipegang agen Anda masih diterima.
2. `GET /v1/me` dengan `Authorization: Bearer $SIMIANX_API_KEY` — paket, sisa poin, batasan.
3. `POST /v1/analysis/quote` — berapa biaya sebuah panggilan, sebelum membayar.
4. `POST /v1/autopilots` dengan `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — lalu long-poll log peristiwa dari cursor yang dikembalikan jawabannya.

Loop lengkapnya, dalam `curl`, ada di [examples/curl](examples/curl); runner kecil yang selalu aktif dan menjalankan perintah atau webhook Anda pada setiap perubahan posisi ada di [examples/runner](examples/runner).

## Poin, bukan kredit

- Semuanya ditagih dalam **poin** dari langganan akun. Tidak ada top-up dan tidak ada bayar-per-panggilan.
- Endpoint AI diukur berdasarkan model yang benar-benar dipakai; `GET /v1/pricing` memublikasikan biaya umum per tier (`fast`, `standard`, `frontier`) dan `GET /v1/models` harga setiap model yang boleh dipilih agen.
- Endpoint data dihargai per permintaan (sepersekian poin); log peristiwa, `/v1/me`, `/v1/skill`, `/v1/pricing`, dan `/v1/models` tidak berbiaya.
- `402` berarti poin atau anggaran key habis dan menyebutkan jalan keluarnya (`renew_now`, `change_plan`, `subscribe`); `429` adalah rate limit dan membawa `Retry-After`. Selain itu tidak pernah ada masalah pembayaran.

## Keamanan

- Key berada di variabel lingkungan `SIMIANX_API_KEY`. Skill tidak pernah meminta agen menuliskannya ke repositori, log, atau prompt.
- Agen tidak pernah mendapat sesi situs web. Masuk dari agen (tautan browser atau kode email) hanya pernah membuat API key untuk agen itu, diumumkan lewat email dan tercantum di aktivitas keamanan Anda; situs web, penagihan, dan pengaturan keamanan tetap di tangan Anda.
- Key membawa scope (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), anggaran poin harian dan bulanan, batas per panggilan, dan allowlist IP opsional. Beri agen key terkecil yang cukup untuk tugasnya.
- Cabut key mana pun di **My Account → API keys**; key yang dicabut ditolak dalam hitungan detik. Setiap panggilan dicatat di akun Anda beserta biayanya.
- Skill hanya membaca akun Anda sendiri: autopilot Anda, run Anda, key Anda. Ia tidak pernah bertransaksi di akun sungguhan; posisi autopilot adalah posisi paper.

## Versi dan pembaruan

Skill melaporkan versinya di header `X-SimianX-Skill`. Saat API tidak lagi menerima sebuah versi, ia menjawab `426` beserta URL yang harus dibaca ulang, dan `GET /v1/skill` selalu menampilkan versi saat ini dan versi minimum beserta [changelog](CHANGELOG.md). Perbarui dengan perintah milik agen Anda sendiri (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) atau jalankan lagi satu kalimat di atas.

## Tata letak repositori

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

## Masukan dan dukungan

- Dari agen: `POST /v1/feedback` (dibaca oleh tim; teks kasar ditolak dan tidak pernah disimpan).
- Dari orang: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) untuk skill, [simianx.ai/agents](https://www.simianx.ai/agents) untuk produk.

Baca [CONTRIBUTING.md](CONTRIBUTING.md) sebelum membuka pull request dan [SECURITY.md](SECURITY.md) untuk melaporkan kerentanan.

## Lisensi

MIT untuk semua yang ada di repositori ini. Penggunaan API SimianX diatur oleh [Ketentuan Layanan](https://www.simianx.ai/legal/terms). Analisis SimianX adalah informasi, bukan saran investasi; posisi autopilot adalah posisi paper.
