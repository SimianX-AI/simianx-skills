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
  给任何 AI agent 配一整个投研团队。装上 SimianX AI，你的 agent 就能对任意美股或加密交易对召开 8 个 agent 的投研委员会并继续追问，拿到四个实时 agent 给出的入场、止损和目标价，还能在你关注的标的上开着一条评分新闻流。一个 skill 加一个远程 MCP 服务器，适用于 Claude Code、Codex、Cursor、Muse、Grok Bot、dots 以及其他所有 agent。
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

## 为什么要给 agent 装上 SimianX

单独问一个 agent *“NVDA 现在适合做波段吗？”*，它只会搜一遍网页，总结一些可能已经过时好几天的标题，再给出一个模型的看法。它没有实时图表，没有人站在对立面反驳，对话一结束就停了。

装上 SimianX 之后，同一个 agent：

| | 只有 agent 自己 | 装了 SimianX AI |
|---|---|---|
| 谁在分析 | 一个模型 | 8 个 agent 的委员会：四位分析师、多头和空头研究员、研究经理、风控经理 |
| 读什么 | 网页搜索结果 | 实时 K 线、财报文件、内部人交易、新闻流；币则读链上和衍生品数据 |
| 你拿到什么 | 一个观点 | 带入场、止损和目标价的结论，外加 PDF 报告 |
| 之后 | 从头再来 | 把追问交给同一个委员会，或设一个自动驾驶仪持续盯着 |

## 你可以这样问

装好之后，用你自己的话问就行：

- *“对 NVDA 召开 SimianX 委员会，看看适不适合做波段。”* 四位分析师汇报，多空研究员辩论，风控经理给出结论、交易计划和 PDF。
- *“问问空头研究员，什么情况会证明多头的逻辑是错的。”* 追问进入同一次分析，回答建立在委员会已经读过的全部材料上。
- *“用短线视角对 SOL 跑一次委员会。”* 分析币的时候，分析师还会读链上资金流和衍生品市场。
- *“BTC 现在 15 分钟图怎么样？”* 四个实时 agent 作答，由决策 agent 给出买入、卖出还是观望，以及入场、止损和目标价。
- *“TSLA 或 ETH 一有高价值新闻就告诉我。”* 你关注标的的评分新闻流，每条新闻一评完分就送到。
- *“在 1 小时图上盯着 AAPL，并管理一个模拟仓位。”* 自动驾驶仪在每根 K 线收盘时重跑 agent，并记录每个信号。
- *“未来 30 天有哪些生物医药 PDUFA 日期？”* 板块观察，数据来自一手来源。
- *“过去一小时加密市场有什么大幅波动？”* 市场脉搏：价格急动、新高新低、放量和跳空。

免费账户可以用 NVDA、AAPL、TSLA、BTC、ETH 等热门标的体验委员会。

## SimianX 能做什么

最常用的是这两样。

