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
  Dale a cualquier agente de IA un equipo de análisis completo. Con SimianX AI, tu agente puede convocar un comité de análisis de 8 agentes sobre cualquier acción de EE. UU. o par cripto y hacerle preguntas después, obtener una lectura en vivo de cuatro agentes con entrada, stop y objetivo, y mantener abierto un flujo de noticias evaluadas sobre tus activos. Una skill y un servidor MCP remoto para Claude Code, Codex, Cursor, Muse, Grok Bot, dots y cualquier otro agente.
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

## Por qué darle SimianX a tu agente

Pregúntale a un agente por su cuenta *"¿Conviene comprar NVDA para un swing trade?"* y buscará en la web, resumirá titulares que pueden tener días y te dará la opinión de un solo modelo. No tiene gráfico en vivo, nadie defiende la postura contraria y se detiene cuando termina el chat.

Con SimianX, el mismo agente:

| | Por su cuenta | Con SimianX AI |
|---|---|---|
| Quién trabaja en ello | Un modelo | Un comité de 8 agentes: cuatro analistas, un investigador alcista y otro bajista, un gerente de investigación y un gestor de riesgos |
| Qué lee | Resultados de búsqueda web | Velas en vivo, informes regulatorios, operaciones de directivos, el flujo de noticias; datos on-chain y de derivados si es una moneda |
| Qué obtienes | Una opinión | Un veredicto con entrada, stop y objetivo, y un informe en PDF |
| Después | Empieza de cero | Lleva las preguntas de seguimiento al mismo comité o deja un piloto automático vigilando |

## Qué puedes pedirle

Con la skill instalada, pídeselo con tus propias palabras:

- *"Convoca al comité de SimianX sobre NVDA para un swing trade."* Cuatro analistas presentan sus informes, el alcista y el bajista lo debaten, y el gestor de riesgos entrega el veredicto, el plan y un PDF.
- *"Pregúntale al investigador bajista qué demostraría que la tesis alcista está equivocada."* Las preguntas de seguimiento van al mismo análisis, así que la respuesta parte de todo lo que el comité ya leyó.
- *"Haz que el comité analice SOL a corto plazo."* En una moneda, los analistas también leen los flujos on-chain y el mercado de derivados.
- *"¿Cómo se ve BTC en el gráfico de 15 minutos ahora mismo?"* Responden cuatro agentes en vivo, y el agente de Decisión dice si comprar, vender o quedarse fuera, con entrada, stop y objetivo.
- *"Avísame cuando salga una noticia importante sobre TSLA o ETH."* Un flujo de noticias evaluadas sobre tus activos, en vivo a medida que se evalúa cada noticia.
- *"Vigila AAPL en el gráfico de 1 hora y gestiona una posición simulada."* Un piloto automático vuelve a ejecutar los agentes en cada cierre de vela y registra cada señal.
- *"¿Qué fechas PDUFA de biofarmacéuticas caen en los próximos 30 días?"* Sectores en Foco, a partir de fuentes primarias.
- *"¿Qué se movió con fuerza en cripto en la última hora?"* Pulso del Mercado: movimientos bruscos, nuevos máximos y mínimos, picos de volumen y gaps.

Las cuentas gratuitas pueden probar el comité con activos populares como NVDA, AAPL, TSLA, BTC y ETH.

## Qué hace SimianX

Dos funciones hacen casi todo el trabajo.

