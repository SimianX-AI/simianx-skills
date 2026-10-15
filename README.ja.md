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
  Claude Code、Codex、Cursor、Copilot、Gemini CLI、そしてスキルを読み込めるあらゆるエージェントを、ひとつのスキルで SimianX トレーディングデスクのクライアントに変えます:
  実行グレードのイベントログを備えたオートパイロット、8 エージェントによるディープリサーチ、ライブ分析、分類済みニュース、セクターカタリスト。
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

## SimianX がカバーする範囲

以下はすべてスキル経由で利用でき、[simianx.ai](https://www.simianx.ai) 上で提供されています。各リンクは、その機能の背後にあるプロダクトページを開きます。

**市場**

- **米国株と ETF** — 13,000 以上の上場銘柄。決算、開示書類、財務時系列データ、取引時間の認識を備えています。時間足は `1m 15m 1H 1D 1W 1mo`。 → [株式分析](https://www.simianx.ai/stocks)
- **暗号資産** — OKX、Binance、Bybit、Coinbase にまたがる 1,500 以上のコインと 4,000 以上のペア。現物と USDT/USD 無期限スワップ(`BTC` のようにシンボルだけを指定すると無期限スワップとして解決されます)。時間足は `1m 5m 15m 1H 4H 1D`。 → [暗号通貨分析](https://www.simianx.ai/l)

**エージェントが行うこと**

- **オートパイロット** — 4 つのライブエージェントが 1 つのシンボルに対してスケジュール実行され、許可すればペーパーポジションを管理します(成行・指値・逆指値のエントリー、分割売買、ストップロス / テイクプロフィット、タイミングゲート)。すべての分析、シグナル、ポジション変更はカーソルで読み取るイベントログに記録され、`signal.fired` と `position.changed` には有効期限が付きます。あなたのエージェントがそのブックを手動で売買することもできます。 → [自動操縦装置](https://www.simianx.ai/autopilots)
- **ディープリサーチ** — 1 回の実行につき 8 エージェントの委員会: 4 人のアナリスト(株式: fundamentals, market, news, timing · 暗号資産: fundamentals, market, news, derivatives)、bull researcher と bear researcher(強気派・弱気派のリサーチャー)、議論を仕切る research manager(リサーチマネージャー)、そして判定とプランを出す risk manager(リスクマネージャー)。期間は `short`、`swing`、`long`。追加質問と PDF レポートに対応。 → [ディープ分析](https://www.simianx.ai/c)
- **ライブ分析** — 4 つのライブエージェントを 1 回だけ実行: **indicator**(インジケーター: チャート上のトレンド、モメンタム、構造)、**intelligence**(インテリジェンス: ニュースフローとナラティブ)、**fundamental**(ファンダメンタル: 財務とイベント、コインの場合はオンチェーンとデリバティブ)、**decision**(ディシジョン: エントリー、ストップ、ターゲットを含む取引提案)。 → [ライブ分析](https://www.simianx.ai/l)
- **分類済みニュース** — すべての記事を、影響する銘柄、バリュー(`low` / `medium` / `high`)、センチメントでスコアリング。リスト形式、記事単位、16 言語への翻訳、ライブストリームのいずれでも取得できます。 → [ストーリー](https://www.simianx.ai/stories)
- **Market Pulse** — 1 分・5 分・15 分ウィンドウでの価格急変、24 時間 / 30 日 / 52 週の高値・安値、日中の値動きとギャップを、暗号資産と株式の両方で重大度 1–4 付きで検出します。 → [マーケットパルス](https://www.simianx.ai/pulse)
- **Sector Watch** — セクターの一次情報に基づくカタリスト: カレンダー(PDUFA 期日、諮問委員会、治験結果の公表)、重大度 1–4 と方向性を持つイベント(承認、審査完了報告書、トップライン結果、指定、査察、添付文書の更新など)、構成銘柄、医薬品アセット、フォロー。現在提供中: **Biopharma · FDA approvals**。SEC の開示書類、FDA と Federal Register の公表、ClinicalTrials.gov、openFDA から構築しています。 → [セクターウォッチ](https://www.simianx.ai/sectors)
- **選べるモデル** — 3 つのティア(`fast`、`standard`、`frontier`)と 7 プロバイダー 50 以上のモデル。有料プランではエージェントごとに設定できます。ポイント建て価格の公開カタログあり。 → [ポイントとレート](https://www.simianx.ai/points)
- **リーダーボード** — 各モデルが実際にどう取引してきたかを示すので、エージェントは根拠に基づいて判定モデルを選べます。 → [暗号通貨AIモデルリーダーボード](https://www.simianx.ai/crypto-leaderboard)

**プランと言語** — Free、Starter、Plus、Pro の各プランには月間ポイントとプランごとのレート制限が付き、Plus 未満では 30 分のデータ遅延があります([料金](https://www.simianx.ai/pricing))。API は 16 言語で応答します(`X-Language`)。SimianX は実口座で取引しません。オートパイロットのポジションはペーパーポジションであり、あなた自身のランナーでミラーできます。

## 一文でインストール

これをエージェントに貼り付けてください。インストールガイドを取得し、エージェントがスキルを読む場所にスキルを配置し、キーの入力を求めます:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

コマンドの方がよければ、どちらもスキルを読み込めるすべてのエージェントで動作します:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

次に **"SimianX にサインインして"** と伝えます。エージェントはブラウザで承認するリンクを渡すか、6 桁のコードをメールで送ります。どちらの場合も、エージェントはスコープと予算の付いた自分専用のキーを受け取り、`SIMIANX_API_KEY` として保存します。アカウントがまだない場合は、メールのコードで作成されます。[simianx.ai](https://www.simianx.ai) の **私のアカウント → API キー** で手動でキーを作成し、エクスポートすることもできます:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## エージェント別のインストール

| エージェント | ネイティブな手順 | スキルの配置先 |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` の後に `/plugin install simianx@simianx` | プラグイン、または `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` の後に `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills`(または `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline`(または `-a roo`、`-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| その他 | `skills/simianx/` をエージェントがスキャンするディレクトリにコピーするか、`scripts/install.sh --agent auto` を実行 | [INSTALL.md](INSTALL.md) を参照 |

[INSTALL.md](INSTALL.md) には各クライアントの正確なディレクトリとシェルコマンドが載っています。`scripts/install.sh`(Windows では `install.py`: `install.ps1`)はインストール済みのエージェントを検出し、スキルをコピーまたはリンクしてくれます。

## エージェントにできること

| 用途 | 呼び出し | リファレンス |
|---|---|---|
| 株式や暗号資産のオートパイロットを起動して追跡する | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| オートパイロットのペーパーブックを手動で売買する | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| エージェントを 1 つ今すぐ実行する | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| 判定とプランを伴う 8 エージェントのディープリサーチ | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| ライブエージェントを 1 回だけ実行する | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| 分類済みニュース(銘柄、バリュー、センチメント)をリストまたはストリームで | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| セクターカタリスト: カレンダー、イベント、構成銘柄、フォロー | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| 暗号資産のローソク足、指標、気配値、Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| エージェントごとに設定できるモデル、価格、アカウント情報 | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

オートパイロットログのすべてのイベントにはカーソルが付き、エージェントが行動を起こしうるもの(`signal.fired`、`position.changed`)には有効期限スタンプが付くため、ランナーが古い情報で動くことはありません。イベントの読み取りは無料です。料金が発生するのは分析だけで、プランにすでに含まれているポイントで支払います。

## 最初のセッション

1. `GET https://service.simianx.ai/v1/skill` ― 公開エンドポイント。エージェントが持つスキルのバージョンがまだ受け付けられるかを確認します。
2. `GET /v1/me`(`Authorization: Bearer $SIMIANX_API_KEY` 付き)― プラン、残りポイント、制限。
3. `POST /v1/analysis/quote` ― 支払う前に、その呼び出しのコストを確認。
4. `POST /v1/autopilots` に `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` を渡す ― その後、レスポンスで返るカーソルからイベントログをロングポーリング。

`curl` によるループ全体は [examples/curl](examples/curl) に、ポジションが変わるたびにコマンドや Webhook を実行する小さな常時稼働ランナーは [examples/runner](examples/runner) にあります。

## 課金はポイントのみ

- すべての課金は、アカウントのサブスクリプションに含まれる **ポイント** で行われます。チャージも従量課金もありません。
- AI エンドポイントは実際に使用したモデルに基づいて計量されます。`GET /v1/pricing` はティア(`fast`、`standard`、`frontier`)ごとの標準的なコストを、`GET /v1/models` はエージェントが選択できる各モデルの価格を公開しています。
- データエンドポイントはリクエスト単位(1 ポイントの何分の一か)で課金されます。イベントログ、`/v1/me`、`/v1/skill`、`/v1/pricing`、`/v1/models` は無料です。
- `402` はポイントまたはキーの予算が尽きたことを意味し、解決方法(`renew_now`、`change_plan`、`subscribe`)を示します。`429` はレート制限で、`Retry-After` を伴います。それ以外が支払いの問題になることはありません。

## セキュリティ

- キーは環境変数 `SIMIANX_API_KEY` に置きます。このスキルがエージェントにキーをリポジトリ、ログ、プロンプトへ書き込ませることは決してありません。
- エージェントがウェブサイトのセッションを得ることは決してありません。エージェントからのサインイン(ブラウザのリンクまたはメールのコード)は、そのエージェント用の API キーを作成するだけです。作成はメールで通知され、セキュリティアクティビティにも記録されます。ウェブサイト、請求、セキュリティ設定はあなたの手元に残ります。
- キーにはスコープ(`data:read`、`analysis:run`、`automation:manage`、`keys:manage`)、日次・月次のポイント予算、1 回の呼び出しあたりの上限、任意の IP 許可リストが設定できます。エージェントには、その仕事に必要な最小限のキーを渡してください。
- キーの失効は **私のアカウント → API キー** からいつでも行えます。失効したキーは 1 秒以内に拒否されます。すべての呼び出しはコストとともにあなたのアカウントに記録されます。
- このスキルが読むのはあなた自身のアカウントだけです: あなたのオートパイロット、あなたの実行、あなたのキー。実際の口座で取引することは決してなく、オートパイロットのポジションはペーパーポジションです。

## バージョンと更新

スキルは自身のバージョンを `X-SimianX-Skill` ヘッダーで報告します。API がそのバージョンを受け付けなくなると、再読み込みすべき URL を添えて `426` を返します。また `GET /v1/skill` は常に現在のバージョンと最低バージョン、そして[変更履歴](CHANGELOG.md)を示します。更新はエージェント自身のコマンド(`npx skills update`、`gh skill update --all`、`/plugin marketplace update simianx` など)で行うか、上の一文をもう一度実行してください。

## リポジトリ構成

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

## フィードバックとサポート

- エージェントから: `POST /v1/feedback`(チームが読みます。暴言は拒否され、保存されることもありません)。
- 人から: スキルについては [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues)、製品については [simianx.ai/agents](https://www.simianx.ai/agents)。

プルリクエストを開く前に [CONTRIBUTING.md](CONTRIBUTING.md) を、脆弱性の報告には [SECURITY.md](SECURITY.md) をご覧ください。

## ライセンス

このリポジトリ内のすべては MIT ライセンスです。SimianX API の利用は[利用規約](https://www.simianx.ai/legal/terms)に従います。SimianX の分析は情報であり、投資助言ではありません。オートパイロットのポジションはペーパーポジションです。
