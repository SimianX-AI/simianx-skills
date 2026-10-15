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
  四个 AI 分析师同时看任何一只美股或加密交易对，再加一条打好分的新闻流，
  给 Claude Code、Codex、Cursor 和所有能读 skill 的智能体直接用。
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
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

它会把 skill 装进你的智能体读取 skill 的目录，然后帮你登录：在浏览器里批准一个链接，或者输入我们发到你邮箱的 6 位验证码。新邮箱当场就开好账户。智能体最后拿到的是一把只属于它自己的 API key，放在 `SIMIANX_API_KEY` 里，你的网站登录它碰不到。

想用终端也可以：

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

每个智能体（Claude Code、Codex、Cursor、Copilot、Gemini CLI、Windsurf、Amp、Cline 等）各自的命令和目录，都在 [INSTALL.md](INSTALL.md) 里。

## 先从这几个调用开始

| 做什么 | 调用 | 文档 |
|---|---|---|
| 跑一次实时分析 | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 看某个标的的新闻 | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| 新闻一到就收到 | `GET /v1/news/stream`（SSE，断线可续） | [news](skills/simianx/references/news.md) |
| 市场脉搏 | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| 深度研究 | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| 板块观察 | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| 自动驾驶仪 | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL 是 `https://service.simianx.ai/v1`，请求头带 `Authorization: Bearer $SIMIANX_API_KEY`。同样的调用写成了 shell 脚本，放在 [examples/curl](examples/curl)。

## 套餐

Free、Starter、Plus 和 Pro，详见[价格](https://www.simianx.ai/pricing)。智能体调用用的是你套餐里的点数，费率和网站上一样。新闻流在 Plus 和 Pro 上是实时的，Plus 以下的新闻会晚 30 分钟。回答支持 16 种语言。SimianX 从不动真实账户，自动驾驶仪的仓位都是模拟仓位。

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
skills/simianx/references/        live · news · data · deep · sectors · autopilots · billing
INSTALL.md                        agent-readable install guide (also at simianx.ai/INSTALL.md)
scripts/install.{sh,py,ps1}       installer for every agent; check_version.py · check_readmes.py
examples/curl · examples/runner   the first calls in curl; an always-on runner for autopilots
.claude-plugin · .agents/plugins · .cursor-plugin · plugin.json · gemini-extension.json
                                  manifests so marketplaces and plugin commands find the skill
README.<locale>.md                this page in the 16 languages SimianX speaks
```

## 反馈

- 智能体：`POST /v1/feedback`。
- 人：skill 的问题提到 [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues)，产品相关的到 [simianx.ai/agents](https://www.simianx.ai/agents)。

提 pull request 之前请先读 [CONTRIBUTING.md](CONTRIBUTING.md)；报告安全漏洞请看 [SECURITY.md](SECURITY.md)。

## 许可

本仓库所有内容采用 MIT 许可。使用 SimianX API 须遵守[服务条款](https://www.simianx.ai/legal/terms)。SimianX 的分析只是信息，不是投资建议。
