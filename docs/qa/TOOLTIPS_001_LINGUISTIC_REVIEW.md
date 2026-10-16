# Independent Linguistic & Technical QA Review — TOOLTIPS-001

> **Document:** `docs/qa/TOOLTIPS_001_LINGUISTIC_REVIEW.md`  
> **Reviewer:** Antigravity (QA Agent)  
> **Target Translation File:** `local/translations/TOOLTIPS-001.th.json` (20 records)  
> **Baseline Source File:** `local/source/TOOLTIPS-001.json` (20 records)  
> **Reference Directives:** `docs/TOOLTIPS_001_CONTROLLER_REVIEW.md`, `docs/TRANSLATION_STYLE_APPROVAL_v0.2.md`  
> **Date:** 2026-10-16  
> **QA Review Scope:** Linguistic, technical terminology, semantic accuracy, quality/performance tradeoffs, markup & whitespace integrity.  
> **Runtime / Rendering Status:** `NOT_RUN` — No in-game PASS granted; no translation or game files modified; no git commits.

---

## 1. Executive Summary

An independent linguistic, technical, and structural QA audit of all 20 graphics/video settings tooltip records in `local/translations/TOOLTIPS-001.th.json` was conducted against `local/source/TOOLTIPS-001.json`.

### Key Highlights:
1. **Structural & Formatting Integrity (100% Pass):**
   - Zero structural errors confirmed by `tools/validate_tooltips.py`.
   - All 4 dynamic tokens (`{STAFF_COUNT_LIMIT}`, `{STUDENT_COUNT_LIMIT}`, `{STAFF_COUNT_UNLIMITED}`, `{STUDENT_COUNT_UNLIMITED}`) and formatting markup (`<color=red>...</color>`) in `CharacterLimits` are perfectly preserved in exact count, case, and sequence.
   - All newline characters (`\n`), tab indentations (`\t\t`), and deliberate trailing spaces (e.g., `AntialiasingQuality` trailing space, `CharacterDrawDistance` line-end spaces) match source bytes verbatim.
   - Zero unapproved invisible control characters, zero Zero-Width Spaces (`\u200b`), and zero Non-Breaking Spaces (`\u00a0`) detected.
2. **Adherence to Controller Directives:**
   - **`CharacterLimits`:** Strictly refrained from translating `{...UNLIMITED}` as "ไม่จำกัด" in visible UI text, maintaining faithful parallel structure without unverified runtime assumptions.
   - **`MaxFPS`:** Neutral translation (`ไม่ทำงานร่วมกับ VSync`) correctly preserved the source's ambiguity without extrapolating unverified behavioral claims like "ไม่มีผลเมื่อเปิดใช้ VSync".
   - **Source Typo Handling:** Faithfully conveyed the intended comparative semantics of `AntialiasingMode` ("higher quality that FXAA") and `RenderScale` ("resoluton setting") without mechanically replicating English grammatical defects in Thai.
3. **Primary Linguistic Findings & Recommendations:**
   - **Moderate Finding 1 — `FullScreenMode`:** Translating literally as `"เลือกระหว่างโหมดเต็มหน้าจอ"` is grammatically awkward in Thai (requires pair/plural complement) and factually misleading because the dropdown includes `Windowed` mode. Recommended: **`เลือกโหมดการแสดงผล`** (Display Mode).
   - **Moderate Finding 2 — `Resolution`:** Literal translation `"กำหนดความละเอียดของหน้าต่างเกม"` creates false impressions that the setting applies only to windowed mode. In PC gaming, it sets the overall display resolution. Recommended: **`กำหนดความละเอียดหน้าจอของเกม`** (or `กำหนดความละเอียดการแสดงผลของเกม`).
   - **Moderate Finding 3 — `WorldDetail`:** `"โลกในเกม"` and `"รายละเอียดโลก"` sound overly literal for a campus simulator. Translating as **`รายละเอียดสภาพแวดล้อม`** (Environment Detail) or **`รายละเอียดฉาก`** (Scene Detail) is more natural and aligns with sim game conventions.
   - **Minor Phrasing / Dangling Comparatives:** In `AmbientOcclusionModeQuality`, `AnimationSkinningQuality`, and `ShadowQuality`, phrases like `"ภาพดูดีกว่า"` or `"ทำให้ดูคมชัดกว่า"` end on dangling comparatives. Refining to `"ดูสวยงามขึ้น"` / `"ดูคมชัดขึ้น"` improves flow and tone.

---

## 2. Detailed Findings by String ID & Key

