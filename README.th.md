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
  นักวิเคราะห์ AI สี่คนช่วยกันดูหุ้นสหรัฐฯ หรือคู่คริปโตตัวไหนก็ได้ พร้อมสตรีมข่าวที่ให้คะแนนแล้ว
  ใช้ได้กับ Claude Code, Codex, Cursor และเอเจนต์ทุกตัวที่อ่านสกิลได้
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

## SimianX ทำอะไรได้บ้าง

งานส่วนใหญ่อยู่ที่สองอย่างนี้

- **วิเคราะห์สดด้วยเอเจนต์หลายตัว** เลือกหุ้นหรือคู่คริปโตกับไทม์เฟรม แล้วเอเจนต์สี่ตัวจะเริ่มวิเคราะห์พร้อมกัน เอเจนต์ตัวชี้วัดดูกราฟ เอเจนต์ข่าวกรองตามกระแสข่าว เอเจนต์ปัจจัยพื้นฐานดูเอกสารที่บริษัทยื่นและการซื้อขายของผู้บริหาร หรือข้อมูลบนเชนกับอนุพันธ์ถ้าเป็นเหรียญ แล้วเอเจนต์ตัดสินใจจะชั่งน้ำหนักทั้งสามมุมและเสนอเทรดพร้อมจุดเข้า จุดตัดขาดทุน และเป้าหมาย → [การวิเคราะห์สด](https://www.simianx.ai/l)
- **สตรีมข่าวที่ให้คะแนนแล้ว** ทุกบทความเข้ามาพร้อมแท็กสัญลักษณ์ที่ข่าวนั้นกระทบ คะแนนความสำคัญ และมุมมองขาขึ้น ขาลง หรือเป็นกลาง ข่าวที่เห็นในชีพจรตลาดก็มาจากฟีดนี้ แสดงคู่กับราคาที่ขยับแรงฉับพลัน จุดสูงสุดและต่ำสุดใหม่ และช่องว่างราคา เอเจนต์ของคุณจะไล่อ่านทีละหน้า หรือเปิดสตรีมค้างไว้กับสัญลักษณ์ที่ติดตามก็ได้ → [ชีพจรตลาด](https://www.simianx.ai/pulse)

มีให้ใช้เพิ่มเมื่อต้องการ

- **วิเคราะห์เชิงลึก** เอเจนต์แปดตัวถกเถียงกันเรื่องหุ้นหรือเหรียญหนึ่งตัว แล้วส่งกลับมาเป็นข้อสรุป แผนเทรด และไฟล์ PDF เอเจนต์ของคุณถามต่อได้ → [การวิเคราะห์เชิงลึก](https://www.simianx.ai/c)
- **จับตากลุ่มอุตสาหกรรม** ปฏิทินและเหตุการณ์ปัจจัยเร่งจากแหล่งข้อมูลปฐมภูมิ เริ่มจากกลุ่มยาและไบโอเทค → [จับตากลุ่มอุตสาหกรรม](https://www.simianx.ai/sectors)
- **ออโตไพลอต** เอเจนต์สี่ตัวชุดเดียวกับการวิเคราะห์สด ทำงานตามตารางเวลากับสัญลักษณ์เดียว พร้อมสถานะจำลองและบันทึกเหตุการณ์ที่เอเจนต์ของคุณตามอ่านได้ → [ระบบนำทางอัตโนมัติ](https://www.simianx.ai/autopilots)
- **เลือกโมเดลเองได้** กำหนดโมเดลให้เอเจนต์แต่ละตัว และดูก่อนได้ว่าแต่ละโมเดลเคยเทรดได้ผลอย่างไร → [กระดานผู้นำโมเดล](https://www.simianx.ai/crypto-leaderboard)

ตลาด: หุ้นและ ETF สหรัฐฯ กว่า 13,000 ตัว แท่งเทียนตั้งแต่ `1m` ถึง `1mo` และคู่คริปโตกว่า 4,000 คู่ ทั้งสปอตและ perpetual แท่งเทียนตั้งแต่ `1m` ถึง `1D` → [วิเคราะห์หุ้น](https://www.simianx.ai/c) · [วิเคราะห์คริปโตเคอร์เรนซี](https://www.simianx.ai/l)

## ติดตั้งด้วยประโยคเดียว

วางประโยคนี้ให้เอเจนต์ของคุณ

```text
Install the SimianX skill from https://www.simianx.ai/INSTALL.md and set it up for this project.
```

เอเจนต์จะติดตั้งสกิลไว้ในที่ที่มันมองหาสกิล แล้วพาคุณลงชื่อเข้าใช้ โดยกดอนุมัติลิงก์ในเบราว์เซอร์ หรือพิมพ์รหัส 6 หลักที่เราส่งไปทางอีเมล ถ้าเป็นอีเมลใหม่ ระบบจะสร้างบัญชีให้ทันที สุดท้ายเอเจนต์จะมีคีย์ API ของตัวเองอยู่ใน `SIMIANX_API_KEY` และไม่มีวันได้ข้อมูลล็อกอินเว็บไซต์ของคุณ

หรือติดตั้งจากเทอร์มินัล

```bash
npx skills add SimianX-AI/simianx-skills
gh skill install SimianX-AI/simianx-skills simianx
```

คำสั่งและไดเรกทอรีของเอเจนต์แต่ละตัว (Claude Code, Codex, Cursor, Copilot, Gemini CLI, Windsurf, Amp, Cline และตัวอื่น ๆ) อยู่ใน [INSTALL.md](INSTALL.md)

### หรือเชื่อมต่อผ่าน MCP

AI เอเจนต์ที่รองรับ MCP ใช้ SimianX เป็นเครื่องมือได้โดยไม่ต้องติดตั้งสกิล เพิ่มเซิร์ฟเวอร์ระยะไกลครั้งเดียวพร้อมคีย์ของคุณ:

```bash
claude mcp add --transport http simianx https://service.simianx.ai/v1/mcp --header "Authorization: Bearer $SIMIANX_API_KEY"
```

วิธีเดียวกันสำหรับ Claude Desktop, Cursor, Codex, VS Code, Windsurf และ Gemini CLI อยู่ใน [INSTALL.md](INSTALL.md#connect-over-mcp) ชื่อในรีจิสทรี: `io.github.SimianX-AI/simianx`

## เริ่มจากการเรียกเหล่านี้

| ต้องการ | การเรียก | เอกสาร |
|---|---|---|
| วิเคราะห์สดหนึ่งครั้ง | `POST /v1/analysis/live` → `GET /v1/analysis/live/{id}?wait=30` | [live](skills/simianx/references/live.md) |
| ข่าวของสัญลักษณ์ที่ติดตาม | `GET /v1/news?symbols=NVDA&min_value=medium` | [news](skills/simianx/references/news.md) |
| ข่าวทันทีที่เข้ามา | `GET /v1/news/stream` (SSE ต่อจากจุดเดิมได้ถ้าหลุด) | [news](skills/simianx/references/news.md) |
| ชีพจรตลาด | `GET /v1/pulse/events` | [data](skills/simianx/references/data.md) |
| วิเคราะห์เชิงลึก | `POST /v1/analysis/deep` → `/events` · `/ask` · `/pdf` | [deep](skills/simianx/references/deep.md) |
| จับตากลุ่มอุตสาหกรรม | `GET /v1/sectors/{sector}/calendar` · `/events` | [sectors](skills/simianx/references/sectors.md) |
| ออโตไพลอต | `POST /v1/autopilots` → `GET /v1/autopilots/{id}/events?after=<cursor>&wait=30` | [autopilots](skills/simianx/references/autopilots.md) |

Base URL คือ `https://service.simianx.ai/v1` และเฮดเดอร์คือ `Authorization: Bearer $SIMIANX_API_KEY` การเรียกชุดเดียวกันในรูปสคริปต์เชลล์อยู่ที่ [examples/curl](examples/curl)

## แผน

มีแผน Free, Starter, Plus และ Pro ดูรายละเอียดได้ที่หน้า[ราคา](https://www.simianx.ai/pricing) การเรียกจากเอเจนต์ใช้แต้มในแผนของคุณ ในอัตราเดียวกับบนเว็บไซต์ สตรีมข่าวเป็นแบบสดในแผน Plus และ Pro ส่วนแผนที่ต่ำกว่า Plus ข่าวจะช้ากว่า 30 นาที คำตอบมีให้เลือก 16 ภาษา SimianX ไม่เทรดบัญชีจริง สถานะของออโตไพลอตเป็นสถานะจำลองทั้งหมด

## ความปลอดภัย

- คีย์อยู่ใน `SIMIANX_API_KEY` เท่านั้น สกิลไม่มีวันเขียนคีย์ลงในรีโพซิทอรี ล็อก หรือพรอมต์
- เอเจนต์ไม่มีวันได้เซสชันของเว็บไซต์ การลงชื่อเข้าใช้จากเอเจนต์จะสร้างแค่คีย์ API ของเอเจนต์ตัวนั้น และเราจะส่งอีเมลแจ้งคุณทุกครั้งที่เกิดขึ้น
- แต่ละคีย์ตั้งขอบเขตสิทธิ์ งบรายวันและรายเดือน และรายการ IP ที่อนุญาตได้ (ไม่บังคับ) ให้เอเจนต์แต่ละตัวใช้คีย์ที่มีสิทธิ์น้อยที่สุดเท่าที่พอทำงาน
- เพิกถอนคีย์ได้ที่ **บัญชีของฉัน → คีย์ API** แล้วคีย์จะใช้ไม่ได้ภายในหนึ่งวินาที

## เวอร์ชัน

สกิลส่งเวอร์ชันของตัวเองไปในเฮดเดอร์ `X-SimianX-Skill` เมื่อเวอร์ชันไหนเลิกใช้แล้ว API จะตอบ `426` พร้อม URL ที่ต้องอ่านใหม่ และ `GET /v1/skill` จะบอกเวอร์ชันปัจจุบันกับเวอร์ชันขั้นต่ำ อัปเดตได้ด้วยคำสั่งของเอเจนต์เอง หรือวางประโยคด้านบนให้เอเจนต์อีกครั้ง ดูสิ่งที่เปลี่ยนได้ใน[บันทึกการเปลี่ยนแปลง](CHANGELOG.md)

## โครงสร้างรีโพซิทอรี

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

## ฟีดแบ็ก

- จากเอเจนต์: `POST /v1/feedback`
- จากคน: เรื่องสกิลแจ้งที่ [GitHub issues](https://github.com/SimianX-AI/simianx-skills/issues) เรื่องผลิตภัณฑ์แจ้งที่ [simianx.ai/agents](https://www.simianx.ai/agents)

อ่าน [CONTRIBUTING.md](CONTRIBUTING.md) ก่อนเปิด pull request และดู [SECURITY.md](SECURITY.md) ถ้าจะรายงานช่องโหว่

## สัญญาอนุญาต

ทุกอย่างในรีโพซิทอรีนี้ใช้สัญญาอนุญาต MIT การใช้ SimianX API อยู่ภายใต้[ข้อกำหนดการให้บริการ](https://www.simianx.ai/legal/terms) การวิเคราะห์ของ SimianX เป็นข้อมูล ไม่ใช่คำแนะนำการลงทุน
