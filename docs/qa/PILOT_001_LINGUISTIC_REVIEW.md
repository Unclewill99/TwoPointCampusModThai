# Independent Linguistic & Token QA Review — PILOT-001 r2

> **Document:** `docs/qa/PILOT_001_LINGUISTIC_REVIEW.md`  
> **Reviewer:** Antigravity (QA Agent)  
> **Target Translation File:** `local/translations/PILOT-001.th.r2.json`  
> **Baseline Source File:** `local/source/PILOT-001.json`  
> **Reference Guidelines:** `docs/TRANSLATION_STYLE_APPROVAL_v0.2.md`, `docs/PILOT_001_REVIEW.md`, `docs/PILOT_001_R2_REVIEW.md`  
> **Date:** 2026-10-15  
> **Overall QA Status:** LINGUISTIC REVIEW COMPLETED — RUNTIME IN-GAME RENDERING REMAINS `NOT_RUN`

---

## 1. Executive Summary

An independent linguistic, semantic, terminology, humor, and token audit of all 50 records in `PILOT-001.th.r2.json` against `local/source/PILOT-001.json` was conducted.

### Key Highlights:
1. **Token & Marker Integrity (100% Pass):**
   - Candidate tokens across all 50 records match the source exactly (0 syntax mismatches, 0 dropped tokens, 0 unescaped brackets).
   - Specialized delimiters are correctly preserved: `[i2p_One]` in `UI/CourseManagement/CoursePointsFormat`, `<br>` in `UI/ChallengeMode/ChallengeModeUnlockTooltip`, and line breaks (`\n`) in Advisor/Challenge score records.
   - Developer sentinel `SHOULDN'T_HAVE_TITLE` in `Advisor_Course_Licensed_Title` is preserved verbatim per Controller directive.
2. **Evaluation of Revision 2 (r2) Targeted Changes:**
   - `Advisor_Characters_Personal_Goals`: The revision successfully eliminated redundant phrasing (`ยังมี...ที่ยัง...`) and replaced the speculative "ตอบรับคำขอ" with the neutral and accurate "ตอบกลับคำขอบางส่วนดู".
   - `Archaeology_YearTwo_DigSite_1`: Replacing "พังแล้วคือจบ" with "ค่อย ๆ ขุด: ทำพังแล้วก็พลาดเลย" successfully removed the unsupported "game over" implication.
3. **Primary Linguistic Findings & Recommendations:**
   - **Critical/Moderate Terminology Defect:** `UI/Settings/AudioLanuuage` translated as `"ภาษาเสียง"` sounds unnatural and overly literal. Standard game UI terminology is `"ภาษาเสียงพากย์"` or `"เสียงพากย์"`.
   - **Minor UI Naturalness Improvements:** Settings toggle `CameraShake` (`"กล้องสั่น"`) should preferably be nominalized as `"การสั่นของกล้อง"`; Advisor class notification (`"เรียนจบคาบเรียน: {CLASS}"`) is slightly repetitive and would read cleaner as `"เรียนจบคาบ: {CLASS}"`.
   - **Humor & Wordplay Assessment (`JOKE_UNRESOLVED`):** Detailed editorial analysis provided for `Can You Dig It?`, `Dating Algorithms`, and `Easy Does It`.

---

## 2. Detailed Findings by String ID & Key