| # | Key & Segment ID | Source English | Current Thai Translation | Category | Severity | Detailed Analysis & Context | Suggested Revision / Recommendation |
| :-: | :--- | :--- | :--- | :--- | :-: | :--- | :--- |
| **01** | `UI/Settings/Tooltips/AmbientOcclusionMode`<br>`segment-107` | Enables ambient occlusion, which increases lighting quality in dark corners.<br>HBAO is higher quality than SSAO.<br>HBAO is also more expensive to run than SSAO.<br>Disable to increase graphics performance. | เปิด Ambient Occlusion เพื่อเพิ่มคุณภาพของแสงในมุมมืด<br>HBAO คุณภาพสูงกว่า SSAO<br>HBAO ใช้ทรัพยากรในการทำงานมากกว่า SSAO ด้วย<br>ปิดเพื่อเพิ่มประสิทธิภาพกราฟิก | Naturalness / Style | **Minor** | แปลถูกต้องและสื่อความหมายเทคนิคได้ดีมาก การคงชื่อเฉพาะ Ambient Occlusion, HBAO, SSAO ตรงกับตัวเลือกในเมนู<br>จุดปรับปรุงเล็กน้อย: คำว่า "ด้วย" ท้ายบรรทัดที่ 3 ("...มากกว่า SSAO ด้วย") ฟังดูเป็นภาษาพูดเล็กน้อย | เสนอปรับบรรทัดที่ 3:<br>**`นอกจากนี้ HBAO ยังใช้ทรัพยากรในการทำงานมากกว่า SSAO`**<br>(หรือคงตามเดิมได้ ไม่กระทบความหมาย) |
| **02** | `UI/Settings/Tooltips/AmbientOcclusionModeQuality`<br>`segment-108` | Controls the quality of ambient occlusion.<br>High and Very High quality settings look nicer.<br>Low quality does not look as nice but will increase performance. | ควบคุมคุณภาพของ Ambient Occlusion<br>คุณภาพระดับสูงและสูงมากทำให้ภาพดูดีกว่า<br>คุณภาพต่ำทำให้ภาพดูดีไม่เท่า แต่จะช่วยเพิ่มประสิทธิภาพ | Naturalness / Parallelism | **Minor** | 1. บรรทัดที่ 2 "ทำให้ภาพดูดีกว่า" เป็นการเปรียบเทียบแบบลอย (look nicer = ดูสวยงามขึ้น/ดูดีขึ้น)<br>2. บรรทัดที่ 3 ใช้ "คุณภาพต่ำ" ขาดคำว่า "ระดับ" ไม่ขนานกับ "คุณภาพระดับสูง" ในบรรทัดที่ 2 | เสนอปรับเป็น:<br>`ควบคุมคุณภาพของ Ambient Occlusion`<br>**`การตั้งค่าคุณภาพระดับสูงและสูงมากทำให้ภาพดูสวยงามขึ้น`**<br>**`คุณภาพระดับต่ำอาจดูไม่สวยงามเท่า แต่จะช่วยเพิ่มประสิทธิภาพ`** |
| **03** | `UI/Settings/Tooltips/AnimationSkinningQuality`<br>`segment-109` | Controls how many animation bones influence each vertex on a mesh.<br>High quality setting uses more bones and looks nicer.<br>Low quality setting uses fewer bones and may increase performance. | ควบคุมจำนวนกระดูกแอนิเมชันที่มีผลต่อจุดยอด (vertex) แต่ละจุดของเมช<br>การตั้งค่าคุณภาพสูงใช้กระดูกมากขึ้นและภาพดูดีกว่า<br>การตั้งค่าคุณภาพต่ำใช้กระดูกน้อยลงและอาจช่วยเพิ่มประสิทธิภาพ | Terminology / Naturalness | **Minor** | ผู้แปลเลือกใช้วงเล็บ `จุดยอด (vertex)` ได้ดี ช่วยให้ผู้เล่นเข้าใจศัพท์ skeletal mesh<br>จุดปรับปรุง: "และภาพดูดีกว่า" ควรปรับเป็น "และทำให้ภาพดูสวยงามขึ้น" เพื่อความสละสลวย การแปล "may increase" เป็น "อาจช่วยเพิ่ม" ถูกต้องแม่นยำมาก | เสนอปรับบรรทัดที่ 2:<br>**`การตั้งค่าคุณภาพสูงใช้กระดูกมากขึ้นและทำให้ภาพดูสวยงามขึ้น`** |
| **04** | `UI/Settings/Tooltips/AnisoTextures`<br>`segment-110` | Enables anisotropic filtering for all textures, or can be enabled for some textures only.<br>This improves quality of textures viewed at glancing angles.<br>Disable to increase graphics performance. | เปิด Anisotropic Filtering กับเท็กซ์เจอร์ทั้งหมด หรือเลือกเปิดกับบางเท็กซ์เจอร์เท่านั้นก็ได้<br>ช่วยเพิ่มคุณภาพของเท็กซ์เจอร์ที่มองจากมุมเฉียง<br>ปิดเพื่อเพิ่มประสิทธิภาพกราฟิก | Terminology / Accuracy | **Informational** (Accepted) | การแปล "glancing angles" ว่า "มุมเฉียง" สื่อความหมายได้อย่างยอดเยี่ยม หลีกเลี่ยงศัพท์เทคนิคที่ซับซ้อนแต่ตรงการใช้งานจริง คำว่า "เท็กซ์เจอร์" สอดคล้องกับรายการอื่น | **คงตามร่างปัจจุบัน** |
| **05** | `UI/Settings/Tooltips/AntialiasingMode`<br>`segment-111` | Enables anti-aliasing, which reduces jagged edges.<br>SMAA is higher quality that FXAA.<br>SMAA is also slower to run than FXAA.<br>Disable to increase graphics performance. | เปิด Anti-Aliasing เพื่อลดรอยหยักตามขอบภาพ<br>SMAA คุณภาพสูงกว่า FXAA<br>SMAA ทำงานช้ากว่า FXAA ด้วย<br>ปิดเพื่อเพิ่มประสิทธิภาพกราฟิก | Source Typo Handling / Style | **Minor** | ผู้แปลจับ typo ต้นฉบับ ("higher quality that FXAA") และแปลเป็นเปรียบเทียบ "คุณภาพสูงกว่า FXAA" ได้ถูกต้อง<br>จุดปรับปรุง: บรรทัดที่ 3 มี "ด้วย" ท้ายประโยคเช่นเดียวกับ #01 | เสนอพิจารณาปรับบรรทัดที่ 3:<br>**`นอกจากนี้ SMAA ยังทำงานช้ากว่า FXAA`**<br>(หรือคงตามเดิมได้) |
| **06** | `UI/Settings/Tooltips/AntialiasingQuality`<br>`segment-112` | Higher quality improves reducing jagged edges.<br>Reduce quality to increase graphics performance. *(trailing space)* | คุณภาพที่สูงขึ้นช่วยลดรอยหยักได้ดีขึ้น<br>ลดคุณภาพเพื่อเพิ่มประสิทธิภาพกราฟิก *(trailing space)* | Source Syntax Handling | **Informational** (Accepted) | ต้นฉบับภาษาอังกฤษไวยากรณ์ผิดปกติ ("improves reducing jagged edges") ผู้แปลเกลาเป็น "คุณภาพที่สูงขึ้นช่วยลดรอยหยักได้ดีขึ้น" ได้สละสลวยและเป็นธรรมชาติมาก ช่องว่างท้ายสตริงคงไว้ตรงเป๊ะ | **คงตามร่างปัจจุบัน** |
| **07** | `UI/Settings/Tooltips/Bloom`<br>`segment-113` | Enables bloom, which makes bright parts of the scene look nicer.<br>Disable to increase graphics performance. | เปิด Bloom เพื่อให้ส่วนที่สว่างของฉากดูดีขึ้น<br>ปิดเพื่อเพิ่มประสิทธิภาพกราฟิก | Clarity & Tone | **Informational** (Accepted) | กระชับ ชัดเจน ถูกต้องตามความหมายของเอฟเฟกต์ Bloom | **คงตามร่างปัจจุบัน** |
| **08** | `UI/Settings/Tooltips/CharacterDrawDistance`<br>`segment-114` | Chooses distance that characters start fading out. *(space)*<br>Higher draw distance keeps characters in view at longer distances. *(space)*<br>Choose a lower setting to improve CPU and graphics performance. | เลือกระยะที่ตัวละครเริ่มจางหายไป *(space)*<br>ระยะแสดงผลที่สูงขึ้นทำให้ตัวละครยังอยู่ในมุมมองได้ในระยะไกลขึ้น *(space)*<br>เลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก | Contextual Terminology | **Informational** (Accepted) | ผู้แปลแปล "characters" เป็น "ตัวละคร" (บุคคลในเกม ไม่ใช่ตัวอักษร) ถูกต้อง 100% ช่องว่างท้ายบรรทัดก่อน `\n` สองตำแหน่งถูกรักษาไว้ครบถ้วน | **คงตามร่างปัจจุบัน** (ปลดธง `AMBIGUOUS` ได้) |
| **09** | `UI/Settings/Tooltips/CharacterLimits`<br>`segment-115` | With this option off, the number of characters in the game is limited as follows:\n\nMaximum number of staff: {STAFF_COUNT_LIMIT}\nMaximum number of students: {STUDENT_COUNT_LIMIT}\n\t\t\nWith this option on, the character limits in the game will be:\n\t\t\nMaximum number of staff: {STAFF_COUNT_UNLIMITED}\nMaximum number of students: {STUDENT_COUNT_UNLIMITED}\n\t\t\n<color=red>WARNING: Exceeding the normal limits will have an adverse effect on the game's performance.</color>\n | เมื่อปิดตัวเลือกนี้ จำนวนตัวละครในเกมจะถูกจำกัดดังนี้:\n\nจำนวนบุคลากรสูงสุด: {STAFF_COUNT_LIMIT}\nจำนวนนักศึกษาสูงสุด: {STUDENT_COUNT_LIMIT}\n\t\t\nเมื่อเปิดตัวเลือกนี้ ขีดจำกัดตัวละครในเกมจะเป็นดังนี้:\n\t\t\nจำนวนบุคลากรสูงสุด: {STAFF_COUNT_UNLIMITED}\nจำนวนนักศึกษาสูงสุด: {STUDENT_COUNT_UNLIMITED}\n\t\t\n<color=red>คำเตือน: การเกินขีดจำกัดปกติจะส่งผลเสียต่อประสิทธิภาพของเกม</color>\n | Token Integrity / Strict Adherence | **Informational** (Verified Pass) | ปฏิบัติตามคำสั่ง Controller เคร่งครัด: ไม่แต่งเติม "ไม่จำกัด" จากชื่อ token `UNLIMITED` โดยคงข้อความ "จำนวน...สูงสุด" ขนานกันทั้งสองส่วน Token ทั้ง 4 ตัว, แท็กสี, การเว้นวรรค `\t\t`, และ LF ครบถ้วน ศัพท์ Staff/Student ตรงตาม Glossary G003/G002 | **คงตามร่างปัจจุบัน** |
| **10** | `UI/Settings/Tooltips/DepthOfField`<br>`segment-116` | Enables depth of field, which subtly blurs near and far parts of the scene.<br>Disable to increase graphics performance. | เปิด Depth of Field ซึ่งจะทำให้ส่วนใกล้และส่วนไกลของฉากเบลอเล็กน้อย<br>ปิดเพื่อเพิ่มประสิทธิภาพกราฟิก | Terminology / Clarity | **Informational** (Accepted) | การคง Depth of Field เป็นภาษาอังกฤษเหมาะสมกว่า "ระยะชัดลึก" ที่อาจทำให้ผู้เล่นทั่วไปสับสนกับระยะโฟกัส คำอธิบายภาพเบลอชัดเจน | **คงตามร่างปัจจุบัน** |
| **11** | `UI/Settings/Tooltips/FullScreenMode`<br>`segment-117` | Chooses between fullscreen modes. | เลือกระหว่างโหมดเต็มหน้าจอ | Semantic Inaccuracy / Thai Grammar | **Moderate** | 1. ไวยากรณ์ไทย "เลือกระหว่างโหมดเต็มหน้าจอ" ขาดคำขยายหรือคู่เปรียบเทียบ ทำให้ฟังดูค้างและห้วน<br>2. ความหมายจริงในเกม: เมนูนี้มีตัวเลือกทั้ง `Full Screen Window`, `Exclusive Full Screen` และ `Windowed` (โหมดหน้าต่าง) การใช้คำว่า "เต็มหน้าจอ" อย่างเดียวจึงขัดแย้งกับตัวเลือกจริงในเกม | **เสนอเปลี่ยนเป็น:**<br>**`เลือกโหมดการแสดงผล`**<br>*(ตรงตามคำแนะนำของ Controller ครอบคลุมทั้งโหมดเต็มหน้าจอและโหมดหน้าต่าง)* |
| **12** | `UI/Settings/Tooltips/MSAASamples`<br>`segment-118` | Increase the number of MSAA samples to reduce jagged edges or reduce it to increase graphics performance. | เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก หรือลดลงเพื่อเพิ่มประสิทธิภาพกราฟิก | Flow / Naturalness | **Minor** | แปลได้ครบถ้วน แต่คำว่า "หรือลดลงเพื่อ..." สามารถเติมกรรมให้ชัดเจนขึ้นเป็น "หรือลดจำนวนลง" เพื่อให้ประโยคสมบูรณ์และอ่านลื่นไหลขึ้น | เสนอปรับเป็น:<br>**`เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก`** |
| **13** | `UI/Settings/Tooltips/MaxFPS`<br>`segment-119` | Limits the maximum framerate the game can run at.<br>Lower this if you find your machine is running too hot or loud.<br>Does not work in conjuction with VSync. *(source typo)* | จำกัดเฟรมเรตสูงสุดที่เกมจะทำงานได้<br>ลดค่านี้หากเครื่องร้อนหรือเสียงดังเกินไป<br>ไม่ทำงานร่วมกับ VSync | Strict Adherence to Ambiguity | **Informational** (Verified Pass) | ปฏิบัติตามคำสั่ง Controller ถูกต้อง โดยคงความหมายกลาง "ไม่ทำงานร่วมกับ VSync" ไม่ด่วนสรุปว่า "ไม่มีผลเมื่อเปิด VSync" การแปล "เครื่องร้อนหรือเสียงดังเกินไป" เป็นธรรมชาติมาก | **คงตามร่างปัจจุบัน** |
| **14** | `UI/Settings/Tooltips/QualityPresets`<br>`segment-120` | Chooses between several graphics quality presets.<br>Higher presets offer better graphics quality, but lower performance.<br>Lower presets reduce graphics quality for better performance. | เลือกจากพรีเซ็ตคุณภาพกราฟิกหลายระดับ<br>พรีเซ็ตที่สูงขึ้นให้คุณภาพกราฟิกดีกว่า แต่ประสิทธิภาพต่ำลง<br>พรีเซ็ตที่ต่ำลงลดคุณภาพกราฟิกเพื่อให้ประสิทธิภาพดีขึ้น | Naturalness / Phrasing | **Minor** | 1. "พรีเซ็ตที่สูงขึ้น/ที่ต่ำลง" สื่อถึงความเปลี่ยนแปลงต่อเนื่อง ในขณะที่บริบทคือระดับตัวเลือก ควรใช้ "พรีเซ็ตระดับที่สูงกว่า / ระดับที่ต่ำกว่า"<br>2. บรรทัดที่ 3 มีคำซ้ำเสียง "ต่ำ**ลงลด**คุณภาพ" ทำให้อ่านสะดุด | เสนอปรับบรรทัด 2–3 เป็น:<br>**`พรีเซ็ตระดับที่สูงกว่าให้คุณภาพกราฟิกดีกว่า แต่ประสิทธิภาพต่ำลง`**<br>**`พรีเซ็ตระดับที่ต่ำกว่าจะลดคุณภาพกราฟิก เพื่อให้ประสิทธิภาพดีขึ้น`** |
| **15** | `UI/Settings/Tooltips/RenderScale`<br>`segment-121` | Change the resolution the 3D graphics are rendered at.<br>GUI is still rendered at the resolution defined in the resoluton setting. *(source typo)*<br>Reduce to increase graphics performance. | เปลี่ยนความละเอียดที่ใช้เรนเดอร์กราฟิก 3D<br>GUI ยังคงเรนเดอร์ที่ความละเอียดตามที่กำหนดในการตั้งค่าความละเอียด<br>ลดค่านี้เพื่อเพิ่มประสิทธิภาพกราฟิก | Repetition / Flow | **Minor** | แปลถูกต้องตามหลักการทำงานของการสเกลภาพ 3D แยกจาก UI<br>จุดสังเกต: วลี "ที่ความละเอียดตามที่กำหนดในการตั้งค่าความละเอียด" มีคำว่า "ความละเอียด" ซ้ำสองครั้ง สามารถเกลาให้กระชับขึ้นได้ | เสนอปรับบรรทัดที่ 2:<br>**`GUI จะยังคงเรนเดอร์ตามความละเอียดที่กำหนดไว้ในการตั้งค่า Resolution`**<br>*(หรือ "...ในการตั้งค่าความละเอียดหน้าจอ")* |
| **16** | `UI/Settings/Tooltips/Resolution`<br>`segment-122` | Sets window resolution.<br>Higher resolution makes the whole game appear sharper.<br>Reduce resolution to increase CPU and graphics performance. | กำหนดความละเอียดของหน้าต่างเกม<br>ความละเอียดที่สูงขึ้นทำให้ทั้งเกมดูคมชัดขึ้น<br>ลดความละเอียดเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก | Source Ambiguity / Player Understanding | **Moderate** | ต้นฉบับใช้คำว่า "window resolution" ซึ่งเป็นศัพท์ทางเทคนิคของการสร้างหน้าต่างโปรแกรม แต่ในความเป็นจริง ตัวเลือกนี้ควบคุมความละเอียดทั้งโหมดหน้าต่างและโหมดเต็มหน้าจอ การแปลตรงตัวว่า "หน้าต่างเกม" อาจทำให้ผู้เล่นเข้าใจผิดว่ามีผลเฉพาะเวลาเล่นแบบ Windowed mode เท่านั้น | **เสนอปรับเป็น:**<br>**`กำหนดความละเอียดหน้าจอของเกม`**<br>*(ตรงตาม alt ของ Claude และข้อสังเกตของ Controller)* |
| **17** | `UI/Settings/Tooltips/ShadowQuality`<br>`segment-123` | Chooses shadow resolution level.<br>Higher shadow resolution looks sharper.<br>Choose a lower setting to increase graphics performance. | เลือกระดับความละเอียดของเงา<br>ความละเอียดของเงาที่สูงขึ้นทำให้ดูคมชัดกว่า<br>เลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพกราฟิก | Dangling Comparative | **Minor** | บรรทัดที่ 2 "ทำให้ดูคมชัดกว่า" ละประธานและไม่มีตัวเปรียบเทียบ ควรระบุให้ชัดว่าอะไรคมชัดขึ้น | เสนอปรับบรรทัดที่ 2 เป็น:<br>**`ความละเอียดของเงาที่สูงขึ้นจะช่วยให้เงาดูคมชัดขึ้น`** |
| **18** | `UI/Settings/Tooltips/TextureQuality`<br>`segment-124` | Chooses different sizes of texture to use.<br>Reduce texture detail to improve graphics performance, particularly if you have low video memory. | เลือกขนาดของเท็กซ์เจอร์ที่จะใช้<br>ลดรายละเอียดเท็กซ์เจอร์เพื่อเพิ่มประสิทธิภาพกราฟิก โดยเฉพาะหากหน่วยความจำวิดีโอมีน้อย | Clarity / Terminology | **Informational** (Accepted) | แปลได้แม่นยำ คำว่า "หน่วยความจำวิดีโอ" สื่อถึง video memory ได้ถูกต้องโดยไม่ต้องใช้คำย่อ VRAM ที่อาจไม่คุ้นหูผู้เล่นทั่วไป | **คงตามร่างปัจจุบัน** |
| **19** | `UI/Settings/Tooltips/Vsync`<br>`segment-125` | Synchronises the game framerate with your display's refresh rate.<br>Reduces screen tearing, but may increase input delay. | ซิงก์เฟรมเรตของเกมให้ตรงกับรีเฟรชเรตของจอภาพ<br>ลดภาพฉีก แต่อาจเพิ่มความหน่วงของอินพุต | Terminology Precision | **Informational** (Accepted) | แปลศัพท์เทคนิคด้านการแสดงผลได้กระชับ ชัดเจน และตรงมาตรฐานเกมเมอร์ไทย ("ภาพฉีก" = screen tearing, "ความหน่วงของอินพุต" = input delay) | **คงตามร่างปัจจุบัน** |
| **20** | `UI/Settings/Tooltips/WorldDetail`<br>`segment-126` | Chooses overall detail level of the world.<br>Higher world detail keeps more detail in view at longer view distances.<br>Choose a lower setting to improve CPU and graphics performance. | เลือกระดับรายละเอียดโดยรวมของโลกในเกม<br>รายละเอียดโลกที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น<br>เลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก | Contextual Naturalness / Repetition | **Moderate** | 1. ในบริบทเกมจำลองการบริหารมหาวิทยาลัย คำว่า "โลกในเกม" (world) ฟังดูแปลกและให้ความรู้สึกเหมือนเกมแนว Open-world RPG บริบทจริงคือสิ่งแวดล้อมรอบมหาวิทยาลัย อาคาร ต้นไม้ และฉากนอกตัวอาคาร<br>2. บรรทัดที่ 2 มีคำซ้ำ "รายละเอียดโลก... จะคงรายละเอียดไว้..." | **เสนอปรับเป็น:**<br>**`เลือกระดับรายละเอียดโดยรวมของฉาก`**<br>**`การตั้งค่ารายละเอียดฉากที่สูงขึ้นจะช่วยคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น`**<br>`เลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก`<br>*(หรือใช้ "รายละเอียดสภาพแวดล้อม" หากตรงกับป้ายเมนู)* |

