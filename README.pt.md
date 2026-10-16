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
  Quatro analistas de IA para qualquer ação dos EUA ou par cripto, e um fluxo de notícias já avaliadas,
  direto no Claude Code, no Codex, no Cursor e em qualquer outro agente que leia skills.
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

## O que o SimianX faz

Duas funções fazem quase todo o trabalho.

- **Análise multiagente ao vivo.** Escolha uma ação ou um par cripto e um tempo gráfico, e quatro agentes começam a analisar ao mesmo tempo. O agente de Indicador lê o gráfico. O de Inteligência acompanha o noticiário. O Fundamental lê documentos regulatórios e negociações de insiders ou, se for uma moeda, dados on-chain e de derivativos. O de Decisão pesa os três e propõe uma operação com entrada, stop e alvo. → [Análise ao vivo](https://www.simianx.ai/l)
- **Um fluxo de notícias avaliadas.** Cada artigo já chega marcado com os ativos que ele move, uma nota de importância e um viés altista, baixista ou neutro. É o feed por trás do Pulso do Mercado, onde aparece ao lado de movimentos bruscos de preço, novas máximas e mínimas e gaps. Seu agente pode percorrer as notícias página por página ou deixar um stream aberto nos ativos dele. → [Pulso do Mercado](https://www.simianx.ai/pulse)

Também à mão quando você precisar:

- **Pesquisa profunda.** Oito agentes debatem uma ação ou uma moeda e voltam com um veredito, um plano de operação e um PDF. Seu agente pode fazer perguntas depois. → [Análise profunda](https://www.simianx.ai/c)
- **Setores em Foco.** Calendários de catalisadores e eventos tirados de fontes primárias, começando pelo setor biofarmacêutico. → [Setores em Foco](https://www.simianx.ai/sectors)
- **Pilotos automáticos.** Os mesmos quatro agentes ao vivo trabalham em horários definidos sobre um único ativo, cuidam de uma posição simulada e deixam um registro de eventos que seu agente pode acompanhar. → [Pilotos automáticos](https://www.simianx.ai/autopilots)
- **Você escolhe o modelo.** Defina o modelo por trás de cada agente e veja antes como cada um já operou. → [Ranking de modelos](https://www.simianx.ai/crypto-leaderboard)

Mercados: mais de 13.000 ações e ETFs dos EUA, com velas de `1m` a `1mo`, e mais de 4.000 pares cripto, à vista e perpétuos, de `1m` a `1D`. → [Análise de Ações](https://www.simianx.ai/c) · [Análise de Criptomoedas](https://www.simianx.ai/l)

## Instale com uma frase

Cole isto no seu agente:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

O agente coloca a skill onde costuma procurar skills e depois faz o seu login: você aprova um link no navegador ou digita o código de 6 dígitos que mandamos por e-mail. Se o e-mail for novo, a conta é criada na hora. No fim, o agente fica com uma chave de API só dele em `SIMIANX_API_KEY`, nunca com o seu login do site.

Se preferir o terminal:

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

O comando e o diretório de cada agente (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline e os demais) estão no [INSTALL.md](INSTALL.md).

### Ou conecte por MCP

Agentes de IA que falam MCP podem usar a SimianX como ferramentas sem instalar a skill. Adicione o servidor remoto uma vez com sua chave:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

O mesmo para Claude Desktop, Cursor, Codex, VS Code, Windsurf e Gemini CLI está em [INSTALL.md](INSTALL.md#connect-over-mcp). Nome no registro: `io.github.SimianX-AI/simianx`.

## Primeiras chamadas

| O quê | Chamada | Referência |
|---|---|---|
| Rodar uma análise ao vivo | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| Notícias dos seus ativos | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| Notícias assim que saem | `GET /v1/news/stream` (server-sent events, retoma se a conexão cair) | [news](skills/simianx/references/news.md) |
| Pulso do Mercado | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| Pesquisa profunda | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| Setores em Foco | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| Pilotos automáticos | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

URL base `https://service.simianx.ai/v1`, cabeçalho `Authorization: Bearer $SIMIANX_API_KEY`. As mesmas chamadas, em scripts de shell, estão em [examples/curl](examples/curl).

## Planos

Free, Starter, Plus e Pro (veja os [preços](https://www.simianx.ai/pricing)). As chamadas do agente usam os pontos do seu plano, com as mesmas tarifas do site. O fluxo de notícias é em tempo real no Plus e no Pro; abaixo do Plus, as notícias chegam com 30 minutos de atraso. A API responde em 16 idiomas. O SimianX nunca opera uma conta real: as posições dos pilotos automáticos são simuladas.

## Segurança

- A chave fica em `SIMIANX_API_KEY`. A skill nunca a grava em repositório, log ou prompt.
- Um agente nunca recebe uma sessão do site. Fazer login por um agente só cria uma chave de API para ele, e avisamos você por e-mail quando isso acontece.
- As chaves têm escopos, orçamentos diários e mensais e uma lista opcional de IPs permitidos. Dê a cada agente a chave mais restrita que dê conta do trabalho.
- Revogue uma chave em **Minha Conta → Chaves de API** e ela para de funcionar em menos de um segundo.

## Versões

A skill envia a própria versão no cabeçalho `X-SimianX-Skill`. Quando uma versão é desativada, a API responde `426` com a URL que deve ser lida de novo, e `GET /v1/skill` mostra a versão atual e a mínima. Atualize com o comando do seu agente ou cole de novo a frase acima. O que mudou está no [histórico de alterações](CHANGELOG.md).

## Estrutura do repositório

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

## Feedback

- De um agente: `POST /v1/feedback`.
- De uma pessoa: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) para a skill, [simianx.ai/agents](https://www.simianx.ai/agents) para o produto.

Leia o [CONTRIBUTING.md](CONTRIBUTING.md) antes de abrir um pull request e o [SECURITY.md](SECURITY.md) para reportar uma vulnerabilidade.

## Licença

Tudo neste repositório está sob a licença MIT. O uso da API do SimianX segue os [Termos de Serviço](https://www.simianx.ai/legal/terms). As análises do SimianX são informação, não recomendação de investimento.