| Item & Key | Source English | Thai Translation (r2) | Category | Severity | Detailed Rationale & Context | Suggested Fix / Recommendation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **[02]**<br>`UI/Settings/AudioLanuuage` | Audio Language *(source typo)* | ภาษาเสียง | Terminology / Naturalness | **Moderate** | ในบริบทหน้าต่างตั้งค่าของเกม คำว่า "ภาษาเสียง" ฟังดูแข็งและแปลตรงตัวเกินไป (literal translation) ภาษาไทยมาตรฐานในวงการเกมใช้คำว่า "ภาษาเสียงพากย์" (เพื่อแยกชัดเจนจาก "ภาษาข้อความ / ภาษาคำบรรยาย") | เสนอปรับเป็น: **`ภาษาเสียงพากย์`** (หรือ `เสียงพากย์`) |
| **[07]**<br>`UI/Settings/CameraShake` | Camera Shake | กล้องสั่น | Naturalness / UI Style | **Minor** | ในเมนูตั้งค่าที่เป็น Toggle เปิด/ปิด ป้ายกำกับควรเป็นอาการ/เอฟเฟกต์เชิงนามธรรม คำว่า "กล้องสั่น" ให้ความรู้สึกเหมือนประโยคบอกเล่าว่ากล้องกำลังสั่น | เสนอปรับเป็น: **`การสั่นของกล้อง`** (ตรงตามตัวเลือกสำรองของ Claude) |
| **[32]**<br>`Courses/Classes/Archaeology_YearOne_Lecture_1` | Can You Dig It? | ขุดแล้วเข้าใจไหม? | Humor / Cultural Tone | **Moderate** | ต้นฉบับเล่นสำนวนสแลงยุค 70s "Can you dig it?" (เข้าใจ/เก็ต/ชอบไหม) ผสมกับ "ขุดดิน" ในวิชาโบราณคดีปี 1 การแปลว่า "ขุดแล้วเข้าใจไหม?" เป็นลูกผสมที่สื่อความหมายได้ครบ แต่ในภาษาไทยฟังดูเป็นประโยคคำถามที่ห้วนและติดขัด ไม่เหมือนชื่อคอร์สบรรยายที่น่าดึงดูด | เสนอพิจารณา 2 แนวทาง:<br>1. *คงมุกสแลง:* **`ขุดแล้วเก็ตไหม?`**<br>2. *เน้นธรรมชาติและท้าทาย:* **`ขุดไหวไหม?`** (ตรงตาม Alt ของ Claude) |
| **[37]**<br>`Courses/Classes/Archaeology_YearThree_Science` | Dating Algorithms: How Old Is It? | อัลกอริทึมหาอายุ: นี่อายุเท่าไร? | Humor / Terminology | **Informational** (Accepted) | ต้นฉบับเล่นคำว่า "Dating" (การคำนวณหาอายุทางโบราณคดี เช่น คาร์บอน-14 vs อัลกอริทึมแอปหาคู่) การคงคำแปล "อัลกอริทึมหาอายุ" ตามมติ Controller มีความถูกต้องทางวิชาการและไม่ทำให้ผู้เล่นสับสนกับระบบความสัมพันธ์ | **คงตาม r2** (`อัลกอริทึมหาอายุ: นี่อายุเท่าไร?`) |
| **[39]**<br>`Courses/Classes/Archaeology_YearTwo_DigSite_1` | Easy Does It: You Break It, You've Blown It | ค่อย ๆ ขุด: ทำพังแล้วก็พลาดเลย | Humor / Naturalness | **Minor** | ต้นฉบับล้อสำนวนการค้า "You break it, you bought it" เปลี่ยนเป็น "you've blown it" การแก้ใน r2 เป็น "ทำพังแล้วก็พลาดเลย" ปลอดภัยจากการเคลม game-over แต่คำว่า "พลาดเลย" ยังฟังดูลอยๆ ในบริบทโบราณคดี การใช้คำว่า "เสียของ" จะตรงกับมิติของโบราณวัตถุล้ำค่าที่พังเสียหาย | เสนอพิจารณา: **`ค่อย ๆ ขุด: ถ้าทำพัง ก็เสียของเลย`** (หรือ `ค่อย ๆ ขุด: พังแล้วพังเลย`) |
| **[41]**<br>`Advisor/Advisor_Characters_Personal_Goals` | Lots of our students have unfulfilled personal goals. Consider checking your inbox and responding to some requests. | นักศึกษาจำนวนมากมีเป้าหมายส่วนตัวที่ยังไม่สำเร็จ ลองเปิดกล่องข้อความแล้วตอบกลับคำขอบางส่วนดู | Meaning / Context | **Informational** (Verified) | แก้ไขใน r2 ได้สละสลวยขึ้นมาก ตัดคำซ้ำซ้อน "ยังมี...ที่ยัง..." ออก และเปลี่ยน "ตอบรับคำขอ" เป็น "ตอบกลับคำขอบางส่วนดู" ซึ่งตรงกับ "responding to some requests" โดยไม่การันตีว่าจะต้องอนุมัติคำขอ | **คงตาม r2** (คงธง `AMBIGUOUS` ไว้จนกว่าจะยืนยันชื่อปุ่ม/หน้าต่าง Inbox ในเกมจริง) |
| **[48], [49]**<br>`Advisor/Advisor_Favourite_Student_Class_Complete`<br>& `_Class_Risk` | Student {NAME} ({COURSE}) finished a class: {CLASS}. ... | นักศึกษา {NAME} ({COURSE}) เรียนจบคาบเรียน: {CLASS} ... | Naturalness / Conciseness | **Minor** | วลี "เรียนจบคาบเรียน: {CLASS}" มีคำว่า "เรียน" ซ้อนกันสองครั้ง ทำให้เยิ่นเย้อ โดยเฉพาะเมื่อต้องแสดงผลในกล่องข้อความแจ้งเตือนที่มีพื้นที่จำกัด | เสนอปรับเป็น: **`เรียนจบคาบ: {CLASS}`** (กระชับและเป็นธรรมชาติกว่า) |
| **[29]**<br>`UI/CourseManagement/CoursePointsFormat` | {POINTS} Course points[i2p_One]{POINTS} point | {POINTS} แต้มหลักสูตร[i2p_One]{POINTS} แต้ม | Plural / Token Syntax | **Informational** (Accepted) | โครงสร้าง `[i2p_One]` ถูกเก็บไว้อย่างถูกต้องทั้งสองกิ่ง แม้ภาษาไทยจะไม่มีรูปพหูพจน์ แต่การจับคู่ "แต้มหลักสูตร" สำหรับหลายแต้ม และ "แต้ม" สำหรับเอกพจน์ สามารถทำงานได้โดยไม่ทำให้ syntax เสียหาย | **คงตาม r2** (รอทดสอบ runtime branch switching ใน Prototype) |
| **[44]**<br>`Advisor/Advisor_Course_Licensed_Title` | SHOULDN'T_HAVE_TITLE | SHOULDN'T_HAVE_TITLE | Sentinel Marker | **Informational** (Verified) | ตัวแปร Dev Sentinel ของผู้พัฒนา ถูกคงค่าเดิมไว้ ไม่มีการแปลหรือดัดแปลง ถูกต้องตามคำสั่ง Controller | **คงตาม r2** |

