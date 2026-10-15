<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI для ИИ-агентов</h1>

<p align="center">
  Один навык, который превращает Claude Code, Codex, Cursor, Copilot, Gemini CLI и любого другого агента, читающего навыки, в клиента торгового деска SimianX:
  автопилоты с журналом событий исполнительного уровня, глубокое исследование силами 8 агентов, живой анализ, классифицированные новости и отраслевые катализаторы.
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">Список изменений</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <b>Русский</b> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## Что покрывает SimianX

Всё перечисленное ниже доступно через навык и живёт на [simianx.ai](https://www.simianx.ai); ссылки открывают страницу продукта за каждой возможностью.

**Рынки**

- **Акции и ETF США** — 13 000+ листингованных инструментов, с отчётностью, регуляторными документами, финансовыми рядами и учётом торговых часов. Таймфреймы `1m 15m 1H 1D 1W 1mo`. → [Анализ акций](https://www.simianx.ai/stocks)
- **Криптовалюты** — 1 500+ монет и 4 000+ пар на OKX, Binance, Bybit и Coinbase: спот и бессрочные свопы USDT/USD (голый символ вроде `BTC` трактуется как бессрочный контракт). Таймфреймы `1m 5m 15m 1H 4H 1D`. → [Анализ криптовалют](https://www.simianx.ai/l)

**Что делают агенты**

- **Автопилоты** — четыре живых агента работают по расписанию на одном символе и, если вы разрешите, ведут бумажную позицию (входы по рынку, лимитом и стопом, набор и сокращение позиции, стоп-лосс / тейк-профит, тайминг-гейт). Каждый анализ, сигнал и изменение позиции попадает в журнал событий, который вы читаете по курсору; у `signal.fired` и `position.changed` есть срок действия. Ваш агент может торговать этой книгой и вручную. → [Автопилоты](https://www.simianx.ai/autopilots)
- **Глубокое исследование** — комитет из 8 агентов на каждый запуск: четыре аналитика (акции: fundamentals, market, news, timing · крипто: fundamentals, market, news, derivatives), bull researcher и bear researcher (исследователи за рост и за падение), research manager (ведущий дебатов) и risk manager (риск-менеджер, который выносит вердикт и план). Горизонты `short`, `swing`, `long`; уточняющие вопросы; отчёт в PDF. → [Глубокий анализ](https://www.simianx.ai/c)
- **Живой анализ** — четыре живых агента, однократно: **indicator** (индикаторы: тренд, импульс, структура на графике), **intelligence** (новостной поток и нарратив), **fundamental** (финансы и события, а для монеты — ончейн и деривативы) и **decision** (торговое предложение с входом, стопом и целью). → [Живой анализ](https://www.simianx.ai/l)
- **Классифицированные новости** — каждая статья оценена по тикерам, которые она двигает, по значимости (`low` / `medium` / `high`) и по сентименту; списком, по одной статье, в переводе на 16 языков или живым потоком. → [Истории](https://www.simianx.ai/stories)
- **Market Pulse** — ценовые шоки в окнах 1, 5 и 15 минут, максимумы и минимумы за 24 часа / 30 дней / 52 недели, дневные движения и гэпы, по криптовалютам и акциям, с серьёзностью 1–4. → [Пульс рынка](https://www.simianx.ai/pulse)
- **Sector Watch** — катализаторы по сектору из первичных источников: календарь (даты PDUFA, консультативные комитеты, результаты испытаний), события с серьёзностью 1–4 и направлением (одобрения, письма CRL, топлайн-результаты, присвоение статусов, инспекции, обновления инструкций…), состав сектора, лекарственные активы и подписки. Уже доступно: **Biopharma · FDA approvals** — собрано из документов SEC, релизов FDA и Federal Register, ClinicalTrials.gov и openFDA. → [Секторы под наблюдением](https://www.simianx.ai/sectors)
- **Модели на ваш выбор** — три уровня (`fast`, `standard`, `frontier`) и 50+ моделей от 7 провайдеров, которые на платном тарифе можно задать каждому агенту; публичный каталог с ценами в баллах. → [Очки и тарифы](https://www.simianx.ai/points)
- **Рейтинг** — как каждая модель торговала на самом деле, чтобы агент выбирал модель решений по фактам. → [Рейтинг AI-моделей криптовалют](https://www.simianx.ai/crypto-leaderboard)

**Тарифы и языки** — тарифы Free, Starter, Plus и Pro с ежемесячными баллами, лимитами запросов на каждый тариф и 30-минутной задержкой данных ниже Plus ([цены](https://www.simianx.ai/pricing)). API отвечает на 16 языках (`X-Language`). SimianX не торгует реальными счетами: позиции автопилота — бумажные, и вы можете зеркалить их собственным раннером.

## Установка одним предложением

Вставьте это своему агенту. Он скачает руководство по установке, положит навык туда, откуда ваш агент читает навыки, и попросит у вас ключ:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Предпочитаете команду? Обе работают с любым агентом, читающим навыки:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Затем скажите **"Войди в SimianX за меня"**. Агент даст вам ссылку для подтверждения в браузере или пришлёт 6-значный код на почту; в обоих случаях он получает собственный ключ со своими скоупами и бюджетом и сохраняет его как `SIMIANX_API_KEY`. Ещё нет аккаунта? Код из письма создаст его. Ключ также можно создать вручную в разделе **Мой аккаунт → API-ключи** на [simianx.ai](https://www.simianx.ai) и экспортировать его:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Установка для вашего агента

| Агент | Родной способ | Куда попадает навык |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills`, затем `/plugin install simianx@simianx` | плагин или `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills`, затем `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (или `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (или `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Любой другой | скопируйте `skills/simianx/` в каталог, который сканирует ваш агент, или запустите `scripts/install.sh --agent auto` | см. [INSTALL.md](INSTALL.md) |

В [INSTALL.md](INSTALL.md) перечислены точный каталог и команды оболочки для каждого клиента; `scripts/install.sh` (`install.py`, на Windows: `install.ps1`) находит установленных агентов и копирует или линкует навык за вас.

## Что умеет ваш агент

| Задача | Вызов | Справка |
|---|---|---|
| Запустить автопилот по акции или монете и следить за ним | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Торговать бумажной книгой автопилота вручную | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Запустить одного агента прямо сейчас | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Глубокое исследование 8 агентами с вердиктом и планом | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Живые агенты, однократно | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Классифицированные новости (тикеры, значимость, сентимент) списком или потоком | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Отраслевые катализаторы: календарь, события, состав, подписки | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Свечи, индикаторы и котировки по криптовалютам, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Модели, которые можно задать каждому агенту, цены, ваш аккаунт | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Каждое событие в журнале автопилота несёт курсор, а всё, на что агент может отреагировать (`signal.fired`, `position.changed`), — ещё и метку истечения, так что раннер никогда не действует по устаревшим данным. Чтение событий бесплатно; вы платите за анализы — баллами, которые уже входят в ваш тариф.

## Первая сессия

1. `GET https://service.simianx.ai/v1/skill` — публичный; подтверждает, что версия навыка у вашего агента всё ещё принимается.
2. `GET /v1/me` с `Authorization: Bearer $SIMIANX_API_KEY` — тариф, остаток баллов, лимиты.
3. `POST /v1/analysis/quote` — сколько будет стоить вызов, до оплаты.
4. `POST /v1/autopilots` с `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — затем long-poll журнала событий с курсора, который вернул ответ.

Полный цикл на `curl` лежит в [examples/curl](examples/curl); небольшой постоянно работающий раннер, который выполняет вашу команду или вебхук при каждом изменении позиции, — в [examples/runner](examples/runner).

## Только баллы

- Всё оплачивается **баллами** из подписки аккаунта. Никаких пополнений и оплаты за вызов.
- AI-эндпоинты тарифицируются по фактически использованным моделям; `GET /v1/pricing` публикует обычную стоимость по уровням (`fast`, `standard`, `frontier`), а `GET /v1/models` — цену каждой модели, которую может выбрать агент.
- Эндпоинты данных оплачиваются за запрос (доля балла); журнал событий, `/v1/me`, `/v1/skill`, `/v1/pricing` и `/v1/models` бесплатны.
- `402` означает, что закончились баллы или бюджет ключа, и называет выход (`renew_now`, `change_plan`, `subscribe`); `429` — это ограничение частоты, с заголовком `Retry-After`. Ничто другое никогда не является проблемой оплаты.

## Безопасность

- Ключ живёт в переменной окружения `SIMIANX_API_KEY`. Навык никогда не просит агента записать его в репозиторий, лог или промпт.
- Агент никогда не получает сессию на сайте. Вход из агента (по ссылке в браузере или по коду из письма) всегда создаёт только API-ключ для этого агента: об этом приходит письмо, а событие попадает в ваши действия, связанные с безопасностью; сайт, оплата и настройки безопасности остаются у вас.
- У ключей есть скоупы (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), дневной и месячный бюджеты баллов, лимит на вызов и необязательный список разрешённых IP. Давайте агенту самый узкий ключ, которого хватает для его задачи.
- Отозвать любой ключ можно в **Мой аккаунт → API-ключи**; отозванный ключ отклоняется в течение секунды. Каждый вызов логируется под вашим аккаунтом вместе с его стоимостью.
- Навык читает только ваш собственный аккаунт: ваши автопилоты, ваши запуски, ваши ключи. Он никогда не торгует на реальном счёте; позиции автопилота — бумажные.

## Версии и обновления

Навык сообщает свою версию в заголовке `X-SimianX-Skill`. Когда API перестаёт принимать версию, он отвечает `426` с URL, который нужно перечитать, а `GET /v1/skill` всегда показывает текущую и минимальную версии плюс [список изменений](CHANGELOG.md). Обновляйтесь родной командой вашего агента (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) или снова выполните то самое предложение выше.

## Структура репозитория

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

## Обратная связь и поддержка

- От агента: `POST /v1/feedback` (читает команда; оскорбительный текст отклоняется и никогда не сохраняется).
- От человека: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) по навыку, [simianx.ai/agents](https://www.simianx.ai/agents) по продукту.

Перед тем как открыть pull request, прочитайте [CONTRIBUTING.md](CONTRIBUTING.md), а чтобы сообщить об уязвимости — [SECURITY.md](SECURITY.md).

## Лицензия

MIT для всего в этом репозитории. Использование SimianX API регулируется [Условиями обслуживания](https://www.simianx.ai/legal/terms). Анализы SimianX — это информация, а не инвестиционная рекомендация; позиции автопилота — бумажные.