- **多智能体实时分析。** 选一只股票或一个加密交易对，再选个周期，四个智能体同时开始看。指标智能体看图表，情报智能体看新闻流，基本面智能体看财报和内部人交易（换成币就看链上和衍生品数据），决策智能体把三份意见合在一起，给出带入场、止损和目标的交易方案。→ [实时分析](https://www.simianx.ai/l)
- **打好分的新闻流。** 每篇文章进来时，影响哪些标的、价值高低、偏多偏空还是中性，都已经标好了。市场脉搏用的就是这条新闻流，和价格异动、新高新低、跳空排在一起。你的智能体可以翻页读，也可以盯着自己关心的标的一直挂着流。→ [市场脉搏](https://www.simianx.ai/pulse)

需要的时候也有：

- **深度研究。** 八个智能体围着一只股票或一个币来回辩论，最后交出结论、交易计划和一份 PDF，之后还能接着追问。→ [深度分析](https://www.simianx.ai/c)
- **板块观察。** 从一手来源整理出的催化剂日历和事件，先从生物医药做起。→ [板块观察](https://www.simianx.ai/sectors)
- **自动驾驶仪。** 还是那四个实时智能体，按计划盯住一个标的，顺手管一笔模拟仓位；每一步都记进事件日志，你的智能体可以一路跟着读。→ [自动驾驶仪](https://www.simianx.ai/autopilots)
- **模型自己选。** 每个智能体背后用哪个模型由你定，选之前还能先看看各个模型实际交易得怎么样。→ [模型排行榜](https://www.simianx.ai/crypto-leaderboard)

市场：13,000+ 只美股和 ETF，K 线从 `1m` 到 `1mo`；4,000+ 个加密交易对，现货和永续都有，K 线从 `1m` 到 `1D`。→ [股票分析](https://www.simianx.ai/c) · [加密货币分析](https://www.simianx.ai/l)

## 一句话安装

把这句话发给你的智能体：

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and sign me in.
```

它会把 skill 装进你的智能体读取 skill 的目录，然后帮你登录：在浏览器里批准一个链接，或者输入我们发到你邮箱的 6 位验证码。新邮箱当场就开好账户。智能体最后拿到的是一把只属于它自己的 API key，放在 `SIMIANX_API_KEY` 里，你的网站登录它碰不到。

想用终端也可以：

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

每个智能体（Claude Code、Codex、Cursor、Copilot、Gemini CLI、Windsurf、Amp、Cline 等）各自的命令和目录，都在 [INSTALL.md](INSTALL.md) 里。

### Muse、Grok Bot、dots 等自带电脑的 agent

运行在自己云端电脑上的 agent 读的是同一句话。它们通过 MCP 接入，或者用 [OpenAPI 文档](https://service.simianx.ai/v1/openapi.json) 建一个连接器，帮你登录，把 key 存进自己的凭据库，再把 SimianX 存成技能。对 Muse、Grok Bot 和 dots 具体怎么说，见 [INSTALL.md](INSTALL.md#agents-with-their-own-computer-muse-grok-bot-dots)。

### 或者通过 MCP 连接

支持 MCP 的 AI 智能体不用装 skill，就能把 SimianX 当工具用。用你的 key 添加一次远程服务器：

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

Claude Desktop、Cursor、Codex、VS Code、Windsurf、Gemini CLI、Grok Bot 和 Muse 的写法见 [INSTALL.md](INSTALL.md#connect-over-mcp)。注册表名称：`io.github.SimianX-AI/simianx`。

## 先从这几个调用开始

| 做什么 | 调用 | 文档 |
|---|---|---|
| 实时分析会话（每根 K 线收盘） | `POST /v1/live/sessions` → the WebSocket, or `GET /v1/updates?wait=30` | [live](skills/simianx/references/live.md) |
| 快速研判（一次） | `POST /v1/analysis/quick` → `GET /v1/updates?wait=30` | [quick](skills/simianx/references/quick.md) |
| 用户还没听到的所有更新 | `GET /v1/updates?ack=<id>&wait=30` | [following](skills/simianx/references/following.md) |
| 看某个标的的新闻 | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| 新闻一到就收到 | `GET /v1/news/stream`（SSE，断线可续） | [news](skills/simianx/references/news.md) |
| 市场脉搏 | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| 深度研究 | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| 板块观察 | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| 自动驾驶仪 | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL 是 `https://service.simianx.ai/v1`，请求头带 `Authorization: Bearer $SIMIANX_API_KEY`。同样的调用写成了 shell 脚本，放在 [examples/curl](examples/curl)。

## 套餐

Free、Starter、Plus 和 Pro，详见[价格](https://www.simianx.ai/pricing)。智能体调用用的是你套餐里的点数，费率和网站上一样。新闻流在 Plus 和 Pro 上是实时的，Plus 以下的新闻会晚 30 分钟。回答支持 16 种语言。

你可以通过 SimianX API 将分析和信号接入自己的交易系统，在你授权的券商或交易所执行真实交易。SimianX 平台内记录的仓位是模拟仓位；真实订单由你接入的系统在自己的账户中提交和管理。

## 安全

- key 只放在 `SIMIANX_API_KEY` 里，skill 绝不会把它写进代码仓库、日志或提示词。
- 智能体永远拿不到网站会话。从智能体登录只会为它生成一把 API key，同时会发邮件通知你。
- key 可以限定权限范围、每日和每月预算，还能加 IP 白名单。给每个智能体刚好够用的那把 key。
- 在 **我的账户 → API 密钥** 撤销 key，一秒之内就失效。

## 版本

skill 会在 `X-SimianX-Skill` 请求头里带上自己的版本。某个版本停用后，API 返回 `426` 并附上要重新读取的地址；`GET /v1/skill` 可以看到当前版本和最低版本。用你的智能体自带的更新命令升级，或者把上面那句话再发一次。具体改了什么见[更新日志](CHANGELOG.md)。

## 仓库结构

```
skills/simianx/SKILL.md           the skill (Agent Skills format)
skills/simianx/references/        following · live · quick · deep · news · autopilots · data · sectors · developers · billing
INSTALL.md                        agent-readable install guide (also at simianx.ai/INSTALL.md)
scripts/install.{sh,py,ps1}       installer for every agent; check_version.py · check_readmes.py
examples/curl · examples/runner   the first calls in curl; an always-on runner for autopilots
.claude-plugin · .agents/plugins · .cursor-plugin · plugin.json · gemini-extension.json
                                  manifests so marketplaces and plugin commands find the skill
server.json                       MCP Registry entry for the remote MCP server (service.simianx.ai/v1/mcp)
README.<locale>.md                this page in the 16 languages SimianX speaks
```

## 反馈

- 智能体：`POST /v1/feedback`。
- 人：skill 的问题提到 [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues)，产品相关的到 [simianx.ai/agents](https://www.simianx.ai/agents)。

提 pull request 之前请先读 [CONTRIBUTING.md](CONTRIBUTING.md)；报告安全漏洞请看 [SECURITY.md](SECURITY.md)。

## 许可

本仓库所有内容采用 MIT 许可。使用 SimianX API 须遵守[服务条款](https://www.simianx.ai/legal/terms)。SimianX 的分析只是信息，不是投资建议。