---

## 3. Systematic Verification Matrix

### 3.1 Token & Special Character Verification
- **Total Records:** 50
- **Syntax / Token Violations:** 0
- **Bracket Matching:** All `{TOKEN}` pairs verified balanced and intact.
- **Formatting Tags:**
  - `<br>` in `UI/ChallengeMode/ChallengeModeUnlockTooltip`: Preserved intact.
  - Newlines (`\n`) in `UI/ChallengeMode/BestTrophyAndScore` and `Advisor/Advisor_Favourite_Student_*`: Preserved in matching positions.
  - Whitespace around `{ROOM}` and `{CLASS}` in `Advisor_Class_Primary_Available`: Evaluated as a valid QA observation; visual spacing will be confirmed when rendered with actual font assets.

### 3.2 Glossary Consistency Check
- **G001 (Campus -> วิทยาเขต):** Consistently applied in `UI/Advisor/CampusLevelUp` ("วิทยาเขตเลื่อนระดับ") and `UI/Advisor/ResearchAvailable` ("วิทยาเขตของเรา").
- **G002 (Student -> นักศึกษา):** Consistently applied across all student-related strings (`UI/AdditionalStudents`, `Advisor_*`).
- **G003 (Staff):** Appropriately adapted as "คณาจารย์" (Teaching Staff) in `UI/Advisor/ResearchAvailable` and "ค่าธรรมเนียมสรรหา" (Staff Hire) in `Code/InspectorStaffHire_*`.
- **Level Distinction:**
  - Campus progression level = "ระดับ" (`CampusLevelUp` -> "วิทยาเขตเลื่อนระดับ")
  - Stage/Mission level = "ด่าน" (`Freshleigh Meadows (Level 1)` -> "Freshleigh Meadows (ด่านที่ 1)")
  - *QA Assessment:* Clear, context-aware distinction that prevents player confusion.

