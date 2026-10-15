# Two Point Campus Thai Mod — QA Bug Report Template

> **Disclaimer:** Suggested fixes in reports are hypotheses until verified in a reproducible test environment. Severity must be assigned strictly based on gameplay/reading impact, not solely on visual category.

---

## Bug Report Form

```markdown
### [BUG-ID] Concise Summary (e.g., "[BUG-REND-001] Mai Tho overlaps Sara I on 3-level stack in Course Management")

- **Status:** [ FAIL | BLOCKED ]
- **Severity:** 
  - [ ] Critical (Game crash, freeze, fatal exception, or total UI lockup)
  - [ ] Major (Unreadable text, truncated meaning, essential gameplay info lost, broken variables)
  - [ ] Moderate (Noticeable rendering defect, e.g. floating mark / descender collision, but meaning still decipherable)
  - [ ] Minor (Cosmetic defect, minor kerning / padding discrepancy, low impact on readability)
- **Impact Assessment Rationale:** [Explain why this severity was assigned based on user comprehension & UI usability]

#### Environment & Build Configuration
- **Game Build:** [e.g. Campus 10.3.169253+2024-12-06.1241 / Unity 2020.3.47f1]
- **Prototype Revision:** [e.g. Controller-proto-rev-0.1.0]
- **Font Identity / Asset:** [e.g. NotoSansThai-Medium (Dynamic TMP) / Fallback Chain: Baloo -> NotoSansThai]
- **Atlas / Caching Mode:** [ Dynamic SDF / Static Pre-baked ]
- **Cold Restart Verified:** [ YES | NO | N/A ] (Required for dynamic fonts to verify cold cache vs hot cache)
- **Multi-Screen Stress Tested:** [ YES | NO | N/A ] (Check for dynamic atlas exhaustion after browsing multiple menus)
- **Display Resolution:** [e.g. 1920x1080, 2560x1440, etc.]
- **Actual In-Game UI Scale:** [Record exact slider value supported by the game engine, or N/A if unsupported]

#### Location & String Information
- **Screen / UI Area:** [e.g. Main Menu > Settings, Course Inspector Dialog, HUD Objective Banner]
- **String ID / Source Key:** [Stable String ID or catalog locator, e.g. UI/Buttons/Btn_Confirm]
- **English Source Text:** [Original English text if applicable]
- **Input Text:** [Exact text string passed to the renderer]
- **Unicode Code Points:** [Required for diagnostic cases, e.g. U+0E19 U+0E49 U+0E33]

#### Defect Classification
- [ ] Upper/Lower Vowel Placement (สระบน/ล่าง)
- [ ] Ascender Collision (ป, ฝ, ฟ ชนสระบน)
- [ ] Descender Truncation Failure (ญ, ฐ ไม่ตัดเชิงเมื่อมีสระล่าง)
- [ ] Deep Descender Collision (ฎ, ฏ ชนสระล่าง)
- [ ] Stacked Tone Mark / Floating Mark (วรรณยุกต์ลอย หรือ จม)
- [ ] Line Break / Syllable Clipping (ตัดคำกลางพยางค์ / สระหน้าตกค้าง)
- [ ] Text Overflow / Button Clipping (ข้อความล้นขอบ UI)
- [ ] Missing Glyph / Fallback Failure (Tofu / □)
- [ ] Tag / Placeholder Corruption (ตัวแปรไม่ถูกแทนที่ / Tag หลุด)
- [ ] Dynamic Atlas Exhaustion (ฟอนต์เบลอหรือหายหลังเปิดหลายหน้าต่าง)

#### Reproduction Steps
1. Launch game with prototype build `[revision]`.
2. Navigate to `[Screen / Menu]`.
3. Locate element `[Element Name / String ID]`.
4. Observe the rendering of the Thai text.

#### Results
- **Expected Behavior:** [Visual expectation verified against a trusted Thai reference renderer / standard Thai typography]
- **Actual Behavior:** [Exact visual defect observed in-game]
- **Visual Evidence:** `[Path or Link to Screenshot / Video, e.g. reports/screenshots/BUG-001.png]`

#### Diagnostic & Technical Hypothesis
- **TMP Inspection:** [Details on font size, RectTransform width/height, auto-sizing bounds, overflow mode]
- **Hypothesis / Suggested Action:** [Tentative hypothesis only; must be validated by Controller in engineering prototype]
```
