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
  Uma skill que transforma o Claude Code, Codex, Cursor, Copilot, Gemini CLI e qualquer outro agente que lê skills em cliente da mesa de operações da SimianX:
  autopilots com um log de eventos de nível de execução, pesquisa profunda com 8 agentes, análise ao vivo, notícias classificadas e catalisadores setoriais.
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
  <a href="README.md">English</a> · <b>Português</b> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## O que a SimianX cobre

Tudo o que está abaixo é acessível pela skill e vive em [simianx.ai](https://www.simianx.ai); os links abrem a página do produto por trás de cada capacidade.

**Mercados**

- **Ações e ETFs dos EUA** — 13,000+ instrumentos listados, com resultados, filings, séries financeiras e consciência do horário de pregão. Timeframes `1m 15m 1H 1D 1W 1mo`. → [Análise de Ações](https://www.simianx.ai/stocks)
- **Cripto** — 1,500+ moedas e 4,000+ pares em OKX, Binance, Bybit e Coinbase: spot e swaps perpétuos USDT/USD (um símbolo simples como `BTC` resolve para o perpétuo). Timeframes `1m 5m 15m 1H 4H 1D`. → [Análise de Criptomoedas](https://www.simianx.ai/l)

**O que os agentes fazem**

- **Autopilots** — os quatro agentes ao vivo rodam em horários programados sobre um símbolo e, se você permitir, gerenciam uma posição simulada (entradas a mercado, limitadas e stop, escalonamento, stop-loss / take-profit, um gate de timing). Cada análise, sinal e mudança de posição cai em um log de eventos que você lê com um cursor; `signal.fired` e `position.changed` carregam uma expiração. Seu agente também pode operar essa carteira manualmente. → [Pilotos automáticos](https://www.simianx.ai/autopilots)
- **Pesquisa profunda** — um comitê de 8 agentes por execução: quatro analistas (ações: fundamentals, market, news, timing · cripto: fundamentals, market, news, derivatives), um bull researcher e um bear researcher (as teses de alta e de baixa), um research manager que modera o debate e um risk manager que emite o veredito e o plano. Horizontes `short`, `swing`, `long`; perguntas de acompanhamento; um relatório em PDF. → [Análise profunda](https://www.simianx.ai/c)
- **Análise ao vivo** — os quatro agentes ao vivo, uma única vez: **indicator** (tendência, momentum e estrutura no gráfico), **intelligence** (fluxo de notícias e narrativa), **fundamental** (demonstrações financeiras e eventos, ou on-chain e derivativos para uma moeda) e **decision** (a proposta de operação, com entrada, stop e alvo). → [Análise ao vivo](https://www.simianx.ai/l)
- **Notícias classificadas** — cada artigo pontuado pelos símbolos que movimenta, pelo seu valor (`low` / `medium` / `high`) e pelo seu sentimento, em lista, por artigo, traduzido para 16 idiomas ou como stream ao vivo. → [Histórias](https://www.simianx.ai/stories)
- **Market Pulse** — choques de preço em janelas de 1, 5 e 15 minutos, máximas e mínimas de 24 horas / 30 dias / 52 semanas, variações do dia e gaps, para cripto e ações, com severidade de 1 a 4. → [Pulso do Mercado](https://www.simianx.ai/pulse)
- **Sector Watch** — catalisadores de fonte primária para um setor: um calendário (datas PDUFA, comitês consultivos, resultados de ensaios clínicos), eventos com severidade de 1 a 4 e direção (aprovações, complete response letters, resultados topline, designações, inspeções, atualizações de bula…), constituintes, ativos farmacêuticos e acompanhamentos. No ar hoje: **Biopharma · aprovações da FDA**, construído a partir de filings da SEC, comunicados da FDA e do Federal Register, ClinicalTrials.gov e openFDA. → [Setores em Foco](https://www.simianx.ai/sectors)
- **Modelos à sua escolha** — três níveis (`fast`, `standard`, `frontier`) e 50+ modelos de 7 provedores que um plano pago pode definir por agente; um catálogo público com preços em pontos. → [Pontos e Tarifas](https://www.simianx.ai/points)
- **Ranking** — como cada modelo realmente operou, para que um agente escolha um modelo de decisão com base em evidências. → [Ranking de Modelos AI de Criptomoedas](https://www.simianx.ai/crypto-leaderboard)

**Planos e idiomas** — planos Free, Starter, Plus e Pro com pontos mensais, limites de requisições por plano e um atraso de dados de 30 minutos abaixo do Plus ([preços](https://www.simianx.ai/pricing)). A API responde em 16 idiomas (`X-Language`). A SimianX não opera contas reais: as posições do autopilot são posições simuladas que você pode espelhar com o seu próprio runner.

## Instale em uma frase

Cole isto no seu agente. Ele busca o guia de instalação, coloca a skill onde o seu agente lê skills e pede uma chave:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

Prefere um comando? Os dois funcionam em qualquer agente que lê skills:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

Depois diga **"Faça meu login na SimianX"**. O agente entrega a você um link para aprovar no navegador ou envia um código de 6 dígitos por e-mail; de um jeito ou de outro, ele recebe uma chave própria, com escopo e orçamento, e a guarda como `SIMIANX_API_KEY`. Ainda não tem conta? O código por e-mail cria uma. Você também pode criar uma chave manualmente em **My Account → API keys** no [simianx.ai](https://www.simianx.ai) e exportá-la:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## Instale para o seu agente

| Agente | Caminho nativo | Onde a skill fica |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` e depois `/plugin install simianx@simianx` | plugin, ou `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` e depois `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (ou `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (ou `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| Qualquer outro | copie `skills/simianx/` para o diretório que o seu agente varre, ou execute `scripts/install.sh --agent auto` | veja [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) lista o diretório exato e as linhas de shell de cada cliente; `scripts/install.sh` (`install.py` no Windows: `install.ps1`) detecta os agentes instalados e copia ou cria links da skill para você.

## O que o seu agente pode fazer

| Necessidade | Chamada | Referência |
|---|---|---|
| Iniciar e acompanhar um autopilot em uma ação ou uma moeda | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| Operar manualmente a carteira simulada do autopilot | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| Executar um agente agora | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| Pesquisa profunda com 8 agentes, com veredito e plano | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Os agentes ao vivo, uma única vez | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Notícias classificadas (símbolos, valor, sentimento), em lista ou em stream | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| Catalisadores setoriais: calendário, eventos, constituintes, acompanhamentos | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| Candles de cripto, indicadores, cotações, Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Modelos que você pode definir por agente, preços, sua conta | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

Cada evento do log do autopilot carrega um cursor e, para tudo em que um agente possa agir (`signal.fired`, `position.changed`), um carimbo de expiração, para que um runner nunca aja sobre informação desatualizada. Ler eventos é gratuito; você paga pelas análises, com os pontos que o seu plano já inclui.

## Uma primeira sessão

1. `GET https://service.simianx.ai/v1/skill` — público; confirma que a versão da skill que o seu agente tem ainda é aceita.
2. `GET /v1/me` com `Authorization: Bearer $SIMIANX_API_KEY` — plano, pontos restantes, limites.
3. `POST /v1/analysis/quote` — quanto uma chamada vai custar, antes de pagar.
4. `POST /v1/autopilots` com `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — depois faça long-poll do log de eventos a partir do cursor que a resposta devolve.

O ciclo completo, em `curl`, está em [examples/curl](examples/curl); um pequeno runner sempre ativo que executa o seu comando ou webhook a cada mudança de posição está em [examples/runner](examples/runner).

## Pontos, não créditos

- Tudo é cobrado em **pontos** da assinatura da conta. Não há recargas nem pagamento por chamada.
- Os endpoints de IA são medidos pelos modelos realmente usados; `GET /v1/pricing` publica o custo habitual por tier (`fast`, `standard`, `frontier`) e `GET /v1/models` o preço de cada modelo que um agente pode escolher.
- Os endpoints de dados são cobrados por requisição (uma fração de ponto); o log de eventos, `/v1/me`, `/v1/skill`, `/v1/pricing` e `/v1/models` não custam nada.
- `402` significa que os pontos ou o orçamento de uma chave acabaram e indica a saída (`renew_now`, `change_plan`, `subscribe`); `429` é limite de taxa e traz `Retry-After`. Nada mais é jamais um problema de pagamento.

## Segurança

- A chave vive na variável de ambiente `SIMIANX_API_KEY`. A skill nunca pede a um agente que a escreva em um repositório, em um log ou em um prompt.
- Um agente nunca recebe uma sessão do site. Fazer login a partir de um agente (link no navegador ou código por e-mail) só cria uma chave de API para esse agente, anunciada por e-mail e listada na sua atividade de segurança; o site, a cobrança e as configurações de segurança continuam com você.
- As chaves carregam escopos (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`), orçamentos diários e mensais de pontos, um teto por chamada e uma lista de IPs permitidos opcional. Dê ao agente a menor chave que dê conta do trabalho dele.
- Revogue qualquer chave em **My Account → API keys**; uma chave revogada é recusada em menos de um segundo. Cada chamada é registrada na sua conta com o respectivo custo.
- A skill lê apenas a sua própria conta: seus autopilots, suas execuções, suas chaves. Ela nunca opera uma conta real; as posições do autopilot são posições simuladas.

## Versões e atualizações

A skill informa a sua versão no cabeçalho `X-SimianX-Skill`. Quando a API deixa de aceitar uma versão, responde `426` com a URL a ser relida, e `GET /v1/skill` mostra sempre a versão atual e a mínima, além do [changelog](CHANGELOG.md). Atualize com o comando do próprio agente (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) ou execute de novo a frase acima.

## Estrutura do repositório

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

## Feedback e suporte

- De um agente: `POST /v1/feedback` (lido pela equipe; texto abusivo é recusado e nunca armazenado).
- De uma pessoa: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) para a skill, [simianx.ai/agents](https://www.simianx.ai/agents) para o produto.

Leia [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir um pull request e [SECURITY.md](SECURITY.md) para reportar uma vulnerabilidade.

## Licença

MIT para tudo neste repositório. O uso da API da SimianX é regido pelos [Termos de Serviço](https://www.simianx.ai/legal/terms). As análises da SimianX são informação, não recomendação de investimento; as posições do autopilot são posições simuladas.
