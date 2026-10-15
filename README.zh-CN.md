<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">面向 AI 智能体的 SimianX AI</h1>

<p align="center">
  一个技能，就能让 Claude Code、Codex、Cursor、Copilot、Gemini CLI 以及所有会读取技能的智能体，成为 SimianX 交易台的客户端：
  带执行级事件日志的 autopilot、8 智能体深度研究、实时分析、分类新闻与板块催化剂。
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">更新日志</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <b>简体中文</b> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## SimianX 覆盖什么

下面的一切都能通过本技能访问，并且都运行在 [simianx.ai](https://www.simianx.ai) 上；链接指向每项能力背后的产品页面。

**市场**

- **美股与 ETF** — 13,000+ 只上市标的，附带财报、申报文件、财务数据序列与交易时段感知。周期 `1m 15m 1H 1D 1W 1mo`。→ [股票分析](https://www.simianx.ai/stocks)
- **加密货币** — 覆盖 OKX、Binance、Bybit 与 Coinbase 的 1,500+ 种币和 4,000+ 个交易对：现货与 USDT/USD 永续合约（裸符号如 `BTC` 会解析为永续合约）。周期 `1m 5m 15m 1H 4H 1D`。→ [加密货币分析](https://www.simianx.ai/l)

**智能体能做什么**

- **Autopilots（自动驾驶仪）** — 四个实时智能体按计划在一个标的上运行，若你允许，还会管理一个模拟仓位（市价、限价与止损入场，加减仓，止损/止盈，择时闸门）。每一次分析、信号和仓位变化都会写入事件日志，你用游标读取；`signal.fired` 和 `position.changed` 带有过期时间。你的智能体也可以手动操作这本账。→ [自动驾驶仪](https://www.simianx.ai/autopilots)
- **深度研究** — 每次运行由 8 个智能体组成的委员会：四位分析师（股票：fundamentals、market、news、timing · 加密：fundamentals、market、news、derivatives），一位 bull researcher（看多研究员）与一位 bear researcher（看空研究员），一位主持辩论的 research manager（研究主管），以及一位给出结论与计划的 risk manager（风险主管）。时间跨度 `short`、`swing`、`long`；支持追问；输出 PDF 报告。→ [深度分析](https://www.simianx.ai/c)
- **实时分析** — 四个实时智能体，各运行一次：**indicator**（指标：图表上的趋势、动量与结构）、**intelligence**（情报：新闻流与叙事）、**fundamental**（基本面：财务与事件，币则为链上与衍生品）和 **decision**（决策：带入场、止损与目标的交易提案）。→ [实时分析](https://www.simianx.ai/l)
- **分类新闻** — 每篇文章都按其影响的标的、价值（`low` / `medium` / `high`）与情绪打分，可按列表、按单篇、按 16 种语言的译文，或作为实时流获取。→ [故事](https://www.simianx.ai/stories)
- **Market Pulse（市场脉搏）** — 1 分钟、5 分钟与 15 分钟窗口内的价格冲击，24 小时 / 30 日 / 52 周高低点，日内波动与跳空，覆盖加密货币与股票，严重度 1–4。→ [市场脉搏](https://www.simianx.ai/pulse)
- **Sector Watch（板块观察）** — 一个板块的一手来源催化剂：日历（PDUFA 日期、咨询委员会、试验数据公布）、带严重度 1–4 与方向的事件（获批、完整回复函、顶线结果、资格认定、现场检查、标签更新……）、成分股、药物资产与关注。现已上线：**Biopharma · FDA approvals**（生物医药 · FDA 审批），数据来自 SEC 申报文件、FDA 与 Federal Register 公告、ClinicalTrials.gov 和 openFDA。→ [板块观察](https://www.simianx.ai/sectors)
- **模型由你选** — 三个档位（`fast`、`standard`、`frontier`）和来自 7 家供应商的 50+ 个模型，付费套餐可为每个智能体单独设置；公开目录以点数标价。→ [点数与费率](https://www.simianx.ai/points)
- **排行榜** — 每个模型真实的交易表现，让智能体可以凭证据选择决策模型。→ [加密货币AI模型排行榜](https://www.simianx.ai/crypto-leaderboard)

**套餐与语言** — Free、Starter、Plus 和 Pro 套餐，含每月点数、按套餐的限流，Plus 以下有 30 分钟数据延迟（[价格](https://www.simianx.ai/pricing)）。API 以 16 种语言应答（`X-Language`）。SimianX 不操作真实账户：autopilot 的仓位都是模拟仓位，你可以用自己的运行器镜像执行。

## 一句话安装

把这句话粘贴给你的智能体。它会获取安装指南，把技能放到你的智能体读取技能的位置，并向你索取一个密钥：

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

更喜欢用命令？以下两种方式对所有会读取技能的智能体都适用：

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

然后对智能体说 **"帮我登录 SimianX"**。它会给你一个在浏览器里批准的链接，或者给你的邮箱发一个 6 位验证码；无论哪种方式，它都会拿到一把专属于它、带作用域和预算的密钥，并把它存为 `SIMIANX_API_KEY`。还没有账号？邮箱验证码会自动创建一个。你也可以在 [simianx.ai](https://www.simianx.ai) 的 **我的账户 → API 密钥** 手动创建一个密钥并导出：

```bash
export SIMIANX_API_KEY=simx_live_...
```

## 为你的智能体安装

| 智能体 | 原生安装方式 | 技能落地位置 |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills`，然后 `/plugin install simianx@simianx` | 插件，或 `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills`，然后 `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills`（或 `npx skills add SimianX-AI/simianx-skills -a cursor`） | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline`（或 `-a roo`、`-a kilo`） | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| 其他任何智能体 | 把 `skills/simianx/` 复制到你的智能体扫描的目录，或运行 `scripts/install.sh --agent auto` | 见 [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) 列出了每个客户端对应的具体目录和 shell 命令；`scripts/install.sh`（或 `install.py`；Windows 上用 `install.ps1`）会检测已安装的智能体，并为你复制或链接技能。

## 你的智能体能做什么

| 需求 | 调用 | 参考 |
|---|---|---|
| 在一只股票或一个币上启动并跟踪 autopilot | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| 手动操作 autopilot 的模拟账本 | `POST /v1/autopilots/{id}/actions`（`open`、`add`、`reduce`、`close`、`set_levels`、`place_order`、`replace_order`、`cancel_order`、`set_timeframe`） | [autopilots](skills/simianx/references/autopilots.md) |
| 立即运行一个智能体 | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| 给出结论与计划的 8 智能体深度研究 | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| 运行一次实时智能体 | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 分类新闻（标的、价值、情绪），列表或流式 | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| 板块催化剂：日历、事件、成分股、关注 | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| 加密 K 线、指标、报价、市场脉搏 | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| 每个智能体可设置的模型、价格、你的账户 | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

autopilot 日志中的每个事件都带有游标；对于智能体可能据此行动的事件（`signal.fired`、`position.changed`），还带有过期时间戳，因此运行器永远不会基于过时信息行动。读取事件免费；你只为分析付费，用的是你的套餐本已包含的点数。

## 第一次会话

1. `GET https://service.simianx.ai/v1/skill` — 公开接口；确认你的智能体持有的技能版本仍被接受。
2. `GET /v1/me`，带上 `Authorization: Bearer $SIMIANX_API_KEY` — 套餐、剩余点数、限额。
3. `POST /v1/analysis/quote` — 付费前先看一次调用要花多少。
4. `POST /v1/autopilots`，请求体为 `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — 然后从响应返回的游标开始长轮询事件日志。

完整流程的 `curl` 版本在 [examples/curl](examples/curl)；一个小型常驻运行器（每次持仓变化时执行你的命令或 webhook）在 [examples/runner](examples/runner)。

## 点数，而不是额度

- 一切都以账户订阅中的**点数**计费。没有充值，也没有按次付费。
- AI 接口按实际使用的模型计量；`GET /v1/pricing` 公布各档位（`fast`、`standard`、`frontier`）的通常费用，`GET /v1/models` 公布智能体可选的每个模型的价格。
- 数据接口按请求计价（不到一个点）；事件日志、`/v1/me`、`/v1/skill`、`/v1/pricing` 和 `/v1/models` 不收费。
- `402` 表示点数或密钥预算已用完，并会指明出路（`renew_now`、`change_plan`、`subscribe`）；`429` 是限流，带有 `Retry-After`。除此之外，任何其他响应都不是付费问题。

## 安全

- 密钥存放在 `SIMIANX_API_KEY` 环境变量中。技能绝不会要求智能体把它写进仓库、日志或提示词。
- 智能体绝不会获得网站会话。从智能体登录（浏览器链接或邮箱验证码）只会为该智能体创建一把 API 密钥，并通过邮件通知你、记录在你的安全活动里；网站、账单和安全设置始终由你掌控。
- 密钥带有作用域（`data:read`、`analysis:run`、`automation:manage`、`keys:manage`）、每日与每月点数预算、单次调用上限，以及可选的 IP 白名单。给智能体一把刚好够用的最小密钥。
- 在 **我的账户 → API 密钥** 可随时吊销任何密钥；被吊销的密钥会在一秒内被拒绝。每次调用都会连同费用记录在你的账户下。
- 技能只读取你自己的账户：你的 autopilot、你的运行、你的密钥。它绝不会操作真实账户；autopilot 持仓都是模拟持仓。

## 版本与更新

技能通过 `X-SimianX-Skill` 请求头上报自己的版本。当 API 不再接受某个版本时，会返回 `426` 并附上需要重新读取的 URL；`GET /v1/skill` 始终显示当前版本和最低版本，以及[更新日志](CHANGELOG.md)。用你的智能体自己的命令更新（`npx skills update`、`gh skill update --all`、`/plugin marketplace update simianx`……），或重新运行上面那句话。

## 仓库结构

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

## 反馈与支持

- 来自智能体：`POST /v1/feedback`（由团队阅读；辱骂性文本会被拒绝且绝不存储）。
- 来自个人：技能相关请到 [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues)，产品相关请到 [simianx.ai/agents](https://www.simianx.ai/agents)。

提交 pull request 前请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)；报告漏洞请参阅 [SECURITY.md](SECURITY.md)。

## 许可证

本仓库中的所有内容均采用 MIT 许可。使用 SimianX API 受[服务条款](https://www.simianx.ai/legal/terms)约束。SimianX 的分析仅为信息，不构成投资建议；autopilot 持仓都是模拟持仓。