---

## 4. Summary of Proposed Changes for Controller / Translator

If approved by the Controller, the following minor edits are recommended for the next translation revision:

```json
[
  {
    "key": "UI/Settings/AudioLanuuage",
    "current_thai": "ภาษาเสียง",
    "proposed_thai": "ภาษาเสียงพากย์",
    "rationale": "More natural and standard in Thai gaming UI."
  },
  {
    "key": "UI/Settings/CameraShake",
    "current_thai": "กล้องสั่น",
    "proposed_thai": "การสั่นของกล้อง",
    "rationale": "Standard nominalized toggle label in settings menus."
  },
  {
    "key": "Courses/Classes/Archaeology_YearOne_Lecture_1",
    "current_thai": "ขุดแล้วเข้าใจไหม?",
    "proposed_thai": "ขุดแล้วเก็ตไหม?",
    "rationale": "More natural and humorous for a lecture title while preserving the double entendre."
  },
  {
    "key": "Courses/Classes/Archaeology_YearTwo_DigSite_1",
    "current_thai": "ค่อย ๆ ขุด: ทำพังแล้วก็พลาดเลย",
    "proposed_thai": "ค่อย ๆ ขุด: ถ้าทำพัง ก็เสียของเลย",
    "rationale": "Better cultural fit for breaking a valuable archaeological discovery."
  },
  {
    "key": "Advisor/Advisor_Favourite_Student_Class_Complete",
    "current_thai": "นักศึกษา {NAME} ({COURSE}) เรียนจบคาบเรียน: {CLASS}\nเกรดปัจจุบันคือ {GRADE} ({SCORE})",
    "proposed_thai": "นักศึกษา {NAME} ({COURSE}) เรียนจบคาบ: {CLASS}\nเกรดปัจจุบันคือ {GRADE} ({SCORE})",
    "rationale": "Eliminates repetitive phrasing 'เรียนจบคาบเรียน' and saves UI space."
  },
  {
    "key": "Advisor/Advisor_Favourite_Student_Class_Risk",
    "current_thai": "นักศึกษา {NAME} ({COURSE}) เรียนจบคาบเรียน: {CLASS} แต่อาจเสี่ยงไม่ผ่าน\nเกรดปัจจุบันคือ {GRADE} ({SCORE})",
    "proposed_thai": "นักศึกษา {NAME} ({COURSE}) เรียนจบคาบ: {CLASS} แต่อาจเสี่ยงไม่ผ่าน\nเกรดปัจจุบันคือ {GRADE} ({SCORE})",
    "rationale": "Eliminates repetitive phrasing 'เรียนจบคาบเรียน' and saves UI space."
  }
]
```

---

## 5. Scope Boundaries & Compliance

- **No Translation Files Modified:** `local/translations/PILOT-001.th.r2.json` and `local/source/PILOT-001.json` remain completely untouched.
- **No Git Operations Performed:** No branch switches, commits, or pushes were executed in the shared workspace.
- **In-Game Rendering Status:** All visual tests remain strictly **`NOT_RUN`** pending the delivery of an executable reversible prototype from the Controller.
