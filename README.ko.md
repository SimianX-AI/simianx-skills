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
  Claude Code, Codex, Cursor, Copilot, Gemini CLI를 비롯해 스킬을 읽는 모든 에이전트를 스킬 하나로 SimianX 트레이딩 데스크의 클라이언트로 만듭니다:
  실행 등급 이벤트 로그를 갖춘 오토파일럿, 8개 에이전트 딥 리서치, 라이브 분석, 분류된 뉴스, 섹터 촉매.
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

## SimianX가 다루는 범위

아래의 모든 기능은 스킬을 통해 사용할 수 있으며 [simianx.ai](https://www.simianx.ai)에서 제공됩니다. 각 링크는 해당 기능의 제품 페이지를 엽니다.

**시장**

- **미국 주식과 ETF** — 13,000개 이상의 상장 종목. 실적, 공시, 재무 시계열, 거래 시간 인식을 갖추고 있습니다. 타임프레임 `1m 15m 1H 1D 1W 1mo`. → [주식 분석](https://www.simianx.ai/c)
- **암호화폐** — OKX, Binance, Bybit, Coinbase에 걸친 1,500개 이상의 코인과 4,000개 이상의 페어: 현물과 USDT/USD 무기한 스왑(`BTC`처럼 심볼만 쓰면 무기한 스왑으로 해석됩니다). 타임프레임 `1m 5m 15m 1H 4H 1D`. → [암호화폐 분석](https://www.simianx.ai/l)

**에이전트가 하는 일**

- **오토파일럿** — 4개의 라이브 에이전트가 하나의 심볼에 대해 일정에 따라 실행되고, 허용하면 페이퍼 포지션을 관리합니다(시장가·지정가·스톱 진입, 분할 매매, 손절 / 익절, 타이밍 게이트). 모든 분석, 시그널, 포지션 변경은 커서로 읽는 이벤트 로그에 기록되며 `signal.fired`와 `position.changed`에는 만료 시각이 붙습니다. 에이전트가 그 북을 직접 거래할 수도 있습니다. → [자동 조종 장치](https://www.simianx.ai/autopilots)
- **딥 리서치** — 실행마다 8개 에이전트로 구성된 위원회: 분석가 4명(주식: fundamentals, market, news, timing · 암호화폐: fundamentals, market, news, derivatives), bull researcher와 bear researcher(강세·약세 리서처), 토론을 진행하는 research manager(리서치 매니저), 판정과 계획을 내놓는 risk manager(리스크 매니저). 기간 `short`, `swing`, `long`; 후속 질문; PDF 보고서. → [딥 분석](https://www.simianx.ai/c)
- **라이브 분석** — 4개의 라이브 에이전트를 한 번 실행: **indicator**(지표: 차트의 추세, 모멘텀, 구조), **intelligence**(인텔리전스: 뉴스 흐름과 내러티브), **fundamental**(펀더멘털: 재무와 이벤트, 코인이라면 온체인과 파생상품), **decision**(결정: 진입가, 손절가, 목표가가 포함된 거래 제안). → [라이브 분석](https://www.simianx.ai/l)
- **분류된 뉴스** — 모든 기사를 영향을 주는 종목, 가치(`low` / `medium` / `high`), 심리로 점수화합니다. 목록으로, 기사 단위로, 16개 언어로 번역해서, 또는 라이브 스트림으로 받을 수 있습니다. → [스토리](https://www.simianx.ai/stories)
- **Market Pulse** — 1분·5분·15분 창의 가격 급변, 24시간 / 30일 / 52주 고점·저점, 일중 변동과 갭을 암호화폐와 주식 모두에서 심각도 1–4와 함께 감지합니다. → [마켓 펄스](https://www.simianx.ai/pulse)
- **Sector Watch** — 섹터의 1차 출처 기반 촉매: 캘린더(PDUFA 기한, 자문위원회, 임상 결과 발표), 심각도 1–4와 방향이 있는 이벤트(승인, 보완요구서한, 톱라인 결과, 지정, 실사, 라벨 변경 등), 구성 종목, 의약품 자산, 팔로우. 현재 제공 중: **Biopharma · FDA approvals** — SEC 공시, FDA와 Federal Register 발표, ClinicalTrials.gov, openFDA로 구축했습니다. → [섹터 워치](https://www.simianx.ai/sectors)
- **직접 고르는 모델** — 3개 티어(`fast`, `standard`, `frontier`)와 7개 제공사의 50개 이상 모델. 유료 요금제에서는 에이전트별로 설정할 수 있습니다. 포인트 기준 가격이 적힌 공개 카탈로그가 있습니다. → [포인트 및 요율](https://www.simianx.ai/points)
- **리더보드** — 각 모델이 실제로 어떻게 거래했는지 보여 주므로, 에이전트가 근거를 바탕으로 결정 모델을 고를 수 있습니다. → [암호화폐 AI 모델 리더보드](https://www.simianx.ai/crypto-leaderboard)

**요금제와 언어** — Free, Starter, Plus, Pro 요금제에는 월간 포인트와 요금제별 속도 제한이 있으며, Plus 미만에서는 데이터가 30분 지연됩니다([가격](https://www.simianx.ai/pricing)). API는 16개 언어로 응답합니다(`X-Language`). SimianX는 실계좌를 거래하지 않습니다. 오토파일럿 포지션은 페이퍼 포지션이며, 자신의 러너로 미러링할 수 있습니다.

## 한 문장으로 설치

이 문장을 에이전트에 붙여 넣으세요. 설치 가이드를 가져와 에이전트가 스킬을 읽는 위치에 스킬을 넣고, 키를 입력하라고 요청합니다:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

명령어가 더 편하신가요? 두 가지 모두 스킬을 읽는 모든 에이전트에서 동작합니다:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

그다음 **"SimianX에 로그인해 줘"** 라고 말하세요. 에이전트는 브라우저에서 승인할 링크를 건네거나 6자리 코드를 이메일로 보냅니다. 어느 쪽이든 에이전트는 스코프와 예산이 정해진 자기만의 키를 받아 `SIMIANX_API_KEY`로 저장합니다. 아직 계정이 없나요? 이메일 코드가 계정을 만들어 줍니다. [simianx.ai](https://www.simianx.ai)의 **내 계좌 → API 키**에서 직접 키를 만들고 내보낼 수도 있습니다:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## 에이전트별 설치

| 에이전트 | 기본 설치 방법 | 스킬이 설치되는 위치 |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` 다음 `/plugin install simianx@simianx` | 플러그인 또는 `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` 다음 `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (또는 `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (또는 `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| 그 외 | `skills/simianx/`를 에이전트가 스캔하는 디렉터리에 복사하거나 `scripts/install.sh --agent auto`를 실행 | [INSTALL.md](INSTALL.md) 참고 |

[INSTALL.md](INSTALL.md)에 각 클라이언트의 정확한 디렉터리와 셸 명령이 정리되어 있습니다. `scripts/install.sh`(Windows에서는 `install.py`: `install.ps1`)가 설치된 에이전트를 감지해 스킬을 복사하거나 링크해 줍니다.

## 에이전트가 할 수 있는 일

| 필요한 작업 | 호출 | 참고 문서 |
|---|---|---|
| 주식이나 코인에 오토파일럿을 시작하고 추적 | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| 오토파일럿의 페이퍼 북을 직접 거래 | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| 에이전트 하나를 지금 바로 실행 | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| 판정과 계획이 포함된 8개 에이전트 딥 리서치 | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| 라이브 에이전트를 한 번 실행 | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 분류된 뉴스(종목, 가치, 심리)를 목록 또는 스트림으로 | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| 섹터 촉매: 캘린더, 이벤트, 구성 종목, 팔로우 | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| 암호화폐 캔들, 지표, 시세, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| 에이전트별로 설정할 수 있는 모델, 가격, 내 계정 정보 | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

오토파일럿 로그의 모든 이벤트에는 커서가 붙고, 에이전트가 행동할 수 있는 이벤트(`signal.fired`, `position.changed`)에는 만료 시각이 붙기 때문에 러너가 오래된 정보로 행동하는 일이 없습니다. 이벤트 읽기는 무료이며, 비용은 분석에만 발생하고 요금제에 이미 포함된 포인트로 지불합니다.

## 첫 세션

1. `GET https://service.simianx.ai/v1/skill` — 공개 엔드포인트. 에이전트가 가진 스킬 버전이 아직 허용되는지 확인합니다.
2. `GET /v1/me`에 `Authorization: Bearer $SIMIANX_API_KEY`를 붙여서 — 요금제, 남은 포인트, 한도.
3. `POST /v1/analysis/quote` — 결제 전에 호출 비용을 확인.
4. `POST /v1/autopilots`에 `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}`를 담아서 — 그다음 응답이 돌려주는 커서부터 이벤트 로그를 롱폴링.

`curl`로 작성한 전체 루프는 [examples/curl](examples/curl)에, 포지션이 바뀔 때마다 명령이나 웹훅을 실행하는 작은 상시 러너는 [examples/runner](examples/runner)에 있습니다.

## 포인트로만 과금

- 모든 비용은 계정 구독에 포함된 **포인트**로 청구됩니다. 충전도, 호출당 과금도 없습니다.
- AI 엔드포인트는 실제로 사용한 모델 기준으로 계량됩니다. `GET /v1/pricing`은 티어(`fast`, `standard`, `frontier`)별 통상 비용을, `GET /v1/models`는 에이전트가 선택할 수 있는 모든 모델의 가격을 공개합니다.
- 데이터 엔드포인트는 요청당(1포인트의 일부) 과금됩니다. 이벤트 로그, `/v1/me`, `/v1/skill`, `/v1/pricing`, `/v1/models`는 무료입니다.
- `402`는 포인트나 키 예산이 소진됐다는 뜻이며 해결 방법(`renew_now`, `change_plan`, `subscribe`)을 알려줍니다. `429`는 속도 제한이며 `Retry-After`를 함께 보냅니다. 그 외에는 결제 문제가 아닙니다.

## 보안

- 키는 `SIMIANX_API_KEY` 환경 변수에 둡니다. 이 스킬은 에이전트에게 키를 저장소, 로그, 프롬프트에 쓰라고 절대 요청하지 않습니다.
- 에이전트는 절대 웹사이트 세션을 얻지 못합니다. 에이전트에서의 로그인(브라우저 링크 또는 이메일 코드)은 그 에이전트용 API 키만 만들며, 이는 이메일로 알려 드리고 보안 활동에도 기록됩니다. 웹사이트, 결제, 보안 설정은 그대로 내 손에 남습니다.
- 키에는 스코프(`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), 일별·월별 포인트 예산, 호출당 상한, 선택적 IP 허용 목록이 있습니다. 에이전트에는 맡은 일을 처리할 수 있는 최소한의 키만 주세요.
- 키는 **내 계좌 → API 키**에서 언제든 폐기할 수 있으며, 폐기된 키는 1초 안에 거부됩니다. 모든 호출은 비용과 함께 내 계정에 기록됩니다.
- 이 스킬은 본인 계정만 읽습니다: 내 오토파일럿, 내 실행, 내 키. 실제 계좌로 거래하는 일은 없으며, 오토파일럿 포지션은 페이퍼 포지션입니다.

## 버전과 업데이트

스킬은 자신의 버전을 `X-SimianX-Skill` 헤더로 알립니다. API가 더 이상 해당 버전을 받지 않으면 다시 읽어야 할 URL과 함께 `426`으로 응답하고, `GET /v1/skill`은 항상 현재 버전과 최소 버전, 그리고 [변경 이력](CHANGELOG.md)을 보여줍니다. 에이전트 자체 명령(`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx` 등)으로 업데이트하거나 위의 한 문장을 다시 실행하세요.

## 저장소 구성

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

## 피드백과 지원

- 에이전트에서: `POST /v1/feedback`(팀이 읽습니다. 욕설이나 폭언은 거부되며 저장되지 않습니다).
- 사람이 직접: 스킬 관련은 [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues), 제품 관련은 [simianx.ai/agents](https://www.simianx.ai/agents).

풀 리퀘스트를 열기 전에 [CONTRIBUTING.md](CONTRIBUTING.md)를, 취약점 신고는 [SECURITY.md](SECURITY.md)를 확인하세요.

## 라이선스

이 저장소의 모든 내용은 MIT 라이선스입니다. SimianX API 사용에는 [서비스 약관](https://www.simianx.ai/legal/terms)이 적용됩니다. SimianX 분석은 정보일 뿐 투자 조언이 아니며, 오토파일럿 포지션은 페이퍼 포지션입니다.