---

## 3. Systematic Verification Matrix

### 3.1 Token, Marker & Special Character Integrity
- **Total Records:** 20
- **Total Placeholders / Tags:** 6 (4 tokens + 2 HTML color tags in `CharacterLimits`)
- **Token Check:** 100% Match (0 dropped, 0 altered, 0 case mismatches).
- **Whitespace / LF Checks:**
  - Standard LFs (`\n`): 100% matched in line count and placement.
  - Multi-line block formatting in `CharacterLimits` (`\n\n`, `\n\t\t\n`, and terminal `\n`): Verified 100% intact.
  - Preserved Trailing Spaces:
    - `UI/Settings/Tooltips/AntialiasingQuality`: Line 2 ending space (`...กราฟิก `) matches source (`...performance. `).
    - `UI/Settings/Tooltips/CharacterDrawDistance`: Line 1 (`...หายไป `) and Line 2 (`...ไกลขึ้น `) ending spaces before LF match source.
- **Glyph / Code Point Verification:** Zero unapproved control characters or hidden split markers (ZWSP `\u200b`, NBSP `\u00a0`).

### 3.2 Performance & Quality Trade-off Consistency Check
The 20 tooltips frequently describe inverse tradeoffs between visual quality and system performance. The consistency across these records was verified:
- **Disabling Features for Graphics Performance:**
  - 5 records (`AmbientOcclusionMode`, `AnisoTextures`, `AntialiasingMode`, `Bloom`, `DepthOfField`) use identical wording:
    > `ปิดเพื่อเพิ่มประสิทธิภาพกราฟิก`
