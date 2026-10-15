<p align="center">
  <a href="https://www.simianx.ai">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/simianx-mark-light.svg">
      <img src="assets/simianx-mark-dark.svg" width="96" height="96" alt="SimianX AI">
    </picture>
  </a>
</p>

<h1 align="center">SimianX AI สำหรับ AI agent</h1>

<p align="center">
  สกิลเดียวที่เปลี่ยน Claude Code, Codex, Cursor, Copilot, Gemini CLI และ agent อื่น ๆ ทุกตัวที่อ่านสกิลได้ ให้กลายเป็นไคลเอนต์ของโต๊ะเทรด SimianX:
  autopilot พร้อมบันทึกเหตุการณ์ระดับการดำเนินคำสั่ง งานวิจัยเชิงลึก 8 agent การวิเคราะห์สด ข่าวที่จัดหมวดแล้ว และปัจจัยกระตุ้นรายกลุ่มอุตสาหกรรม
</p>

<p align="center">
  <a href="https://www.simianx.ai/agents">simianx.ai/agents</a> ·
  <a href="https://www.simianx.ai/SKILL.md">SKILL.md</a> ·
  <a href="https://www.simianx.ai/INSTALL.md">INSTALL.md</a> ·
  <a href="https://service.simianx.ai/v1/openapi.json">OpenAPI</a> ·
  <a href="CHANGELOG.md">บันทึกการเปลี่ยนแปลง</a>
</p>

<p align="center">
  <a href="https://github.com/SimianX-AI/simianx-skills/releases"><img alt="Release" src="https://img.shields.io/github/v/release/SimianX-AI/simianx-skills?label=release&color=0B1220"></a>
  <a href="https://skills.sh/SimianX-AI/simianx-skills"><img alt="skills.sh" src="https://skills.sh/b/SimianX-AI/simianx-skills"></a>
  <a href="LICENSE"><img alt="MIT" src="https://img.shields.io/badge/license-MIT-0B1220"></a>
</p>

<p align="center">
  <a href="README.md">English</a> · <a href="README.pt.md">Português</a> · <a href="README.es.md">Español</a> · <a href="README.hi.md">हिन्दी</a> · <a href="README.id.md">Bahasa Indonesia</a> · <a href="README.vi.md">Tiếng Việt</a> · <b>ไทย</b> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ja.md">日本語</a> · <a href="README.ko.md">한국어</a> · <a href="README.fil.md">Filipino</a> · <a href="README.ru.md">Русский</a> · <a href="README.fr.md">Français</a> · <a href="README.de.md">Deutsch</a> · <a href="README.tr.md">Türkçe</a>
</p>

---

## SimianX ครอบคลุมอะไรบ้าง

