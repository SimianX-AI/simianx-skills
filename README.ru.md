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
  ИИ в реальном времени для live trading. Четыре агента анализируют любую акцию США или криптопару вживую и дают вход, стоп и цель; плюс поток новостей с оценками в реальном времени, сигналы Market Pulse, глубокое исследование, Sector Watch и автопилоты. Skill и удалённый MCP-сервер для Claude Code, Codex, Cursor и любого другого ИИ-агента.
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

## Что умеет SimianX

Основную работу делают две функции.

- **Мультиагентный анализ в реальном времени.** Выберите акцию или криптопару и таймфрейм, и четыре агента одновременно возьмутся за анализ. Агент индикаторов читает график. Агент разведки следит за потоком новостей. Фундаментальный агент изучает отчётность и сделки инсайдеров, а для монеты — ончейн-данные и деривативы. Агент решений взвешивает три вывода и предлагает сделку со входом, стопом и целью. → [Анализ в реальном времени](https://www.simianx.ai/l)
- **Поток новостей с оценками.** Каждая статья приходит с тикерами, которые она двигает, оценкой значимости и тоном: бычьим, медвежьим или нейтральным. Этот же поток питает Пульс рынка, где новости идут рядом с резкими движениями цены, новыми максимумами и минимумами и гэпами. Ваш агент может листать его постранично или держать открытым по своим тикерам. → [Пульс рынка](https://www.simianx.ai/pulse)

Под рукой, когда понадобится:

- **Глубокое исследование.** Восемь агентов спорят об акции или монете и выдают вердикт, торговый план и PDF. Ваш агент может задавать уточняющие вопросы. → [Глубокий анализ](https://www.simianx.ai/c)
- **Секторы под наблюдением.** Календари катализаторов и события из первоисточников, начиная с биофармы. → [Секторы под наблюдением](https://www.simianx.ai/sectors)
- **Автопилоты.** Те же четыре агента работают по расписанию на одном тикере, ведут виртуальную позицию и пишут журнал событий, за которым может следить ваш агент. → [Автопилоты](https://www.simianx.ai/autopilots)
- **Модель на ваш выбор.** Выберите модель для каждого агента и заранее посмотрите, как каждая из них торговала. → [Рейтинг моделей](https://www.simianx.ai/crypto-leaderboard)

Рынки: более 13 000 акций и ETF США на свечах от `1m` до `1mo` и более 4 000 криптопар, спот и бессрочные контракты, от `1m` до `1D`. → [Анализ акций](https://www.simianx.ai/c) · [Анализ криптовалют](https://www.simianx.ai/l)

## Установка одной фразой

Отправьте агенту эту фразу:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Он положит skill туда, где ищет skills, а затем выполнит вход: вы подтверждаете ссылку в браузере или вводите 6-значный код, который мы пришлём на почту. Для нового адреса аккаунт создаётся сразу. В итоге у агента будет собственный API-ключ в `SIMIANX_API_KEY`, а ваш вход на сайт останется только у вас.

Или из терминала:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

Команды и каталоги для каждого агента (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline и других) собраны в [INSTALL.md](INSTALL.md).

### Или подключитесь по MCP

ИИ-агенты с поддержкой MCP могут пользоваться SimianX как набором инструментов без установки skill. Добавьте удалённый сервер один раз со своим ключом:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

То же для Claude Desktop, Cursor, Codex, VS Code, Windsurf и Gemini CLI — в [INSTALL.md](INSTALL.md#connect-over-mcp). Имя в реестре: `io.github.SimianX-AI/simianx`.

## Первые вызовы

| Что | Вызов | Справка |
|---|---|---|
| Разовый анализ в реальном времени | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Новости по вашим тикерам | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| Новости в момент выхода | `GET /v1/news/stream` (server-sent events, с возобновлением) | [news](skills/simianx/references/news.md) |
| Пульс рынка | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Глубокое исследование | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Секторы под наблюдением | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Автопилоты | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Базовый URL `https://service.simianx.ai/v1`, заголовок `Authorization: Bearer $SIMIANX_API_KEY`. Те же вызовы в виде shell-скриптов лежат в [examples/curl](examples/curl).

## Тарифные планы

Free, Starter, Plus и Pro. Подробности на странице [цен](https://www.simianx.ai/pricing). Вызовы агентов используют очки вашего плана по тем же расценкам, что и на сайте. На Plus и Pro поток новостей идёт в реальном времени, на планах ниже Plus новости приходят с задержкой в 30 минут. Ответы доступны на 16 языках. SimianX никогда не торгует на реальном счёте: позиции автопилотов виртуальные.

## Безопасность

- Ключ хранится в `SIMIANX_API_KEY`. Skill никогда не записывает его в репозиторий, лог или промпт.
- Агент никогда не получает сессию на сайте. Вход из агента лишь создаёт API-ключ для этого агента, и мы сообщаем вам об этом письмом.
- У ключей есть области доступа, дневной и месячный бюджеты и необязательный белый список IP. Давайте каждому агенту самый узкий ключ, которого хватает для его задачи.
- Отзовите ключ в разделе **Мой аккаунт → API-ключи**, и он перестанет работать в течение секунды.

## Версии

Skill передаёт свою версию в заголовке `X-SimianX-Skill`. Когда версия выходит из обращения, API отвечает `426` и указывает URL, который нужно перечитать, а `GET /v1/skill` показывает текущую и минимальную версии. Обновитесь командой своего агента или снова отправьте фразу, приведённую выше. Что изменилось, смотрите в [списке изменений](CHANGELOG.md).

## Структура репозитория

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

## Обратная связь

- От агента: `POST /v1/feedback`.
- От человека: вопросы по skill в [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues), по продукту на [simianx.ai/agents](https://www.simianx.ai/agents).

Перед тем как открыть pull request, прочитайте [CONTRIBUTING.md](CONTRIBUTING.md). Об уязвимостях сообщайте по правилам из [SECURITY.md](SECURITY.md).

## Лицензия

Всё в этом репозитории распространяется по лицензии MIT. Использование SimianX API регулируется [Условиями обслуживания](https://www.simianx.ai/legal/terms). Анализы SimianX носят информационный характер и не являются инвестиционной рекомендацией.