- **Lowering Settings for CPU & Graphics Performance:**
  - 3 records (`CharacterDrawDistance`, `Resolution`, `WorldDetail`) correctly maintain the explicit source distinction between CPU and GPU impact:
    > `...เพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก`
- **Modality Preservation:**
  - `AnimationSkinningQuality` ("may increase performance") -> `อาจช่วยเพิ่มประสิทธิภาพ` (Preserves uncertainty).
  - `Vsync` ("may increase input delay") -> `แต่อาจเพิ่มความหน่วงของอินพุต` (Preserves uncertainty).

---

## 4. Source Ambiguity vs Translation Defect Analysis

| Item & Key | Source Phenomenon | Source Ambiguity vs Translation Defect | Assessment & QA Conclusion |
| :--- | :--- | :--- | :--- |
| `UI/Settings/Tooltips/Resolution` | "Sets window resolution." | **Source Ambiguity** | ต้นฉบับอังกฤษใช้คำว่า "window resolution" (ความละเอียดของหน้าต่าง) ซึ่งเป็นศัพท์เชิงเทคนิคของเอนจินเกม แต่ทำให้ผู้เล่นเข้าใจผิดว่ามีผลเฉพาะโหมดหน้าต่าง Translation ถอดตรงตัวตามต้นฉบับ จึงไม่ใช่ข้อผิดพลาดทางภาษา แต่สมควรปรับเป็น "ความละเอียดหน้าจอของเกม" เพื่อความชัดเจนในการใช้งานจริง |
| `UI/Settings/Tooltips/FullScreenMode` | "Chooses between fullscreen modes." | **Both (Ambiguous Source + Translation Defect)** | 1. **ต้นฉบับกำกวม:** ระบุเฉพาะ "fullscreen modes" ทั้งที่เมนูมีตัวเลือก Windowed ด้วย<br>2. **คำแปลมีจุดบกพร่อง:** ไวยากรณ์ "เลือกระหว่างโหมดเต็มหน้าจอ" ขาดคู่เปรียบเทียบ การปรับเป็น "เลือกโหมดการแสดงผล" แก้ไขได้ทั้งสองปัญหา |
| `UI/Settings/Tooltips/MaxFPS` | "Does not work in conjuction with VSync." *(typo)* | **Source Ambiguity & Typo** | ต้นฉบับสะกด "conjuction" ตกตัว g และไม่ได้ระบุชัดเจนว่าพฤติกรรมคืออะไร คำแปลเลือกแปลตรงตัว "ไม่ทำงานร่วมกับ VSync" เป็นการตัดสินใจที่ถูกต้องตามหลัก QA โดยไม่คาดเดาพฤติกรรมเอง |
| `UI/Settings/Tooltips/CharacterLimits` | `{STAFF_COUNT_UNLIMITED}`, `{STUDENT_COUNT_UNLIMITED}` | **Source Variable Naming Ambiguity** | แม้ชื่อตัวแปรภายในจะมีคำว่า UNLIMITED แต่ข้อความต้นฉบับแสดงผลว่า "Maximum number of staff:" คำแปลคงโครงสร้าง "จำนวน...สูงสุด" ไว้ ถือเป็นความรอบคอบและถูกต้องตามคำสั่ง Controller |
| `UI/Settings/Tooltips/WorldDetail` | "Chooses overall detail level of the world." | **Source Ambiguity** | คำว่า "world" ในเกมบริหารวิทยาเขตกำกวม ผู้แปลแปลตรงตัวว่า "โลกในเกม" ซึ่งไม่เข้ากับบรรยากาศของเกม การปรับเป็น "ฉาก" หรือ "สภาพแวดล้อม" เป็นการปรับตามบริบท (Contextual adaptation) |
| `UI/Settings/Tooltips/AntialiasingMode` | "higher quality that FXAA" | **Source Typo** | ต้นฉบับพิมพ์ผิดจาก than เป็น that ผู้แปลเข้าใจความหมายและแปลเปรียบเทียบได้ถูกต้อง ไม่ถือเป็นข้อผิดพลาดของคำแปล |
| `UI/Settings/Tooltips/AntialiasingQuality` | "improves reducing jagged edges" | **Source Grammar Defect** | ต้นฉบับใช้ไวยากรณ์แปลก คำแปลเกลาเป็น "ช่วยลดรอยหยักได้ดีขึ้น" เป็นการแก้ปัญหาที่ยอดเยี่ยม |

