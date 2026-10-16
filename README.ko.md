<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">AI 에이전트를 위한 SimianX AI</h1>

<p align="center">
  미국 주식이든 암호화폐 페어든 AI 분석가 네 명이 동시에 분석하고, 뉴스는 점수를 매겨 스트림으로 보냅니다.
  Claude Code, Codex, Cursor를 비롯해 스킬을 읽는 모든 에이전트에서 쓸 수 있습니다.
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">변경 이력</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <b>한국어</b> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## SimianX로 할 수 있는 일

가장 많이 쓰는 기능은 이 두 가지입니다.

- **멀티 에이전트 실시간 분석.** 주식이나 암호화폐 페어와 타임프레임을 고르면 에이전트 4개가 동시에 분석을 시작합니다. 지표 에이전트는 차트를, 정보 에이전트는 뉴스 흐름을 읽습니다. 기본적 분석 에이전트는 공시와 내부자 거래를 보고, 코인이면 온체인과 파생상품 데이터를 봅니다. 결정 에이전트는 세 분석을 종합해 진입가, 손절가, 목표가가 담긴 거래안을 내놓습니다. → [실시간 분석](https://www.simianx.ai/l)
- **점수가 매겨진 뉴스 스트림.** 모든 기사에는 영향을 주는 종목, 중요도 점수, 강세·약세·중립 판단이 붙어서 들어옵니다. 마켓 펄스의 뉴스가 바로 이 피드이고, 급등락, 신고가·신저가, 갭과 나란히 표시됩니다. 에이전트는 페이지를 넘겨 가며 읽을 수도 있고, 관심 종목에 스트림을 열어 둘 수도 있습니다. → [마켓 펄스](https://www.simianx.ai/pulse)

필요할 때 쓸 수 있는 기능도 있습니다.

- **심층 분석.** 에이전트 8개가 주식이나 코인 하나를 놓고 토론한 뒤 판정, 거래 계획, PDF를 돌려줍니다. 에이전트가 이어서 추가 질문을 할 수도 있습니다. → [심층 분석](https://www.simianx.ai/c)
- **섹터 워치.** 1차 출처에서 모은 촉매 캘린더와 이벤트입니다. 제약·바이오부터 시작했습니다. → [섹터 워치](https://www.simianx.ai/sectors)
- **오토파일럿.** 같은 실시간 에이전트 4개가 종목 하나를 정해진 일정대로 분석합니다. 모의 포지션을 관리하고, 에이전트가 따라 읽을 수 있는 이벤트 로그를 남깁니다. → [자동 조종 장치](https://www.simianx.ai/autopilots)
- **모델 선택.** 에이전트마다 쓸 모델을 고를 수 있고, 고르기 전에 모델별 실제 거래 성적을 확인할 수 있습니다. → [모델 리더보드](https://www.simianx.ai/crypto-leaderboard)

시장: 미국 주식과 ETF 13,000개 이상을 `1m`부터 `1mo`까지, 현물과 무기한을 포함한 암호화폐 페어 4,000개 이상을 `1m`부터 `1D`까지 캔들로 다룹니다. → [주식 분석](https://www.simianx.ai/c) · [암호화폐 분석](https://www.simianx.ai/l)

## 한 문장으로 설치

에이전트에게 이 문장을 붙여 넣으세요.

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

에이전트가 스킬을 읽는 위치에 스킬을 설치한 뒤 로그인을 진행합니다. 브라우저에서 링크를 승인하거나, 이메일로 받은 6자리 코드를 입력하면 됩니다. 처음 쓰는 이메일이면 그 자리에서 계정이 만들어집니다. 에이전트가 갖게 되는 것은 `SIMIANX_API_KEY`에 담긴 자기 전용 API 키뿐이고, 웹사이트 로그인은 넘겨받지 않습니다.

터미널에서 설치하려면:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

에이전트별(Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline 등) 명령과 설치 디렉터리는 [INSTALL.md](INSTALL.md)에 있습니다.

### 또는 MCP로 연결

MCP를 지원하는 AI 에이전트는 스킬을 설치하지 않아도 SimianX를 도구로 쓸 수 있습니다. 키와 함께 원격 서버를 한 번만 추가하세요.

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

Claude Desktop, Cursor, Codex, VS Code, Windsurf, Gemini CLI 설정은 [INSTALL.md](INSTALL.md#connect-over-mcp)에 있습니다. 레지스트리 이름: `io.github.SimianX-AI/simianx`.

## 처음 해 볼 호출

| 용도 | 호출 | 문서 |
|---|---|---|
| 실시간 분석 한 번 | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 관심 종목 뉴스 | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| 뉴스가 나오는 즉시 받기 | `GET /v1/news/stream` (SSE, 끊겨도 이어 받기) | [news](skills/simianx/references/news.md) |
| 마켓 펄스 | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| 심층 분석 | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| 섹터 워치 | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| 오토파일럿 | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL은 `https://service.simianx.ai/v1`, 헤더는 `Authorization: Bearer $SIMIANX_API_KEY`입니다. 같은 호출을 셸 스크립트로 만든 예제는 [examples/curl](examples/curl)에 있습니다.

## 플랜

Free, Starter, Plus, Pro가 있고, 자세한 내용은 [가격](https://www.simianx.ai/pricing) 페이지에 있습니다. 에이전트 호출에는 플랜의 포인트가 웹사이트와 같은 요율로 쓰입니다. 뉴스 스트림은 Plus와 Pro에서 실시간이고, Plus 미만에서는 뉴스가 30분 늦게 들어옵니다. 답변은 16개 언어로 받을 수 있습니다. SimianX는 실제 계좌로 거래하지 않으며, 오토파일럿 포지션은 모두 모의 포지션입니다.

## 보안

- 키는 `SIMIANX_API_KEY`에만 둡니다. 스킬은 키를 저장소, 로그, 프롬프트에 절대 쓰지 않습니다.
- 에이전트는 웹사이트 세션을 받지 못합니다. 에이전트에서 로그인하면 그 에이전트용 API 키만 만들어지고, 그때마다 이메일로 알려 드립니다.
- 키마다 권한 범위, 일별·월별 예산, IP 허용 목록(선택)을 정할 수 있습니다. 에이전트에는 맡은 일에 꼭 필요한 만큼만 열어 둔 키를 주세요.
- **내 계정 → API 키**에서 키를 폐기하면 1초 안에 작동을 멈춥니다.

## 버전

스킬은 `X-SimianX-Skill` 헤더에 자기 버전을 담아 보냅니다. 지원이 끝난 버전이면 API가 `426`과 함께 다시 읽을 URL을 알려 주고, `GET /v1/skill`에서 현재 버전과 최소 버전을 확인할 수 있습니다. 업데이트는 에이전트 자체 명령으로 하거나 위 문장을 다시 붙여 넣으면 됩니다. 바뀐 내용은 [변경 이력](CHANGELOG.md)에 있습니다.

## 저장소 구성

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

## 피드백

- 에이전트: `POST /v1/feedback`.
- 사람: 스킬 관련은 [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues), 제품 관련은 [simianx.ai/agents](https://www.simianx.ai/agents).

풀 리퀘스트를 열기 전에 [CONTRIBUTING.md](CONTRIBUTING.md)를 읽어 주세요. 취약점 신고 방법은 [SECURITY.md](SECURITY.md)에 있습니다.

## 라이선스

이 저장소의 모든 내용은 MIT 라이선스입니다. SimianX API 사용에는 [이용 약관](https://www.simianx.ai/legal/terms)이 적용됩니다. SimianX의 분석은 정보이며 투자 조언이 아닙니다.
