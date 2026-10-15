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
  Bốn nhà phân tích AI cho mọi cổ phiếu Mỹ hay cặp crypto, kèm một luồng tin tức đã chấm điểm,
  dùng ngay trong Claude Code, Codex, Cursor và mọi agent khác biết đọc skill.
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

## SimianX làm được gì

Phần việc chính nằm ở hai tính năng này.

- **Phân tích đa agent trực tiếp.** Chọn một cổ phiếu hoặc cặp crypto cùng khung thời gian, bốn agent sẽ phân tích cùng lúc. Agent Chỉ báo đọc biểu đồ. Agent Tình báo đọc dòng tin tức. Agent Cơ bản đọc hồ sơ công bố và giao dịch nội bộ, hoặc dữ liệu on-chain và phái sinh nếu là coin. Agent Quyết định cân nhắc cả ba rồi đề xuất giao dịch kèm điểm vào, cắt lỗ và mục tiêu. → [Phân tích trực tiếp](https://www.simianx.ai/l)
- **Luồng tin tức đã chấm điểm.** Mỗi bài viết đến nơi đều đã được gắn các mã mà nó tác động, điểm giá trị và nhận định tăng, giảm hay trung lập. Đây là luồng tin đứng sau Nhịp Thị Trường, nơi tin tức hiện cạnh các cú biến động giá đột ngột, các đỉnh đáy mới và khoảng trống giá. Agent của bạn có thể đọc lần lượt từng trang hoặc giữ một luồng mở cho các mã của nó. → [Nhịp Thị Trường](https://www.simianx.ai/pulse)

Khi cần, còn có:

- **Nghiên cứu chuyên sâu.** Tám agent tranh luận về một cổ phiếu hay một coin, rồi trả về kết luận, kế hoạch giao dịch và một file PDF. Agent của bạn có thể hỏi thêm. → [Phân tích chuyên sâu](https://www.simianx.ai/c)
- **Theo dõi ngành.** Lịch chất xúc tác và sự kiện lấy từ nguồn gốc, bắt đầu với dược sinh học. → [Theo dõi ngành](https://www.simianx.ai/sectors)
- **Lái tự động.** Vẫn bốn agent trực tiếp đó, chạy theo lịch cho một mã, kèm một vị thế giả lập và nhật ký sự kiện để agent của bạn theo dõi. → [Thiết bị lái tự động](https://www.simianx.ai/autopilots)
- **Tự chọn mô hình.** Chọn mô hình cho từng agent, và xem trước mỗi mô hình đã giao dịch ra sao. → [Bảng xếp hạng mô hình](https://www.simianx.ai/crypto-leaderboard)

Thị trường: 13.000+ cổ phiếu và ETF Mỹ với nến từ `1m` đến `1mo`, và 4.000+ cặp crypto, cả spot lẫn hợp đồng vĩnh cửu, với nến từ `1m` đến `1D`. → [Phân tích cổ phiếu](https://www.simianx.ai/c) · [Phân tích tiền điện tử](https://www.simianx.ai/l)

## Cài đặt bằng một câu

Dán câu này vào agent của bạn:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Agent sẽ đặt skill vào đúng nơi nó tìm skill, rồi giúp bạn đăng nhập: bạn phê duyệt một liên kết trong trình duyệt, hoặc nhập mã 6 chữ số chúng tôi gửi qua email. Email mới sẽ được tạo tài khoản ngay. Cuối cùng agent có một khóa API của riêng nó trong `SIMIANX_API_KEY`, và không bao giờ có thông tin đăng nhập website của bạn.

Hoặc cài từ terminal:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

Lệnh và thư mục cho từng agent (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline và các agent khác) có trong [INSTALL.md](INSTALL.md).

## Các lệnh gọi đầu tiên

| Việc cần làm | Lệnh gọi | Tài liệu |
|---|---|---|
| Chạy phân tích trực tiếp một lần | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Tin tức về các mã của bạn | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| Nhận tin ngay khi có | `GET /v1/news/stream` (server-sent events, nối tiếp được khi mất kết nối) | [news](skills/simianx/references/news.md) |
| Nhịp Thị Trường | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Nghiên cứu chuyên sâu | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Theo dõi ngành | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Lái tự động | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL là `https://service.simianx.ai/v1`, header `Authorization: Bearer $SIMIANX_API_KEY`. Các lệnh gọi trên đã viết sẵn thành script shell trong [examples/curl](examples/curl).

## Gói

Free, Starter, Plus và Pro, xem [bảng giá](https://www.simianx.ai/pricing). Lệnh gọi từ agent dùng điểm trong gói của bạn, theo cùng đơn giá như trên website. Luồng tin tức là thời gian thực trên Plus và Pro; dưới Plus, tin tức chậm 30 phút. Câu trả lời có sẵn bằng 16 ngôn ngữ. SimianX không bao giờ giao dịch trên tài khoản thật: vị thế của lái tự động là vị thế giả lập.

## Bảo mật

- Khóa chỉ nằm trong `SIMIANX_API_KEY`. Skill không bao giờ ghi nó vào repository, log hay prompt.
- Agent không bao giờ có phiên đăng nhập website. Đăng nhập từ agent chỉ tạo một khóa API cho agent đó, và chúng tôi gửi email báo cho bạn mỗi khi việc này xảy ra.
- Khóa có phạm vi quyền (scope), ngân sách theo ngày và theo tháng, và danh sách IP cho phép nếu cần. Hãy cấp cho mỗi agent khóa hẹp nhất mà vẫn đủ cho việc của nó.
- Thu hồi khóa tại **Tài khoản của tôi → Khóa API**, khóa sẽ ngừng hoạt động trong vòng một giây.

## Phiên bản

Skill gửi phiên bản của mình trong header `X-SimianX-Skill`. Khi một phiên bản bị ngừng hỗ trợ, API trả về `426` kèm URL cần đọc lại, còn `GET /v1/skill` cho biết phiên bản hiện tại và phiên bản tối thiểu. Cập nhật bằng lệnh riêng của agent, hoặc dán lại câu ở trên. Những gì đã thay đổi có trong [nhật ký thay đổi](CHANGELOG.md).

## Cấu trúc repository

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

## Góp ý

- Từ agent: `POST /v1/feedback`.
- Từ người dùng: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) cho skill, [simianx.ai/agents](https://www.simianx.ai/agents) cho sản phẩm.

Đọc [CONTRIBUTING.md](CONTRIBUTING.md) trước khi mở pull request, và [SECURITY.md](SECURITY.md) để báo cáo lỗ hổng bảo mật.

## Giấy phép

Mọi thứ trong repository này theo giấy phép MIT. Việc sử dụng SimianX API tuân theo [Điều khoản dịch vụ](https://www.simianx.ai/legal/terms). Phân tích của SimianX là thông tin, không phải lời khuyên đầu tư.
