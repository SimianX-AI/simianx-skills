<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI dành cho các AI agent</h1>

<p align="center">
  Một skill duy nhất biến Claude Code, Codex, Cursor, Copilot, Gemini CLI và mọi agent khác biết đọc skill thành client của bàn giao dịch SimianX:
  autopilot với nhật ký sự kiện cấp thực thi, nghiên cứu chuyên sâu 8 agent, phân tích trực tiếp, tin tức đã phân loại và chất xúc tác theo ngành.
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">Nhật ký thay đổi</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <b>Tiếng Việt</b> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## SimianX bao phủ những gì

Mọi thứ dưới đây đều truy cập được qua skill và nằm trên [simianx.ai](https://www.simianx.ai); các liên kết mở trang sản phẩm đứng sau từng năng lực.

**Thị trường**

- **Cổ phiếu và ETF Mỹ** — 13.000+ mã niêm yết, kèm báo cáo lợi nhuận, hồ sơ nộp, chuỗi số liệu tài chính và nhận biết giờ giao dịch. Khung thời gian `1m 15m 1H 1D 1W 1mo`. → [Phân tích cổ phiếu](https://www.simianx.ai/stocks)
- **Crypto** — 1.500+ đồng coin và 4.000+ cặp giao dịch trên OKX, Binance, Bybit và Coinbase: giao dịch spot và hợp đồng hoán đổi vĩnh cửu USDT/USD (một ký hiệu trần như `BTC` sẽ được hiểu là hợp đồng vĩnh cửu). Khung thời gian `1m 5m 15m 1H 4H 1D`. → [Phân tích tiền điện tử](https://www.simianx.ai/l)

**Các agent làm gì**

- **Autopilots** — bốn agent trực tiếp chạy theo lịch trên một mã và, nếu bạn cho phép, quản lý một vị thế giả lập (vào lệnh thị trường, giới hạn và dừng, gia giảm khối lượng, cắt lỗ / chốt lời, một cổng chọn thời điểm). Mọi phân tích, tín hiệu và thay đổi vị thế đều được ghi vào nhật ký sự kiện mà bạn đọc bằng cursor; `signal.fired` và `position.changed` mang theo thời điểm hết hạn. Agent của bạn cũng có thể tự tay giao dịch trên sổ lệnh đó. → [Thiết bị lái tự động](https://www.simianx.ai/autopilots)
- **Nghiên cứu chuyên sâu** — một hội đồng 8 agent cho mỗi lần chạy: bốn nhà phân tích (cổ phiếu: fundamentals, market, news, timing · crypto: fundamentals, market, news, derivatives), một bull researcher (phe mua) và một bear researcher (phe bán), một research manager (quản lý nghiên cứu) điều phối cuộc tranh luận và một risk manager (quản lý rủi ro) đưa ra kết luận cùng kế hoạch. Tầm nhìn `short`, `swing`, `long`; câu hỏi tiếp theo; báo cáo PDF. → [Phân tích chuyên sâu](https://www.simianx.ai/c)
- **Phân tích trực tiếp** — bốn agent trực tiếp, chạy một lần: **indicator** (chỉ báo: xu hướng, động lượng, cấu trúc trên biểu đồ), **intelligence** (tình báo: dòng tin tức và câu chuyện thị trường), **fundamental** (cơ bản: tài chính và sự kiện, hoặc on-chain và phái sinh với một đồng coin) và **decision** (quyết định: đề xuất giao dịch với điểm vào, điểm dừng và mục tiêu). → [Phân tích trực tiếp](https://www.simianx.ai/l)
- **Tin tức đã phân loại** — mỗi bài viết được chấm theo các mã mà nó tác động, giá trị (`low` / `medium` / `high`) và tâm lý thị trường; lấy dạng danh sách, theo từng bài, dịch sang 16 ngôn ngữ, hoặc dạng stream trực tiếp. → [Câu chuyện](https://www.simianx.ai/stories)
- **Market Pulse** — cú sốc giá trên các cửa sổ 1 phút, 5 phút và 15 phút, đỉnh/đáy 24 giờ / 30 ngày / 52 tuần, biến động trong ngày và khoảng trống giá (gap), cho cả crypto và cổ phiếu, với mức nghiêm trọng 1–4. → [Nhịp Thị Trường](https://www.simianx.ai/pulse)
- **Sector Watch** — chất xúc tác từ nguồn sơ cấp cho một ngành: lịch (ngày PDUFA, ủy ban cố vấn, công bố kết quả thử nghiệm), sự kiện với mức nghiêm trọng 1–4 và chiều hướng (phê duyệt, thư phản hồi đầy đủ, kết quả topline, chỉ định đặc biệt, thanh tra, cập nhật nhãn thuốc…), thành phần, tài sản thuốc và theo dõi. Đang hoạt động: **Biopharma · FDA approvals** (dược sinh học · phê duyệt của FDA), xây dựng từ hồ sơ SEC, thông cáo của FDA và Federal Register, ClinicalTrials.gov và openFDA. → [Theo dõi ngành](https://www.simianx.ai/sectors)
- **Model do bạn chọn** — ba tier (`fast`, `standard`, `frontier`) và 50+ model từ 7 nhà cung cấp mà gói trả phí có thể đặt riêng cho từng agent; danh mục công khai với giá tính bằng điểm. → [Điểm & Đơn giá](https://www.simianx.ai/points)
- **Bảng xếp hạng** — mỗi model đã thực sự giao dịch ra sao, để agent có thể chọn model quyết định dựa trên bằng chứng. → [Bảng xếp hạng AI tiền điện tử](https://www.simianx.ai/crypto-leaderboard)

**Gói và ngôn ngữ** — các gói Free, Starter, Plus và Pro với điểm hằng tháng, giới hạn tốc độ theo từng gói và độ trễ dữ liệu 30 phút với các gói dưới Plus ([giá](https://www.simianx.ai/pricing)). API trả lời bằng 16 ngôn ngữ (`X-Language`). SimianX không giao dịch tài khoản thật: vị thế của autopilot là vị thế giả lập mà bạn có thể sao chép bằng runner của chính mình.

## Cài đặt bằng một câu

Dán câu này cho agent của bạn. Nó sẽ tải hướng dẫn cài đặt, đặt skill vào nơi agent của bạn đọc skill, rồi hỏi bạn một khóa:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Thích dùng lệnh hơn? Cả hai cách đều chạy được với mọi agent biết đọc skill:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Sau đó tạo một khóa tại **Tài khoản của tôi → Khóa API** trên [simianx.ai](https://www.simianx.ai) rồi export nó:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Cài đặt cho agent của bạn

| Agent | Cách cài gốc | Skill được đặt ở đâu |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` rồi `/plugin install simianx@simianx` | plugin, hoặc `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` rồi `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (hoặc `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (hoặc `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Agent khác | sao chép `skills/simianx/` vào thư mục mà agent của bạn quét, hoặc chạy `scripts/install.sh --agent auto` | xem [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) liệt kê chính xác thư mục và các dòng lệnh shell cho từng client; `scripts/install.sh` (hoặc `install.py`; trên Windows: `install.ps1`) tự phát hiện các agent đã cài và sao chép hoặc liên kết skill cho bạn.

## Agent của bạn làm được gì

| Nhu cầu | Gọi | Tài liệu |
|---|---|---|
| Khởi chạy và theo dõi một autopilot trên một cổ phiếu hoặc một coin | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Tự tay giao dịch trên sổ lệnh giả lập của autopilot | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Chạy một agent ngay bây giờ | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Nghiên cứu chuyên sâu 8 agent kèm kết luận và kế hoạch | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Các agent trực tiếp, chạy một lần | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Tin tức đã phân loại (mã, giá trị, tâm lý thị trường), dạng danh sách hoặc stream | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Chất xúc tác theo ngành: lịch, sự kiện, thành phần, theo dõi | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Nến crypto, chỉ báo, báo giá, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Các model bạn có thể đặt cho từng agent, giá, tài khoản của bạn | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Mỗi sự kiện trong nhật ký autopilot đều mang một cursor và, với bất kỳ sự kiện nào agent có thể hành động theo (`signal.fired`, `position.changed`), một dấu hết hạn, nên runner không bao giờ hành động trên thông tin cũ. Đọc sự kiện là miễn phí; bạn chỉ trả cho các phân tích, bằng số điểm mà gói của bạn đã bao gồm sẵn.

## Phiên đầu tiên

1. `GET https://service.simianx.ai/v1/skill` — công khai; xác nhận phiên bản skill mà agent của bạn đang giữ vẫn được chấp nhận.
2. `GET /v1/me` với `Authorization: Bearer $SIMIANX_API_KEY` — gói, số điểm còn lại, giới hạn.
3. `POST /v1/analysis/quote` — một lệnh gọi sẽ tốn bao nhiêu, trước khi trả.
4. `POST /v1/autopilots` với `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — rồi long-poll nhật ký sự kiện từ cursor mà phản hồi trả về.

Vòng lặp đầy đủ, dưới dạng `curl`, nằm ở [examples/curl](examples/curl); một runner nhỏ chạy liên tục, thực thi lệnh hoặc webhook của bạn mỗi khi vị thế thay đổi, nằm ở [examples/runner](examples/runner).

## Điểm, không phải tín dụng

- Mọi thứ đều được tính bằng **điểm** từ gói đăng ký của tài khoản. Không có nạp thêm, không có trả theo từng lệnh gọi.
- Các endpoint AI được tính theo model thực tế đã dùng; `GET /v1/pricing` công bố chi phí thông thường cho từng tier (`fast`, `standard`, `frontier`) và `GET /v1/models` công bố giá của từng model mà agent có thể chọn.
- Các endpoint dữ liệu tính theo request (một phần nhỏ của một điểm); nhật ký sự kiện, `/v1/me`, `/v1/skill`, `/v1/pricing` và `/v1/models` không tốn gì.
- `402` nghĩa là hết điểm hoặc hết ngân sách của khóa, và cho biết lối ra (`renew_now`, `change_plan`, `subscribe`); `429` là giới hạn tốc độ và kèm `Retry-After`. Không có mã nào khác là vấn đề thanh toán.

## Bảo mật

- Khóa nằm trong biến môi trường `SIMIANX_API_KEY`. Skill không bao giờ yêu cầu agent ghi nó vào repository, log hay prompt.
- Khóa có scope (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), ngân sách điểm theo ngày và theo tháng, mức trần mỗi lệnh gọi và danh sách IP cho phép (tùy chọn). Hãy cấp cho agent khóa nhỏ nhất đủ để làm việc.
- Thu hồi bất kỳ khóa nào tại **Tài khoản của tôi → Khóa API**; khóa đã thu hồi bị từ chối trong vòng một giây. Mọi lệnh gọi đều được ghi lại dưới tài khoản của bạn kèm chi phí.
- Skill chỉ đọc tài khoản của chính bạn: autopilot của bạn, các lần chạy của bạn, khóa của bạn. Nó không bao giờ giao dịch trên tài khoản thật; vị thế của autopilot là vị thế giả lập.

## Phiên bản và cập nhật

Skill báo phiên bản của mình trong header `X-SimianX-Skill`. Khi API không còn chấp nhận một phiên bản, nó trả lời `426` kèm URL cần đọc lại, và `GET /v1/skill` luôn hiển thị phiên bản hiện tại và phiên bản tối thiểu cùng với [nhật ký thay đổi](CHANGELOG.md). Cập nhật bằng lệnh riêng của agent (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) hoặc chạy lại câu ở trên.

## Bố cục repository

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

## Phản hồi và hỗ trợ

- Từ agent: `POST /v1/feedback` (đội ngũ sẽ đọc; nội dung lăng mạ bị từ chối và không bao giờ được lưu).
- Từ người dùng: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) cho skill, [simianx.ai/agents](https://www.simianx.ai/agents) cho sản phẩm.

Hãy xem [CONTRIBUTING.md](CONTRIBUTING.md) trước khi mở pull request và [SECURITY.md](SECURITY.md) để báo cáo lỗ hổng bảo mật.

## Giấy phép

MIT cho mọi thứ trong repository này. Việc sử dụng SimianX API tuân theo [Điều khoản dịch vụ](https://www.simianx.ai/legal/terms). Các phân tích của SimianX chỉ là thông tin, không phải lời khuyên đầu tư; vị thế của autopilot là vị thế giả lập.
