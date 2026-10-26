# WO-VISUAL-019 report — fresh-translation-007 first screens (user captures, 2026-10-26)

Tester: user (Willy). Candidate installed and checked: fresh-translation-007, all three files `probe` (manage_probe output pasted in chat). Captures: four full-frame native 3840x2160 PNGs under local/qa/WO-VISUAL-019/ (user sent each twice; duplicates dropped). UI Scale per capture: NOT STATED by the tester → recorded UNKNOWN (cards look the same size as the 2026-10-26 Small evidence). Display/build string: not recorded.

| Cell | Screen / record | Observed rows | Result |
|---|---|---|---|
| P1 | Loading tip "ปูทางไป" (Tips_LS_Paths_Text) | not reached; a different tip was shown | NOT_EXERCISED |
| P1' | Loading tip "อุปกรณ์เฉพาะทาง" (Tips_LS_* specialist items) | `วางไอเท็มเฉพาะห้องโดยเลือกห้องแล้ว` / `เลือกตัวเลือก "เพิ่มไอเท็มลงในห้อง" จาก` / `ตัวตรวจสอบห้อง` | PASS — every edge on a word boundary (แล้ว|เลือก, จาก|ตัว), complete, no artifact |
| P2 | Freshleigh Meadows card (Level_Description), two captures with different presenter | `วิทยาลัยชนบทแห่งนี้มีความคาดหวังต่ำ` / `และมีคลองสวย เป็นที่เหมาะจะเริ่มต้น` / `อาชีพ` | PASS — the reported defect `ต่ำแล|ะมี` is gone (break now ต่ำ|และ at the proposed opportunity); ต่ำ ligature unchanged; third edge เริ่มต้น|อาชีพ is a word boundary |
| R-mail | Messages > Visit letter body | `กลุ่มว่าที่นักศึกษาสนใจความปกติเสมือน และหวังจะมาเยี่ยมชม` / `วิทยาเขต` | PASS — edge เยี่ยมชม|วิทยาเขต |

No visible glyph, dot or extra gap at any inserted U+200B position in body text; no missing text; no break after a leading vowel; no detached mark.

## Separate observation (not caused by 007)

The bold section header `การประเมินการเยี่ ยมชมโดยพิจารณาจาก:` shows a visible gap inside เยี่ยม. SEGMENTATION-002 places no cut there (cuts: การประเมิน|การ|เยี่ยมชม|โดย|พิจารณา|จาก:), so the gap comes from the bold/header font's advance for the ี + ่ stack, i.e. the BUG-THAI-001 shaping family, in the header font only. Needs a 006 comparison capture of the same screen to confirm it pre-exists. Logged as BUG-THAI-001 follow-up item, not a 007 regression.

## Not covered

Medium/Small pairs not distinguishable from the captures; Settings > Game, Video tooltips, opening modal and the ต่ำ/น้ำ screen map not re-checked. User continues normal play on 007 and will report anomalies.