---

## 5. Unresolved Runtime & Contextual Questions

The following questions cannot be resolved through linguistic review alone and must be tracked for runtime verification:

1. **Menu Label Synchronization:**
   - คำแปลของ Tooltip ในชุดนี้มีการอ้างอิงถึงชื่อการตั้งค่าอื่น เช่น `Resolution`, `GUI`, `VSync`, `พรีเซ็ต` และตัวเลือกระดับคุณภาพ (`สูง`, `สูงมาก`, `ต่ำ`)
   - **คำถามค้างตรวจ:** เมื่อป้ายกำกับของตัวเลือกเหล่านั้นในไฟล์แปลหลัก (`Settings`) ได้รับการแปล คำแปลใน Tooltip จะต้องสอดคล้องกับป้ายกำกับที่ผู้เล่นเห็นบนหน้าจอ 100%
2. **FullScreenMode Dropdown Values:**
   - **คำถามค้างตรวจ:** ในเกม Two Point Campus ตัวเลือกของ FullScreenMode มีอะไรบ้างอย่างเป็นทางการ? (หลักฐานปัจจุบันพบ: Full Screen Window, Exclusive Full Screen, Windowed) ซึ่งยืนยันว่าการใช้ "เลือกโหมดการแสดงผล" เหมาะสมกว่า "เลือกระหว่างโหมดเต็มหน้าจอ"