- **Análisis multiagente en vivo.** Elige una acción o un par cripto y una temporalidad, y cuatro agentes se ponen a analizarlo a la vez. El agente de Indicadores lee el gráfico. El de Inteligencia sigue las noticias. El Fundamental lee los informes regulatorios y las operaciones de directivos o, si es una moneda, los datos on-chain y de derivados. El de Decisión sopesa los tres y propone una operación con entrada, stop y objetivo. → [Análisis en vivo](https://www.simianx.ai/l)
- **Un flujo de noticias evaluadas.** Cada artículo llega etiquetado con los activos que mueve, una puntuación de importancia y una lectura alcista, bajista o neutral. Es el feed que alimenta el Pulso del Mercado, donde aparece junto a los movimientos bruscos de precio, los nuevos máximos y mínimos y los gaps. Tu agente puede recorrerlo página a página o dejar un stream abierto con sus activos. → [Pulso del Mercado](https://www.simianx.ai/pulse)

Y para cuando lo necesites:

- **Investigación a fondo.** Ocho agentes debaten sobre una acción o una moneda y vuelven con un veredicto, un plan de trading y un PDF. Tu agente puede hacer preguntas de seguimiento. → [Análisis profundo](https://www.simianx.ai/c)
- **Sectores en Foco.** Calendarios de catalizadores y eventos sacados de fuentes primarias, empezando por el sector biofarmacéutico. → [Sectores en Foco](https://www.simianx.ai/sectors)
- **Pilotos automáticos.** Los mismos cuatro agentes en vivo trabajan con un horario sobre un solo activo, llevan una posición simulada y dejan un registro de eventos que tu agente puede seguir. → [Pilotos automáticos](https://www.simianx.ai/autopilots)
- **El modelo lo eliges tú.** Decide qué modelo usa cada agente y, antes, mira cómo ha operado cada uno. → [Clasificación de modelos](https://www.simianx.ai/crypto-leaderboard)

Mercados: más de 13,000 acciones y ETF de EE. UU., con velas de `1m` a `1mo`, y más de 4,000 pares cripto, spot y perpetuos, de `1m` a `1D`. → [Análisis de acciones](https://www.simianx.ai/c) · [Análisis de criptomonedas](https://www.simianx.ai/l)

## Instala con una frase

Pega esto en tu agente:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and sign me in.
```

El agente deja la skill donde busca sus skills y luego inicia tu sesión: apruebas un enlace en el navegador o escribes el código de 6 dígitos que te enviamos por correo. Si el correo es nuevo, la cuenta se crea en el acto. Al final, el agente tiene su propia clave de API en `SIMIANX_API_KEY` y nunca tu acceso a la web.

Si prefieres la terminal:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

El comando y el directorio de cada agente (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline y los demás) están en [INSTALL.md](INSTALL.md).

### Muse, Grok Bot, dots y otros agentes con su propia computadora

Los agentes que funcionan en su propia computadora en la nube leen la misma frase. Se conectan por MCP o crean un conector a partir del [documento OpenAPI](https://service.simianx.ai/v1/openapi.json), inician tu sesión, guardan la clave en su propio almacén de credenciales y registran SimianX como skill. Las instrucciones exactas para Muse, Grok Bot y dots están en [INSTALL.md](INSTALL.md#agents-with-their-own-computer-muse-grok-bot-dots).

### O conéctate por MCP

Los agentes de IA que hablan MCP pueden usar SimianX como herramientas sin instalar la skill. Añade el servidor remoto una vez con tu clave:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

Lo mismo para Claude Desktop, Cursor, Codex, VS Code, Windsurf, Gemini CLI, Grok Bot y Muse está en [INSTALL.md](INSTALL.md#connect-over-mcp). Nombre en el registro: `io.github.SimianX-AI/simianx`.

## Primeras llamadas

| Qué | Llamada | Referencia |
|---|---|---|
| Sesión de análisis en vivo (en cada cierre de vela) | `POST /v1/live/sessions` → the WebSocket, or `GET /v1/updates?wait=30` | [live](skills/simianx/references/live.md) |
| Lectura rápida, una vez | `POST /v1/analysis/quick` → `GET /v1/updates?wait=30` | [quick](skills/simianx/references/quick.md) |
| Todo lo que el usuario aún no ha oído | `GET /v1/updates?ack=<id>&wait=30` | [following](skills/simianx/references/following.md) |
| Noticias de tus activos | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| Noticias en cuanto salen | `GET /v1/news/stream` (server-sent events, se reanuda si se corta) | [news](skills/simianx/references/news.md) |
| Pulso del Mercado | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Investigación a fondo | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Sectores en Foco | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Pilotos automáticos | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

URL base `https://service.simianx.ai/v1`, cabecera `Authorization: Bearer $SIMIANX_API_KEY`. Las mismas llamadas, como scripts de shell, están en [examples/curl](examples/curl).

## Planes

Free, Starter, Plus y Pro (consulta los [precios](https://www.simianx.ai/pricing)). Las llamadas del agente usan los puntos de tu plan, con las mismas tarifas que la web. El flujo de noticias es en tiempo real en Plus y Pro; por debajo de Plus, las noticias llegan con 30 minutos de retraso. La API responde en 16 idiomas.

Puedes conectar los análisis y las señales de la API de SimianX a tu propio sistema de trading y enviar órdenes reales mediante un bróker o exchange que autorices. Las posiciones registradas dentro de SimianX son simuladas; tu integración envía y gestiona las órdenes reales en tu propia cuenta.

## Seguridad

- La clave se queda en `SIMIANX_API_KEY`. La skill nunca la escribe en un repositorio, un log ni un prompt.
- Un agente nunca obtiene una sesión de la web. Iniciar sesión desde un agente solo crea una clave de API para ese agente, y te avisamos por correo cuando ocurre.
- Las claves tienen alcances, presupuestos diarios y mensuales y una lista opcional de IPs permitidas. Dale a cada agente la clave más restringida que le sirva para su trabajo.
- Revoca una clave en **Mi cuenta → Claves de API** y deja de funcionar en menos de un segundo.

## Versiones

La skill envía su versión en la cabecera `X-SimianX-Skill`. Cuando se retira una versión, la API responde `426` con la URL que hay que volver a leer, y `GET /v1/skill` muestra la versión actual y la mínima. Actualiza con el comando de tu agente o vuelve a pegar la frase de arriba. Lo que cambió está en el [registro de cambios](CHANGELOG.md).

## Estructura del repositorio

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

## Comentarios

- Desde un agente: `POST /v1/feedback`.
- Desde una persona: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) para la skill, [simianx.ai/agents](https://www.simianx.ai/agents) para el producto.

Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir un pull request y [SECURITY.md](SECURITY.md) para reportar una vulnerabilidad.

## Licencia

Todo el contenido de este repositorio tiene licencia MIT. El uso de la API de SimianX se rige por los [Términos de servicio](https://www.simianx.ai/legal/terms). Los análisis de SimianX son información, no asesoramiento de inversión.
