<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">為 AI 代理打造的 SimianX AI</h1>

<p align="center">
  四位 AI 分析師同時盯著任一檔美股或加密貨幣交易對，再加上一條附評分的新聞串流，
  給 Claude Code、Codex、Cursor 和所有能讀 skill 的 AI 代理直接使用。
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">更新日誌</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <b>繁體中文</b> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## SimianX 能做什麼

最常用的是這兩項。

- **多智能體即時分析。** 選一檔股票或一個加密貨幣交易對，再選個週期，四個智能體就同時開始分析。指標智能體看線圖，情報智能體追新聞動態，基本面智能體看財報和內部人交易（換成幣就看鏈上和衍生品數據），決策智能體綜合三方的判讀，提出附進場、停損和目標價的交易方案。→ [即時分析](https://www.simianx.ai/l)
- **附評分的新聞串流。** 每篇文章進來時，會影響哪些標的、價值高低、偏多偏空還是中性，都已經標好了。市場脈搏用的就是這條串流，和價格異動、創新高新低、跳空排在一起。你的代理可以翻頁讀，也可以針對自己關注的標的一直開著串流。→ [市場脈搏](https://www.simianx.ai/pulse)

需要的時候也有這些：

- **深度研究。** 八個智能體針對一檔股票或一個幣來回辯論，最後交出結論、交易計畫和一份 PDF，你的代理還能接著追問。→ [深度分析](https://www.simianx.ai/c)
- **板塊觀察。** 從第一手來源整理出的催化劑行事曆和事件，先從生技製藥做起。→ [板塊觀察](https://www.simianx.ai/sectors)
- **自動駕駛儀。** 同樣是那四個即時智能體，按排程盯住一個標的，順手管理一筆模擬部位；每一步都寫進事件日誌，你的代理可以一路跟著讀。→ [自動駕駛儀](https://www.simianx.ai/autopilots)
- **模型自己選。** 每個智能體背後用哪個模型由你決定，選之前還能先看看各個模型實際交易的成績。→ [模型排行榜](https://www.simianx.ai/crypto-leaderboard)

市場：13,000+ 檔美股和 ETF，K 線從 `1m` 到 `1mo`；4,000+ 個加密貨幣交易對，現貨和永續合約都有，K 線從 `1m` 到 `1D`。→ [股票分析](https://www.simianx.ai/c) · [加密貨幣分析](https://www.simianx.ai/l)

## 一句話安裝

把這句話貼給你的代理：

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

它會把 skill 裝進你的代理讀取 skill 的目錄，再帶你登入：在瀏覽器裡核准一個連結，或輸入我們寄到你信箱的 6 位數驗證碼。新的信箱會當場開好帳戶。代理最後拿到的是一把專屬於它的 API 金鑰，存在 `SIMIANX_API_KEY` 裡，你的網站登入它碰不到。

想用終端機也可以：

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

各個代理（Claude Code、Codex、Cursor、Copilot、Gemini CLI、Windsurf、Amp、Cline 等）的指令和安裝目錄，都在 [INSTALL.md](INSTALL.md) 裡。

## 先從這幾個呼叫開始

| 用途 | 呼叫 | 文件 |
|---|---|---|
| 跑一次即時分析 | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 查標的相關新聞 | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| 新聞一到就收到 | `GET /v1/news/stream`（SSE，斷線可接續） | [news](skills/simianx/references/news.md) |
| 市場脈搏 | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| 深度研究 | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| 板塊觀察 | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| 自動駕駛儀 | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL 是 `https://service.simianx.ai/v1`，請求標頭帶上 `Authorization: Bearer $SIMIANX_API_KEY`。同樣的呼叫也寫成了 shell 腳本，放在 [examples/curl](examples/curl)。

## 方案

Free、Starter、Plus 和 Pro，詳見[價格](https://www.simianx.ai/pricing)。代理發出的呼叫用的是你方案裡的點數，費率和網站相同。Plus 和 Pro 的新聞串流是即時的，Plus 以下的新聞會延遲 30 分鐘。回答支援 16 種語言。SimianX 從不操作真實帳戶，自動駕駛儀的部位都是模擬部位。

## 安全性

- 金鑰只放在 `SIMIANX_API_KEY`，skill 絕不會把它寫進儲存庫、日誌或提示詞。
- 代理永遠拿不到網站的登入工作階段。從代理登入只會替它建立一把 API 金鑰，同時寄信通知你。
- 金鑰可以限定權限範圍、設定每日和每月預算，還能加上 IP 允許清單。每個代理給一把剛好夠用的金鑰就好。
- 在 **我的帳戶 → API 金鑰** 撤銷金鑰，一秒內就會失效。

## 版本

skill 會在 `X-SimianX-Skill` 標頭帶上自己的版本。某個版本停用後，API 會回傳 `426` 並附上要重新讀取的網址；`GET /v1/skill` 可以查到目前版本和最低版本。用你的代理自己的指令更新，或把上面那句話再貼一次。改了哪些地方請看[更新日誌](CHANGELOG.md)。

## 儲存庫結構

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

## 回饋

- 代理：`POST /v1/feedback`。
- 人：skill 的問題請到 [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues)，產品相關請到 [simianx.ai/agents](https://www.simianx.ai/agents)。

送出 pull request 之前請先讀 [CONTRIBUTING.md](CONTRIBUTING.md)；回報安全漏洞請見 [SECURITY.md](SECURITY.md)。

## 授權

本儲存庫的所有內容皆採 MIT 授權。使用 SimianX API 須遵守[服務條款](https://www.simianx.ai/legal/terms)。SimianX 的分析只是資訊，不構成投資建議。
