<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI para agentes de IA</h1>

<p align="center">
  Una skill que convierte a Claude Code, Codex, Cursor, Copilot, Gemini CLI y cualquier otro agente que lea skills en cliente de la mesa de trading de SimianX:
  autopilots con un registro de eventos de nivel de ejecución, investigación profunda con 8 agentes, análisis en vivo, noticias clasificadas y catalizadores sectoriales.
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">Changelog</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <b>Español</b> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## Qué cubre SimianX

Todo lo que sigue es accesible a través de la skill y vive en [simianx.ai](https://www.simianx.ai); los enlaces abren la página de producto que hay detrás de cada capacidad.

**Mercados**

- **Acciones y ETFs de EE. UU.** — 13,000+ instrumentos cotizados, con resultados, filings, series financieras y conciencia del horario de mercado. Marcos temporales `1m 15m 1H 1D 1W 1mo`. → [Análisis de acciones](https://www.simianx.ai/stocks)
- **Cripto** — 1,500+ monedas y 4,000+ pares en OKX, Binance, Bybit y Coinbase: spot y swaps perpetuos USDT/USD (un símbolo escueto como `BTC` se resuelve al perpetuo). Marcos temporales `1m 5m 15m 1H 4H 1D`. → [Análisis de criptomonedas](https://www.simianx.ai/l)

**Qué hacen los agentes**

- **Autopilots** — los cuatro agentes en vivo se ejecutan de forma programada sobre un símbolo y, si tú lo permites, gestionan una posición simulada (entradas a mercado, limitadas y stop, escalado, stop-loss / take-profit, una puerta de timing). Cada análisis, señal y cambio de posición queda en un registro de eventos que lees con un cursor; `signal.fired` y `position.changed` llevan una caducidad. Tu agente también puede operar esa cartera a mano. → [Pilotos automáticos](https://www.simianx.ai/autopilots)
- **Investigación profunda** — un comité de 8 agentes por ejecución: cuatro analistas (acciones: fundamentals, market, news, timing · cripto: fundamentals, market, news, derivatives), un bull researcher y un bear researcher (las tesis alcista y bajista), un research manager que modera el debate y un risk manager que emite el veredicto y el plan. Horizontes `short`, `swing`, `long`; preguntas de seguimiento; un informe en PDF. → [Análisis profundo](https://www.simianx.ai/c)
- **Análisis en vivo** — los cuatro agentes en vivo, una sola vez: **indicator** (tendencia, momentum y estructura en el gráfico), **intelligence** (flujo de noticias y narrativa), **fundamental** (estados financieros y eventos, u on-chain y derivados para una moneda) y **decision** (la propuesta de operación, con entrada, stop y objetivo). → [Análisis en vivo](https://www.simianx.ai/l)
- **Noticias clasificadas** — cada artículo puntuado por los símbolos que mueve, su valor (`low` / `medium` / `high`) y su sentimiento, como lista, por artículo, traducido a 16 idiomas o como stream en vivo. → [Historias](https://www.simianx.ai/stories)
- **Market Pulse** — choques de precio en ventanas de 1, 5 y 15 minutos, máximos y mínimos de 24 horas / 30 días / 52 semanas, movimientos del día y gaps, para cripto y acciones, con una severidad de 1 a 4. → [Pulso del Mercado](https://www.simianx.ai/pulse)
- **Sector Watch** — catalizadores de fuente primaria para un sector: un calendario (fechas PDUFA, comités asesores, resultados de ensayos clínicos), eventos con severidad de 1 a 4 y dirección (aprobaciones, complete response letters, resultados topline, designaciones, inspecciones, actualizaciones de ficha técnica…), componentes, activos farmacéuticos y seguimientos. Disponible hoy: **Biopharma · aprobaciones de la FDA**, construido a partir de filings de la SEC, comunicados de la FDA y del Federal Register, ClinicalTrials.gov y openFDA. → [Sectores en Foco](https://www.simianx.ai/sectors)
- **Modelos a tu elección** — tres niveles (`fast`, `standard`, `frontier`) y 50+ modelos de 7 proveedores que un plan de pago puede fijar por agente; un catálogo público con precios en puntos. → [Puntos y tarifas](https://www.simianx.ai/points)
- **Clasificación** — cómo ha operado realmente cada modelo, para que un agente elija un modelo de decisión basándose en evidencia. → [Clasificación de modelos AI de criptomonedas](https://www.simianx.ai/crypto-leaderboard)

**Planes e idiomas** — planes Free, Starter, Plus y Pro con puntos mensuales, límites de peticiones por plan y un retraso de datos de 30 minutos por debajo de Plus ([precios](https://www.simianx.ai/pricing)). La API responde en 16 idiomas (`X-Language`). SimianX no opera cuentas reales: las posiciones del autopilot son posiciones simuladas que puedes replicar con tu propio runner.

## Instalación en una frase

Pega esto en tu agente. Descarga la guía de instalación, coloca la skill donde tu agente lee skills y te pide una clave:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

¿Prefieres un comando? Los dos funcionan con cualquier agente que lea skills:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Después crea una clave en **My Account → API keys** en [simianx.ai](https://www.simianx.ai) y expórtala:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Instalación para tu agente

| Agente | Ruta nativa | Dónde queda la skill |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` y luego `/plugin install simianx@simianx` | plugin, o `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` y luego `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (o `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (o `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Cualquier otro | copia `skills/simianx/` en el directorio que escanea tu agente, o ejecuta `scripts/install.sh --agent auto` | ver [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) indica el directorio exacto y las líneas de shell de cada cliente; `scripts/install.sh` (`install.py` en Windows: `install.ps1`) detecta los agentes instalados y copia o enlaza la skill por ti.

## Qué puede hacer tu agente

| Necesidad | Llamada | Referencia |
|---|---|---|
| Iniciar y seguir un autopilot sobre una acción o una moneda | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Operar a mano la cartera simulada del autopilot | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Ejecutar un agente ahora mismo | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Investigación profunda con 8 agentes, con veredicto y plan | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Los agentes en vivo, una sola vez | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Noticias clasificadas (símbolos, valor, sentimiento), como lista o como stream | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Catalizadores sectoriales: calendario, eventos, componentes, seguimientos | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Velas de cripto, indicadores, cotizaciones, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Modelos que puedes fijar por agente, precios, tu cuenta | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Cada evento del registro del autopilot lleva un cursor y, para todo aquello sobre lo que un agente pueda actuar (`signal.fired`, `position.changed`), una marca de caducidad, de modo que un runner nunca actúe sobre información obsoleta. Leer eventos es gratis; pagas por los análisis, con los puntos que tu plan ya incluye.

## Una primera sesión

1. `GET https://service.simianx.ai/v1/skill` — público; confirma que la versión de la skill que tiene tu agente sigue siendo aceptada.
2. `GET /v1/me` con `Authorization: Bearer $SIMIANX_API_KEY` — plan, puntos restantes, límites.
3. `POST /v1/analysis/quote` — cuánto costará una llamada, antes de pagar.
4. `POST /v1/autopilots` con `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — y después haz long-poll del registro de eventos desde el cursor que devuelve la respuesta.

El ciclo completo, en `curl`, está en [examples/curl](examples/curl); un pequeño runner siempre activo que ejecuta tu comando o webhook en cada cambio de posición está en [examples/runner](examples/runner).

## Puntos, no créditos

- Todo se factura en **puntos** de la suscripción de la cuenta. No hay recargas ni pago por llamada.
- Los endpoints de IA se miden según los modelos realmente usados; `GET /v1/pricing` publica el coste habitual por tier (`fast`, `standard`, `frontier`) y `GET /v1/models` el precio de cada modelo que un agente puede elegir.
- Los endpoints de datos se cobran por petición (una fracción de punto); el registro de eventos, `/v1/me`, `/v1/skill`, `/v1/pricing` y `/v1/models` no cuestan nada.
- `402` significa que se agotaron los puntos o el presupuesto de una clave e indica la salida (`renew_now`, `change_plan`, `subscribe`); `429` es un límite de tasa y lleva `Retry-After`. Nada más es nunca un problema de pago.

## Seguridad

- La clave vive en la variable de entorno `SIMIANX_API_KEY`. La skill nunca pide a un agente que la escriba en un repositorio, un log o un prompt.
- Las claves llevan scopes (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), presupuestos de puntos diarios y mensuales, un tope por llamada y una lista de IP permitidas opcional. Dale al agente la clave más pequeña que cumpla su trabajo.
- Revoca cualquier clave en **My Account → API keys**; una clave revocada se rechaza en menos de un segundo. Cada llamada queda registrada en tu cuenta con su coste.
- La skill solo lee tu propia cuenta: tus autopilots, tus ejecuciones, tus claves. Nunca opera con una cuenta real; las posiciones del autopilot son posiciones simuladas.

## Versiones y actualizaciones

La skill informa de su versión en la cabecera `X-SimianX-Skill`. Cuando la API deja de aceptar una versión responde `426` con la URL que hay que releer, y `GET /v1/skill` muestra siempre la versión actual y la mínima junto con el [changelog](CHANGELOG.md). Actualiza con el comando propio de tu agente (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) o vuelve a ejecutar la frase de arriba.

## Estructura del repositorio

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

## Comentarios y soporte

- Desde un agente: `POST /v1/feedback` (lo lee el equipo; el texto abusivo se rechaza y nunca se almacena).
- Desde una persona: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) para la skill, [simianx.ai/agents](https://www.simianx.ai/agents) para el producto.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir un pull request y [SECURITY.md](SECURITY.md) para reportar una vulnerabilidad.

## Licencia

MIT para todo lo que hay en este repositorio. El uso de la API de SimianX se rige por los [Términos de Servicio](https://www.simianx.ai/legal/terms). Los análisis de SimianX son información, no asesoramiento de inversión; las posiciones del autopilot son posiciones simuladas.