3. **MaxFPS & VSync Runtime Interaction:**
   - **คำถามค้างตรวจ:** เมื่อเปิด VSync ในเกม ตัวเลื่อน MaxFPS จะถูกล็อคเป็นสีเทา (disabled) หรือไม่? หรือตัวเลื่อนยังทำงานได้แต่ไม่มีผลจริง?
4. **Visual Layout & Multi-line Tooltip Boundaries:**
   - **คำถามค้างตรวจ:** จากผลการทดสอบ `WO-VISUAL-008` พบว่า Tooltip ยังไม่จำกัดความกว้างที่ 800 units โดยแท้จริงใน C# Runtime ดังนั้น ข้อความขนาดยาว เช่น `CharacterLimits` (มีหลายบรรทัดและการจัดวางแท็บ) จะแสดงผลล้นขอบจอหรือไม่อยู่ในภารกิจทดสอบด้าน Visual ของ Controller ในลำดับถัดไป

---

## 6. Recommended Action Items for Controller

สำหรับชุดแก้ถัดไป (Next Translation Revision) ขอเสนอให้ Controller นำข้อเสนอแนะ 3 รายการระดับ **Moderate** และ 4 รายการระดับ **Minor** ไปพิจารณาปรับปรุงในไฟล์คำแปล:

```json
[
  {
    "key": "UI/Settings/Tooltips/FullScreenMode",
    "current_thai": "เลือกระหว่างโหมดเต็มหน้าจอ",
    "proposed_thai": "เลือกโหมดการแสดงผล",
    "rationale": "Grammatically complete in Thai and covers Windowed mode present in dropdown."
  },
  {
    "key": "UI/Settings/Tooltips/Resolution",
    "current_thai": "กำหนดความละเอียดของหน้าต่างเกม",
    "proposed_thai": "กำหนดความละเอียดหน้าจอของเกม",
    "rationale": "Prevents player confusion that setting only applies to Windowed mode."
  },
  {
    "key": "UI/Settings/Tooltips/WorldDetail",
    "current_thai": "เลือกระดับรายละเอียดโดยรวมของโลกในเกม\nรายละเอียดโลกที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น\nเลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก",
    "proposed_thai": "เลือกระดับรายละเอียดโดยรวมของฉาก\nการตั้งค่ารายละเอียดฉากที่สูงขึ้นจะช่วยคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น\nเลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก",
    "rationale": "More natural context for a campus management sim and eliminates awkward repetition of รายละเอียด."
  },
  {
    "key": "UI/Settings/Tooltips/AmbientOcclusionModeQuality",
    "current_thai": "ควบคุมคุณภาพของ Ambient Occlusion\nคุณภาพระดับสูงและสูงมากทำให้ภาพดูดีกว่า\nคุณภาพต่ำทำให้ภาพดูดีไม่เท่า แต่จะช่วยเพิ่มประสิทธิภาพ",
    "proposed_thai": "ควบคุมคุณภาพของ Ambient Occlusion\nการตั้งค่าคุณภาพระดับสูงและสูงมากทำให้ภาพดูสวยงามขึ้น\nคุณภาพระดับต่ำอาจดูไม่สวยงามเท่า แต่จะช่วยเพิ่มประสิทธิภาพ",
    "rationale": "Resolves dangling comparative (ดูดีกว่า) and maintains parallel ระดับ phrasing."
  },
  {
    "key": "UI/Settings/Tooltips/QualityPresets",
    "current_thai": "เลือกจากพรีเซ็ตคุณภาพกราฟิกหลายระดับ\nพรีเซ็ตที่สูงขึ้นให้คุณภาพกราฟิกดีกว่า แต่ประสิทธิภาพต่ำลง\nพรีเซ็ตที่ต่ำลงลดคุณภาพกราฟิกเพื่อให้ประสิทธิภาพดีขึ้น",
    "proposed_thai": "เลือกจากพรีเซ็ตคุณภาพกราฟิกหลายระดับ\nพรีเซ็ตระดับที่สูงกว่าให้คุณภาพกราฟิกดีกว่า แต่ประสิทธิภาพต่ำลง\nพรีเซ็ตระดับที่ต่ำกว่าจะลดคุณภาพกราฟิก เพื่อให้ประสิทธิภาพดีขึ้น",
    "rationale": "More idiomatic for tier options and eliminates the repetitive sound clash of ต่ำลงลด."
  },
  {
    "key": "UI/Settings/Tooltips/ShadowQuality",
    "current_thai": "เลือกระดับความละเอียดของเงา\nความละเอียดของเงาที่สูงขึ้นทำให้ดูคมชัดกว่า\nเลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพกราฟิก",
    "proposed_thai": "เลือกระดับความละเอียดของเงา\nความละเอียดของเงาที่สูงขึ้นจะช่วยให้เงาดูคมชัดขึ้น\nเลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพกราฟิก",
    "rationale": "Eliminates dangling comparative (ทำให้ดูคมชัดกว่า) by adding proper subject and natural ending."
  },
  {
    "key": "UI/Settings/Tooltips/MSAASamples",
    "current_thai": "เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก หรือลดลงเพื่อเพิ่มประสิทธิภาพกราฟิก",
    "proposed_thai": "เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก",
    "rationale": "Adds explicit object to reduce (ลดจำนวนลง) for smoother reading rhythm."
  }
]
```
