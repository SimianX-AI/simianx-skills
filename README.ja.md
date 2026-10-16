<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">AI エージェントのための SimianX AI</h1>

<p align="center">
  どの米国株や暗号資産ペアにも 4 人の AI アナリストが付き、スコア付きのニュースもストリームで届きます。
  Claude Code、Codex、Cursor をはじめ、スキルを読めるすべてのエージェントで使えます。
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">変更履歴</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <a href="README.th.md">ไทย</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <b>日本語</b> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## SimianX でできること

中心になるのは次の 2 つです。

- **マルチエージェントのライブ分析。** 銘柄か暗号資産ペアと時間足を指定すると、4 つのエージェントが同時に分析を始めます。チャートはインジケーター、ニュースの流れはインテリジェンス、開示資料とインサイダー取引（コインならオンチェーンとデリバティブのデータ）はファンダメンタルが担当。最後に意思決定エージェントが 3 つの見立てを比べ、エントリー・損切り・目標価格付きのトレード案を出します。→ [ライブ分析](https://www.simianx.ai/l)
- **スコア付きのニュースストリーム。** 記事はどれも、影響する銘柄、重要度のスコア、強気・弱気・中立の判定が付いた状態で届きます。マーケットパルスで急な値動き、高値・安値の更新、ギャップと並んで流れているのも、このフィードです。お使いのエージェントは、ページ送りで順に読むことも、担当銘柄のストリームを開いたままにしておくこともできます。→ [マーケットパルス](https://www.simianx.ai/pulse)

このほか、必要に応じて次の機能も使えます。

- **ディープリサーチ。** 8 つのエージェントが 1 つの銘柄やコインについて議論し、結論、トレードプラン、PDF を返します。お使いのエージェントから追加で質問することもできます。→ [ディープ分析](https://www.simianx.ai/c)
- **セクターウォッチ。** 一次情報から集めたカタリストのカレンダーとイベント。まずはバイオ医薬品から始めています。→ [セクターウォッチ](https://www.simianx.ai/sectors)
- **オートパイロット。** 同じ 4 つのライブエージェントが 1 つの銘柄をスケジュールどおりに分析し、仮想ポジションを管理します。動きはすべてイベントログに残り、お使いのエージェントがそれを追えます。→ [自動操縦装置](https://www.simianx.ai/autopilots)
- **モデルの選択。** 各エージェントの裏で動くモデルを自分で選べます。選ぶ前に、それぞれのモデルがこれまでどう取引してきたかも確かめられます。→ [モデルリーダーボード](https://www.simianx.ai/crypto-leaderboard)

対象市場：米国株と ETF が 13,000 銘柄以上（ローソク足は `1m`〜`1mo`）、暗号資産が現物と無期限先物あわせて 4,000 ペア以上（`1m`〜`1D`）。→ [株式分析](https://www.simianx.ai/c) · [暗号通貨分析](https://www.simianx.ai/l)

## 一文でインストール

エージェントにこの一文を貼ってください。

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

エージェントがスキルを所定の場所に入れ、そのままサインインまで進めます。ブラウザでリンクを承認するか、メールで届く 6 桁のコードを入力してください。初めてのメールアドレスなら、その場でアカウントが作られます。エージェントが受け取るのは専用の API キーで、`SIMIANX_API_KEY` に保存されます。ウェブサイトのログインがエージェントに渡ることはありません。

ターミナルから入れることもできます。

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

エージェントごと（Claude Code、Codex、Cursor、Copilot、Gemini CLI、Windsurf、Amp、Cline など）のコマンドとディレクトリは [INSTALL.md](INSTALL.md) にまとめています。

### MCP で接続する方法も

MCP に対応した AI エージェントなら、スキルを入れなくても SimianX をツールとして使えます。キーを添えてリモートサーバーを一度追加するだけです。

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

Claude Desktop、Cursor、Codex、VS Code、Windsurf、Gemini CLI での設定は [INSTALL.md](INSTALL.md#connect-over-mcp) にあります。レジストリ名：`io.github.SimianX-AI/simianx`。

## まず試す呼び出し

| やりたいこと | 呼び出し | リファレンス |
|---|---|---|
| ライブ分析を 1 回実行 | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 銘柄のニュースを取得 | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| ニュースを届いた瞬間に受け取る | `GET /v1/news/stream`（SSE、切れても続きから再開） | [news](skills/simianx/references/news.md) |
| マーケットパルス | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| ディープリサーチ | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| セクターウォッチ | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| オートパイロット | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

ベース URL は `https://service.simianx.ai/v1`、ヘッダーは `Authorization: Bearer $SIMIANX_API_KEY` です。同じ呼び出しをシェルスクリプトにしたものを [examples/curl](examples/curl) に置いています。

## プラン

Free、Starter、Plus、Pro があります。詳しくは[料金](https://www.simianx.ai/pricing)をご覧ください。エージェントからの呼び出しにはプランのポイントを使い、レートはウェブサイトと同じです。ニュースストリームは Plus と Pro ならリアルタイム、Plus 未満では 30 分遅れです。回答は 16 言語に対応しています。SimianX が実際の口座で取引することはなく、オートパイロットのポジションはすべて仮想ポジションです。

## セキュリティ

- キーは `SIMIANX_API_KEY` に置きます。スキルがキーをリポジトリ、ログ、プロンプトに書き込むことはありません。
- エージェントがウェブサイトのセッションを得ることはありません。エージェントからサインインしても、作られるのはそのエージェント用の API キーだけで、作成時にはメールでお知らせします。
- キーにはスコープ、1 日と 1 か月の予算、任意の IP 許可リストを設定できます。エージェントには、それぞれの仕事に足りる最小限のキーを渡してください。
- **マイアカウント → API キー** でキーを失効させると、1 秒以内に使えなくなります。

## バージョン

スキルは自分のバージョンを `X-SimianX-Skill` ヘッダーで送ります。サポートが終わったバージョンには、API が読み直す URL を添えて `426` を返します。現在のバージョンと最低バージョンは `GET /v1/skill` で確認できます。更新はエージェント自身のコマンドで行うか、上の一文をもう一度貼ってください。変更点は[変更履歴](CHANGELOG.md)にあります。

## リポジトリ構成

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

## フィードバック

- エージェントから：`POST /v1/feedback`。
- 人から：スキルについては [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues)、製品については [simianx.ai/agents](https://www.simianx.ai/agents) へ。

プルリクエストを送る前に [CONTRIBUTING.md](CONTRIBUTING.md) を、脆弱性の報告は [SECURITY.md](SECURITY.md) をお読みください。

## ライセンス

このリポジトリの内容はすべて MIT ライセンスです。SimianX API の利用には[利用規約](https://www.simianx.ai/legal/terms)が適用されます。SimianX の分析は情報であり、投資助言ではありません。