ทุกอย่างด้านล่างเข้าถึงได้ผ่านสกิลและอยู่บน [simianx.ai](https://www.simianx.ai); ลิงก์จะเปิดหน้าผลิตภัณฑ์ที่อยู่เบื้องหลังแต่ละความสามารถ

**ตลาด**

- **หุ้นและ ETF สหรัฐฯ** — ตราสารจดทะเบียน 13,000+ ตัว พร้อมผลประกอบการ เอกสารยื่นต่อทางการ ชุดข้อมูลการเงิน และการรับรู้เวลาทำการตลาด กรอบเวลา `1m 15m 1H 1D 1W 1mo` → [วิเคราะห์หุ้น](https://www.simianx.ai/stocks)
- **คริปโต** — เหรียญ 1,500+ เหรียญและคู่เทรด 4,000+ คู่บน OKX, Binance, Bybit และ Coinbase: ทั้ง spot และสัญญา perpetual swap แบบ USDT/USD (สัญลักษณ์เปล่าอย่าง `BTC` จะหมายถึงสัญญา perpetual) กรอบเวลา `1m 5m 15m 1H 4H 1D` → [วิเคราะห์คริปโตเคอร์เรนซี](https://www.simianx.ai/l)

**agent ทำอะไรได้บ้าง**

- **Autopilots** — agent สดทั้งสี่ตัวรันตามตารางเวลาบนสัญลักษณ์หนึ่งตัว และหากคุณอนุญาต จะบริหารโพซิชันจำลองให้ด้วย (เข้าตลาดแบบ market, limit และ stop, การเพิ่ม-ลดขนาด, stop-loss / take-profit, เกตจับจังหวะ) ทุกการวิเคราะห์ สัญญาณ และการเปลี่ยนแปลงโพซิชันจะถูกบันทึกลงบันทึกเหตุการณ์ที่คุณอ่านด้วย cursor; `signal.fired` และ `position.changed` มีเวลาหมดอายุกำกับ agent ของคุณยังเทรดสมุดนั้นด้วยตัวเองได้ → [ระบบนำทางอัตโนมัติ](https://www.simianx.ai/autopilots)
- **งานวิจัยเชิงลึก** — คณะกรรมการ 8 agent ต่อหนึ่งรอบ: นักวิเคราะห์สี่คน (หุ้น: fundamentals, market, news, timing · คริปโต: fundamentals, market, news, derivatives), bull researcher (ฝั่งมองขึ้น) หนึ่งคนและ bear researcher (ฝั่งมองลง) หนึ่งคน, research manager (ผู้จัดการงานวิจัย) ที่ดำเนินการอภิปราย และ risk manager (ผู้จัดการความเสี่ยง) ที่ออกบทสรุปและแผน กรอบระยะเวลา `short`, `swing`, `long`; ถามต่อได้; รายงาน PDF → [วิเคราะห์เชิงลึก](https://www.simianx.ai/c)
- **การวิเคราะห์สด** — agent สดทั้งสี่ตัว รันครั้งเดียว: **indicator** (อินดิเคเตอร์: แนวโน้ม โมเมนตัม โครงสร้างบนกราฟ), **intelligence** (ข่าวกรอง: กระแสข่าวและเรื่องเล่าของตลาด), **fundamental** (ปัจจัยพื้นฐาน: งบการเงินและเหตุการณ์ หรือ on-chain และอนุพันธ์สำหรับเหรียญ) และ **decision** (การตัดสินใจ: ข้อเสนอเทรดพร้อมจุดเข้า จุดหยุด และเป้าหมาย) → [วิเคราะห์สด](https://www.simianx.ai/l)
- **ข่าวที่จัดหมวดแล้ว** — ทุกบทความถูกให้คะแนนตามสัญลักษณ์ที่มันขยับ มูลค่า (`low` / `medium` / `high`) และอารมณ์ตลาด ดูได้แบบรายการ แบบรายบทความ แปลเป็น 16 ภาษา หรือแบบสตรีมสด → [เรื่องราว](https://www.simianx.ai/stories)
- **Market Pulse** — ราคาช็อกบนหน้าต่าง 1 นาที 5 นาที และ 15 นาที จุดสูงสุด/ต่ำสุด 24 ชั่วโมง / 30 วัน / 52 สัปดาห์ การเคลื่อนไหวรายวันและช่องว่างราคา (gap) ทั้งคริปโตและหุ้น พร้อมระดับความรุนแรง 1–4 → [ชีพจรตลาด](https://www.simianx.ai/pulse)
- **Sector Watch** — ปัจจัยกระตุ้นจากแหล่งข้อมูลปฐมภูมิของกลุ่มอุตสาหกรรม: ปฏิทิน (วัน PDUFA, คณะกรรมการที่ปรึกษา, การประกาศผลการทดลอง), เหตุการณ์พร้อมระดับความรุนแรง 1–4 และทิศทาง (การอนุมัติ, จดหมายตอบกลับฉบับสมบูรณ์, ผล topline, การขึ้นทะเบียนสถานะพิเศษ, การตรวจสอบโรงงาน, การอัปเดตฉลากยา…), หุ้นในกลุ่ม, สินทรัพย์ยา และการติดตาม เปิดให้ใช้แล้ววันนี้: **Biopharma · FDA approvals** (ชีวเภสัชภัณฑ์ · การอนุมัติของ FDA) สร้างจากเอกสารยื่นต่อ SEC, ประกาศของ FDA และ Federal Register, ClinicalTrials.gov และ openFDA → [จับตากลุ่มอุตสาหกรรม](https://www.simianx.ai/sectors)
- **โมเดลที่คุณเลือกเอง** — สาม tier (`fast`, `standard`, `frontier`) และโมเดล 50+ ตัวจาก 7 ผู้ให้บริการ ซึ่งแผนแบบชำระเงินตั้งค่าแยกต่อ agent ได้; แคตตาล็อกสาธารณะพร้อมราคาเป็นแต้ม → [แต้มและอัตรา](https://www.simianx.ai/points)
- **กระดานผู้นำ** — แต่ละโมเดลเทรดจริงได้ผลอย่างไร เพื่อให้ agent เลือกโมเดลตัดสินใจจากหลักฐาน → [กระดานผู้นำโมเดล AI คริปโต](https://www.simianx.ai/crypto-leaderboard)

**แผนและภาษา** — แผน Free, Starter, Plus และ Pro พร้อมแต้มรายเดือน ขีดจำกัดอัตราตามแผน และความหน่วงข้อมูล 30 นาทีสำหรับแผนต่ำกว่า Plus ([ราคา](https://www.simianx.ai/pricing)) API ตอบกลับได้ 16 ภาษา (`X-Language`) SimianX ไม่เทรดบัญชีจริง: โพซิชันของ autopilot เป็นโพซิชันจำลองที่คุณนำไปทำตามด้วยตัวรันของคุณเองได้

## ติดตั้งด้วยประโยคเดียว

วางประโยคนี้ให้ agent ของคุณ มันจะไปดึงคู่มือติดตั้ง วางสกิลไว้ในที่ที่ agent ของคุณอ่านสกิล แล้วขอคีย์จากคุณ:

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

ถนัดใช้คำสั่งมากกว่า? ทั้งสองแบบใช้ได้กับ agent ทุกตัวที่อ่านสกิลได้:

```bash
npx skills add SimianX-AI/simianx-skills          # universal installer (pick your agents interactively)
gh skill install SimianX-AI/simianx-skills simianx  # GitHub CLI, --agent <id> to target one agent
```

จากนั้นพูดว่า **"ลงชื่อเข้าใช้ SimianX ให้ฉันหน่อย"** agent จะส่งลิงก์ให้คุณอนุมัติในเบราว์เซอร์ หรือส่งรหัส 6 หลักไปทางอีเมล ไม่ว่าทางไหน มันจะได้รับคีย์ของตัวเองที่กำหนด scope และงบไว้แล้ว และเก็บไว้เป็น `SIMIANX_API_KEY` ยังไม่มีบัญชี? รหัสทางอีเมลจะสร้างบัญชีให้ คุณยังสร้างคีย์เองได้ที่ **บัญชีของฉัน → คีย์ API** บน [simianx.ai](https://www.simianx.ai) แล้ว export:

```bash
export SIMIANX_API_KEY=simx_live_...
```

## ติดตั้งสำหรับ agent ของคุณ

| Agent | วิธีติดตั้งแบบเนทีฟ | สกิลไปอยู่ที่ไหน |
|---|---|---|
| Claude Code | `/plugin marketplace add SimianX-AI/simianx-skills` จากนั้น `/plugin install simianx@simianx` | ปลั๊กอิน หรือ `~/.claude/skills/simianx` |
| OpenAI Codex | `codex plugin marketplace add SimianX-AI/simianx-skills` จากนั้น `/plugins` → **simianx** | `.agents/skills/simianx` |
| Cursor | Customize → *From GitHub Repository* → `SimianX-AI/simianx-skills` (หรือ `npx skills add SimianX-AI/simianx-skills -a cursor`) | `.agents/skills/simianx` · `~/.cursor/skills` |
| GitHub Copilot | `gh skill install SimianX-AI/simianx-skills simianx --agent github-copilot` | `.github/skills/simianx` · `~/.copilot/skills` |
| Gemini CLI | `gemini skills install https://github.com/SimianX-AI/simianx-skills.git --path skills/simianx --consent` | `~/.gemini/skills/simianx` |
| Windsurf / Devin | `npx skills add SimianX-AI/simianx-skills -a windsurf` | `.devin/skills/simianx` |
| Amp | `amp skill add SimianX-AI/simianx-skills` | `~/.config/agents/skills/simianx` |
| Cline · Roo Code · Kilo Code | `npx skills add SimianX-AI/simianx-skills -a cline` (หรือ `-a roo`, `-a kilo`) | `.cline/skills` · `.roo/skills` · `.kilo/skills` |
| OpenCode · Zed · Kiro · Factory Droid · OpenHands · Goose · Antigravity | `npx skills add SimianX-AI/simianx-skills -a <agent>` | `.agents/skills/simianx` |
| ตัวอื่น ๆ | คัดลอก `skills/simianx/` ไปไว้ในไดเรกทอรีที่ agent ของคุณสแกน หรือรัน `scripts/install.sh --agent auto` | ดู [INSTALL.md](INSTALL.md) |

[INSTALL.md](INSTALL.md) ระบุไดเรกทอรีและบรรทัดคำสั่งเชลล์ที่แน่นอนของแต่ละไคลเอนต์; `scripts/install.sh` (หรือ `install.py`; บน Windows: `install.ps1`) จะตรวจหา agent ที่ติดตั้งไว้ แล้วคัดลอกหรือลิงก์สกิลให้คุณเอง

## agent ของคุณทำอะไรได้บ้าง

| ต้องการ | เรียก | เอกสารอ้างอิง |
|---|---|---|
| เริ่มและติดตาม autopilot บนหุ้นหรือเหรียญหนึ่งตัว | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |
| เทรดสมุดจำลองของ autopilot ด้วยตัวเอง | `POST /v1/autopilots/{id}/actions` (`open`, `add`, `reduce`, `close`, `set_levels`, `place_order`, `replace_order`, `cancel_order`, `set_timeframe`) | [autopilots](skills/simianx/references/autopilots.md) |
| รัน agent หนึ่งตัวทันที | `POST /v1/autopilots/{id}/run {"agent": "decision"}` | [autopilots](skills/simianx/references/autopilots.md) |
| งานวิจัยเชิงลึก 8 agent พร้อมบทสรุปและแผน | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| agent สด แบบรันครั้งเดียว | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| ข่าวที่จัดหมวดแล้ว (สัญลักษณ์ มูลค่า อารมณ์ตลาด) แบบรายการหรือสตรีม | `GET /v1/news` · `GET /v1/news/stream` | [news](skills/simianx/references/news.md) |
| ปัจจัยกระตุ้นรายกลุ่มอุตสาหกรรม: ปฏิทิน เหตุการณ์ หุ้นในกลุ่ม การติดตาม | `GET /v1/sectors` · `/{sector}/calendar` · `/{sector}/events` | [sectors](skills/simianx/references/sectors.md) |
| แท่งเทียนคริปโต อินดิเคเตอร์ ราคา Market Pulse | `GET /v1/market/{symbol}/candles` · `/indicators` · `/v1/quotes` · `/v1/pulse/events` | [data](skills/simianx/references/data.md) |
| โมเดลที่ตั้งค่าได้ต่อ agent ราคา และบัญชีของคุณ | `GET /v1/models` · `GET /v1/pricing` · `GET /v1/me` · `POST /v1/analysis/quote` | [billing](skills/simianx/references/billing.md) |

ทุกเหตุการณ์ในบันทึกของ autopilot มี cursor กำกับ และสำหรับเหตุการณ์ที่ agent อาจนำไปลงมือทำ (`signal.fired`, `position.changed`) ยังมีเวลาหมดอายุกำกับด้วย ตัวรันจึงไม่มีวันลงมือจากข้อมูลที่ล้าสมัย การอ่านเหตุการณ์ฟรี คุณจ่ายเฉพาะค่าวิเคราะห์ เป็นแต้มที่แผนของคุณมีอยู่แล้ว

## เซสชันแรก

1. `GET https://service.simianx.ai/v1/skill` — สาธารณะ ใช้ยืนยันว่าเวอร์ชันสกิลที่ agent ของคุณถืออยู่ยังเป็นที่ยอมรับ
2. `GET /v1/me` พร้อม `Authorization: Bearer $SIMIANX_API_KEY` — แผน แต้มคงเหลือ ขีดจำกัด
3. `POST /v1/analysis/quote` — การเรียกหนึ่งครั้งจะมีค่าใช้จ่ายเท่าไร ก่อนจ่ายจริง
4. `POST /v1/autopilots` พร้อม `{"asset": "crypto", "symbol": "BTC", "timeframe": "15m", "tier": "fast"}` — จากนั้น long-poll บันทึกเหตุการณ์จาก cursor ที่คำตอบส่งกลับมา

ลูปเต็มในรูปแบบ `curl` อยู่ที่ [examples/curl](examples/curl); ตัวรันขนาดเล็กที่ทำงานตลอดเวลาและรันคำสั่งหรือ webhook ของคุณทุกครั้งที่โพซิชันเปลี่ยน อยู่ที่ [examples/runner](examples/runner)

## แต้ม ไม่ใช่เครดิต

- ทุกอย่างคิดเป็น**แต้ม**จากแผนสมาชิกของบัญชี ไม่มีการเติมเงิน และไม่มีการจ่ายรายครั้ง
- endpoint ด้าน AI คิดตามโมเดลที่ใช้จริง; `GET /v1/pricing` เผยแพร่ค่าใช้จ่ายตามปกติของแต่ละ tier (`fast`, `standard`, `frontier`) และ `GET /v1/models` เผยแพร่ราคาของทุกโมเดลที่ agent เลือกได้
- endpoint ด้านข้อมูลคิดต่อคำขอ (เศษส่วนของหนึ่งแต้ม); บันทึกเหตุการณ์, `/v1/me`, `/v1/skill`, `/v1/pricing` และ `/v1/models` ไม่มีค่าใช้จ่าย
- `402` หมายถึงแต้มหรืองบของคีย์หมด และบอกทางออกไว้ด้วย (`renew_now`, `change_plan`, `subscribe`); `429` คือการจำกัดอัตราและมาพร้อม `Retry-After` นอกจากนี้ไม่มีอะไรเป็นปัญหาเรื่องการชำระเงิน

## ความปลอดภัย

- คีย์อยู่ในตัวแปรสภาพแวดล้อม `SIMIANX_API_KEY` สกิลไม่มีวันขอให้ agent เขียนคีย์ลงในรีโพซิทอรี ล็อก หรือพรอมต์
- agent ไม่มีวันได้รับเซสชันของเว็บไซต์ การลงชื่อเข้าใช้จาก agent (ลิงก์ในเบราว์เซอร์หรือรหัสทางอีเมล) จะสร้างได้แค่คีย์ API สำหรับ agent ตัวนั้นเท่านั้น โดยมีอีเมลแจ้งและแสดงอยู่ในกิจกรรมด้านความปลอดภัยของคุณ ส่วนเว็บไซต์ การเรียกเก็บเงิน และการตั้งค่าความปลอดภัยยังอยู่กับคุณ
- คีย์มี scope (`data:read`, `analysis:run`, `automation:manage`, `keys:manage`) งบแต้มรายวันและรายเดือน เพดานต่อการเรียกหนึ่งครั้ง และรายการ IP ที่อนุญาต (ไม่บังคับ) ให้ agent ใช้คีย์ที่เล็กที่สุดเท่าที่พอทำงานได้
- เพิกถอนคีย์ใดก็ได้ที่ **บัญชีของฉัน → คีย์ API**; คีย์ที่ถูกเพิกถอนจะถูกปฏิเสธภายในหนึ่งวินาที ทุกการเรียกถูกบันทึกไว้ใต้บัญชีของคุณพร้อมค่าใช้จ่าย
- สกิลอ่านได้เฉพาะบัญชีของคุณเอง: autopilot ของคุณ การรันของคุณ คีย์ของคุณ มันไม่มีวันเทรดบัญชีจริง; โพซิชันของ autopilot เป็นโพซิชันจำลอง

## เวอร์ชันและการอัปเดต

สกิลรายงานเวอร์ชันของตัวเองในเฮดเดอร์ `X-SimianX-Skill` เมื่อ API ไม่รับเวอร์ชันนั้นอีกต่อไป จะตอบ `426` พร้อม URL ที่ต้องไปอ่านใหม่ และ `GET /v1/skill` จะแสดงเวอร์ชันปัจจุบันและเวอร์ชันขั้นต่ำเสมอ พร้อม[บันทึกการเปลี่ยนแปลง](CHANGELOG.md) อัปเดตด้วยคำสั่งของ agent เอง (`npx skills update`, `gh skill update --all`, `/plugin marketplace update simianx`, …) หรือรันประโยคเดียวด้านบนอีกครั้ง

## โครงสร้างรีโพซิทอรี

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

## ฟีดแบ็กและการสนับสนุน

- จาก agent: `POST /v1/feedback` (ทีมงานอ่านเอง; ข้อความหยาบคายจะถูกปฏิเสธและไม่ถูกเก็บไว้)
- จากคน: [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) สำหรับเรื่องสกิล, [simianx.ai/agents](https://www.simianx.ai/agents) สำหรับเรื่องผลิตภัณฑ์

อ่าน [CONTRIBUTING.md](CONTRIBUTING.md) ก่อนเปิด pull request และดู [SECURITY.md](SECURITY.md) เพื่อรายงานช่องโหว่

## สัญญาอนุญาต

MIT สำหรับทุกอย่างในรีโพซิทอรีนี้ การใช้ SimianX API อยู่ภายใต้[ข้อกำหนดการให้บริการ](https://www.simianx.ai/legal/terms) การวิเคราะห์ของ SimianX เป็นข้อมูล ไม่ใช่คำแนะนำการลงทุน; โพซิชันของ autopilot เป็นโพซิชันจำลอง
