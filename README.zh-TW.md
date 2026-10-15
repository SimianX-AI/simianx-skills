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
  一個技能，就能讓 Claude Code、Codex、Cursor、Copilot、Gemini CLI 以及所有會讀取技能的 AI 代理，成為 SimianX 交易台的用戶端：
  附執行級事件日誌的 autopilot、8 代理深度研究、即時分析、已分類新聞與板塊催化劑。
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

## SimianX 涵蓋什麼

下面的一切都能透過本技能存取，並且都運行在 [simianx.ai](https://www.simianx.ai) 上；連結指向每項能力背後的產品頁面。

**市場**

- **美股與 ETF** — 13,000+ 檔上市標的，附財報、申報文件、財務數據序列與交易時段感知。週期 `1m 15m 1H 1D 1W 1mo`。→ [股票分析](https://www.simianx.ai/stocks)
- **加密貨幣** — 涵蓋 OKX、Binance、Bybit 與 Coinbase 的 1,500+ 種幣和 4,000+ 個交易對：現貨與 USDT/USD 永續合約（裸代號如 `BTC` 會解析為永續合約）。週期 `1m 5m 15m 1H 4H 1D`。→ [加密貨幣分析](https://www.simianx.ai/l)

**代理能做什麼**

- **Autopilots（自動駕駛儀）** — 四個即時代理依排程在一個標的上運行，若你允許，還會管理一個模擬部位（市價、限價與停損進場，加減碼，停損/停利，擇時閘門）。每一次分析、訊號和部位變動都會寫入事件日誌，你用游標讀取；`signal.fired` 和 `position.changed` 帶有到期時間。你的代理也可以手動操作這本帳。→ [自動駕駛儀](https://www.simianx.ai/autopilots)
- **深度研究** — 每次執行由 8 個代理組成的委員會：四位分析師（股票：fundamentals、market、news、timing · 加密：fundamentals、market、news、derivatives），一位 bull researcher（看多研究員）與一位 bear researcher（看空研究員），一位主持辯論的 research manager（研究主管），以及一位給出結論與計畫的 risk manager（風險主管）。時間跨度 `short`、`swing`、`long`；支援追問；輸出 PDF 報告。→ [深度分析](https://www.simianx.ai/c)
- **即時分析** — 四個即時代理，各執行一次：**indicator**（指標：圖表上的趨勢、動能與結構）、**intelligence**（情報：新聞流與敘事）、**fundamental**（基本面：財務與事件，幣則為鏈上與衍生品）和 **decision**（決策：附進場、停損與目標的交易提案）。→ [即時分析](https://www.simianx.ai/l)
- **已分類新聞** — 每篇文章都依其影響的標的、價值（`low` / `medium` / `high`）與情緒評分，可依清單、依單篇、依 16 種語言的譯文，或作為即時串流取得。→ [故事](https://www.simianx.ai/stories)
- **Market Pulse（市場脈搏）** — 1 分鐘、5 分鐘與 15 分鐘視窗內的價格衝擊，24 小時 / 30 日 / 52 週高低點，日內波動與跳空，涵蓋加密貨幣與股票，嚴重度 1–4。→ [市場脈搏](https://www.simianx.ai/pulse)
- **Sector Watch（板塊觀察）** — 一個板塊的第一手來源催化劑：行事曆（PDUFA 日期、諮詢委員會、試驗數據公布）、帶嚴重度 1–4 與方向的事件（核准、完整回覆函、頂線結果、資格認定、查廠、仿單更新……）、成分股、藥物資產與追蹤。現已上線：**Biopharma · FDA approvals**（生技製藥 · FDA 核准），資料來自 SEC 申報文件、FDA 與 Federal Register 公告、ClinicalTrials.gov 和 openFDA。→ [板塊觀察](https://www.simianx.ai/sectors)
- **模型由你選** — 三個層級（`fast`、`standard`、`frontier`）和來自 7 家供應商的 50+ 個模型，付費方案可為每個代理個別設定；公開目錄以點數標價。→ [點數與費率](https://www.simianx.ai/points)
- **排行榜** — 每個模型實際的交易表現，讓代理可以憑證據選擇決策模型。→ [加密貨幣AI模型排行榜](https://www.simianx.ai/crypto-leaderboard)

**方案與語言** — Free、Starter、Plus 與 Pro 方案，含每月點數、依方案的速率限制，Plus 以下有 30 分鐘資料延遲（[價格](https://www.simianx.ai/pricing)）。API 以 16 種語言回應（`X-Language`）。SimianX 不操作真實帳戶：autopilot 的部位都是模擬部位，你可以用自己的執行器鏡像執行。

## 一句話安裝

把這句話貼給你的 AI 代理。它會抓取安裝指南，把技能放到你的代理讀取技能的位置，並向你索取一把金鑰：

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

偏好用指令？以下兩種方式對所有會讀取技能的代理都適用：

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

接著對代理說 **"幫我登入 SimianX"**。代理會給你一個在瀏覽器裡批准的連結，或寄給你一組 6 位數驗證碼；無論哪種方式，它都會拿到一把專屬於它、帶有範圍與預算的金鑰，並存成 `SIMIANX_API_KEY`。還沒有帳戶？電子郵件驗證碼會順帶建立一個。你也可以在 [simianx.ai](https://www.simianx.ai) 的 **我的帳戶 → API 金鑰** 手動建立一把金鑰並匯出：

```bash
export SIMIANX_API_KEY=simx_live_...
```

## 為你的代理安裝

| 代理 | 原生安裝方式 | 技能安裝位置 |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills`，接著 `/plugin install simianx@simianx` | 外掛，或 `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills`，接著 `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills`（或 `npx skills add SimianX-AI/simianx-skills -a cursor`） | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline`（或 `-a roo`、`-a kilo`） | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| 其他任何代理 | 把 `skills/simianx/` 複製到你的代理掃描的目錄，或執行 `scripts/install.sh --agent auto` | 見 [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) 列出了每個用戶端對應的確切目錄與 shell 指令；`scripts/install.sh`（或 `install.py`；Windows 上用 `install.ps1`）會偵測已安裝的代理，並為你複製或連結技能。

## 你的代理能做什麼

| 需求 | 呼叫 | 參考 |
|---|---|---|
| 在一檔股票或一枚幣上啟動並追蹤 autopilot | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| 手動操作 autopilot 的模擬帳本 | `POST /v1/autopilots/{id}/actions`（`open`、`add`、`reduce`、`close`、`set_levels`、`place_order`、`replace_order`、`cancel_order`、`set_timeframe`） | [autopilots](skills/simianx/references/autopilots.md) |
| 立即執行一個代理 | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| 附結論與計畫的 8 代理深度研究 | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| 執行一次即時代理 | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 已分類新聞（標的、價值、情緒），清單或串流 | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| 板塊催化劑：行事曆、事件、成分股、追蹤 | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| 加密貨幣 K 線、指標、報價、市場脈搏 | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| 每個代理可設定的模型、價格、你的帳戶 | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

autopilot 日誌中的每個事件都帶有游標；對於代理可能據此行動的事件（`signal.fired`、`position.changed`），還帶有到期時間戳記，因此執行器永遠不會依過時資訊行動。讀取事件免費；你只為分析付費，用的是你的方案本來就包含的點數。

## 第一次會話

1. `GET https://service.simianx.ai/v1/skill` — 公開端點；確認你的代理持有的技能版本仍被接受。
2. `GET /v1/me`，帶上 `Authorization: Bearer $SIMIANX_API_KEY` — 方案、剩餘點數、限額。
3. `POST /v1/analysis/quote` — 付費前先看一次呼叫要花多少。
4. `POST /v1/autopilots`，請求內容為 `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — 接著從回應傳回的游標開始長輪詢事件日誌。

完整流程的 `curl` 版本在 [examples/curl](examples/curl)；一個小型常駐執行器（每次持倉變動時執行你的指令或 webhook）在 [examples/runner](examples/runner)。

## 點數，而不是額度

- 一切都以帳戶訂閱中的**點數**計費。沒有儲值，也沒有按次付費。
- AI 端點依實際使用的模型計量；`GET /v1/pricing` 公布各層級（`fast`、`standard`、`frontier`）的一般費用，`GET /v1/models` 公布代理可選的每個模型的價格。
- 資料端點按請求計價（不到一點）；事件日誌、`/v1/me`、`/v1/skill`、`/v1/pricing` 與 `/v1/models` 不收費。
- `402` 表示點數或金鑰預算已用完，並會指明出路（`renew_now`、`change_plan`、`subscribe`）；`429` 是速率限制，附有 `Retry-After`。除此之外，任何其他回應都不是付款問題。

## 安全性

- 金鑰存放在 `SIMIANX_API_KEY` 環境變數中。技能絕不會要求代理把它寫進儲存庫、日誌或提示詞。
- 代理永遠不會取得網站的登入工作階段。從代理登入（瀏覽器連結或電子郵件驗證碼）只會為該代理建立一把 API 金鑰，並以電子郵件通知你、列在你的安全活動中；網站、帳單與安全設定仍由你掌控。
- 金鑰帶有範圍（`data:read`、`analysis:run`、`automation:manage`、`keys:manage`）、每日與每月點數預算、單次呼叫上限，以及可選的 IP 允許清單。給代理一把剛好夠用的最小金鑰。
- 在 **我的帳戶 → API 金鑰** 可隨時撤銷任何金鑰；被撤銷的金鑰會在一秒內被拒絕。每次呼叫都會連同費用記錄在你的帳戶下。
- 技能只讀取你自己的帳戶：你的 autopilot、你的執行、你的金鑰。它絕不會操作真實帳戶；autopilot 持倉都是模擬持倉。

## 版本與更新

技能透過 `X-SimianX-Skill` 標頭回報自己的版本。當 API 不再接受某個版本時，會回覆 `426` 並附上需要重新讀取的 URL；`GET /v1/skill` 永遠顯示目前版本與最低版本，以及[更新日誌](CHANGELOG.md)。用你的代理自己的指令更新（`npx skills update`、`gh skill update --all`、`/plugin marketplace update simianx`……），或重新執行上面那句話。

## 儲存庫結構

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

## 回饋與支援

- 來自代理：`POST /v1/feedback`（由團隊閱讀；辱罵性文字會被拒絕且絕不儲存）。
- 來自個人：技能相關請到 [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues)，產品相關請到 [simianx.ai/agents](https://www.simianx.ai/agents)。

提交 pull request 前請先閱讀 [CONTRIBUTING.md](CONTRIBUTING.md)；回報漏洞請參閱 [SECURITY.md](SECURITY.md)。

## 授權條款

本儲存庫中的所有內容均採用 MIT 授權。使用 SimianX API 受[服務條款](https://www.simianx.ai/legal/terms)約束。SimianX 的分析僅為資訊，不構成投資建議；autopilot 持倉都是模擬持倉。
