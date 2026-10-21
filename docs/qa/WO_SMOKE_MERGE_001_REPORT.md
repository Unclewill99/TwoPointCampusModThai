# WO-SMOKE-MERGE-001 QA Report — Merged Thai Mod (`community-merge-002`) One-Session Screening

- **Date:** 2026-10-21
- **Candidate:** `community-merge-002` (supersedes `community-merge-001` preparation; `probe-013` byte-identical font/UI baseline + 15,677 reloaded records)
- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Display & Capture Dimensions:**
  - Native Runtime Display: `Full Screen Window`, `3840 x 2160 @ 60hz` (`ImageGrab.grab()` raw dimensions: `3840 x 2160`)
  - Saved Capture Dimensions: `1920 x 1080` JPEG (downsampled from `3840 x 2160` via `PIL.Image.Resampling.LANCZOS` in `tools/qa_driver.py`)
  - UI Scale: `Medium` (retained from baseline environment; no settings sliders or presets modified)
- **Active Elapsed Time:** ~10 minutes (21:04–21:14 ICT; target budget: 20 minutes)
- **Screenshot & Recovery Counts:** 3 base screenshots + 3 recoveries = 6 captures total (strictly 1 base + 1 recovery per view; no coordinate sweeps)
- **Overall Screening Verdict:** **`BLOCKED`** (Confirmed blank-text defect in translated Settings dropdown controls across Views 2 and 3; View 3 tooltip hover sub-check **`INCONCLUSIVE`** within the 1-recovery cap)

---

## 1. Three-View Screening Results Table

| View # | Target View | Base Screenshot | Recovery Screenshot | Captures (Base + Recovery) | Observed Status | Key Findings |
|:---:|---|---|---|:---:|---|---|
| **1** | **Main Menu** | [01-main-menu.jpg](../../local/qa/WO-SMOKE-MERGE-001/01-main-menu.jpg) *(Splash / Legal screen)* | [01-main-menu-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/01-main-menu-r1.jpg) *(Main Menu)* | 1 + 1 | **PASS** *(Observed)* | Startup succeeded. All 8 main menu buttons (`ดำเนินการต่อ`, `เกมใหม่`, `โหลดเกม`, `โหมดท้าทาย`, `แซนด์บ็อกซ์`, `ม็อด (Mods)`, `การตั้งค่า`, `ออก`) and County login panel (`ออกจากระบบแล้ว`, `เข้าสู่ระบบ`) display readable Thai without missing glyphs or raw tags. |
| **2** | **Settings > General (`การตั้งค่า > เกม`)** | [02-settings-general.jpg](../../local/qa/WO-SMOKE-MERGE-001/02-settings-general.jpg) *(Landed on Mods screen)* | [02-settings-general-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/02-settings-general-r1.jpg) *(Settings > Game)* | 1 + 1 | **BLOCKED / FAIL** *(Observed)* | Setting row labels (`ระดับบันทึก`, `ปิดใช้งานการสั่นของกล้อง`, `ความถี่การบันทึกอัตโนมัติของเกม`, `ความถี่บันทึกอัตโนมัติโหมดอาชีพ`, `คำบรรยาย`, `ภาษา`, `ภาษาเสียงพากย์`, `ขนาด UI`), toggles (`ปิด`/`เปิด`), and buttons (`เครดิต`, `กลับสู่ค่าเริ่มต้น`) are readable. **Blocking defect:** all 6 dropdown selected-value boxes on this tab are **completely blank**. |
| **3** | **Settings > Video (`การตั้งค่า > Video`) + Translated Tooltip** | [03-settings-video-tooltip.jpg](../../local/qa/WO-SMOKE-MERGE-001/03-settings-video-tooltip.jpg) *(Video tab, hover attempt 1)* | [03-settings-video-tooltip-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/03-settings-video-tooltip-r1.jpg) *(Video tab, hover attempt 2)* | 1 + 1 | **BLOCKED / INCONCLUSIVE** *(Observed tab; tooltip hover not established within cap)* | Translated Video labels (`การตั้งค่าพื้นฐาน`, `โหมดเต็มหน้าจอ`, `ความละเอียด`, `นำไปใช้`, `ขีดจำกัดอัตราเฟรม`, `ไม่จำกัด`, `พื้นที่ปลอดภัย`, `ปรับ`, `ค่าที่ตั้งไว้ล่วงหน้าของคุณภาพ`, `ต่ำมาก`..`สูงมาก`, `การตั้งค่าขั้นสูง`, `โหมดการลบรอยหยัก`) render readably. **Blocking defect:** translated dropdown value boxes (`โหมดเต็มหน้าจอ`, `VSync`) are **completely blank**, while ASCII/numeric dropdowns (`3840 x 2160 @ 60hz`, `SMAA`) display text. Tooltip popup did not trigger within the 1-recovery limit due to window-focus matching a background window title; stopped per no-sweep rule. |

*Note on Scope Distinction:*
- **Observed `PASS`:** View 1 (Main Menu & Splash Screen) and static Thai labels/buttons on Views 2 and 3.
- **Observed `BLOCKED`:** Dropdown selected-value rendering across Views 2 and 3.
- **Observed `INCONCLUSIVE`:** View 3 tooltip hover capture (stopped at 1 recovery limit per brief).
- **`NOT_RUN` / `DEFERRED`:** Gameplay / save loading, Audio tab inspection, exhaustive translation accuracy review, fine vowel/tone shaping verification, and release readiness.

---

## 2. Blocking Defects & Layout Observations

1. **[BLOCKING] Blank Selected-Value Text in Translated Dropdown Controls (Views 2 & 3):**
   - **Evidence:** [02-settings-general-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/02-settings-general-r1.jpg) and [03-settings-video-tooltip.jpg](../../local/qa/WO-SMOKE-MERGE-001/03-settings-video-tooltip.jpg).
   - **Description:** Every dropdown control whose currently selected option string is localized into Thai renders an **empty/blank box**:
     - `Settings > เกม`: `ระดับบันทึก` (Log Level), `ความถี่การบันทึกอัตโนมัติของเกม` (Game Autosave Frequency), `ความถี่บันทึกอัตโนมัติโหมดอาชีพ` (Career Autosave Frequency), `ภาษา` (Language), `ภาษาเสียงพากย์` (Voice Language), and `ขนาด UI` (UI Scale) are all blank.
     - `Settings > Video`: `โหมดเต็มหน้าจอ` (Fullscreen Mode) and `VSync` are blank, whereas `ความละเอียด` (`3840 x 2160 @ 60hz`) and `โหมดการลบรอยหยัก` (`SMAA`) remain visible.
   - **Impact:** Players cannot see active settings for language, UI scale, display mode, VSync, or autosave frequency. In prior probes (`probe-018-800a/b`) where those option strings remained in English, the dropdown text rendered normally.
2. **[MINOR CLIPPING] Bottom Row Label Clipped at Scroll Viewport Edge (Views 2 & 3):**
   - **Evidence:** Bottom of the scroll list in [02-settings-general-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/02-settings-general-r1.jpg) (`การมองเห็นออนไลน์`) and [03-settings-video-tooltip.jpg](../../local/qa/WO-SMOKE-MERGE-001/03-settings-video-tooltip.jpg) (`คุณภาพการลบรอยหยัก`).
   - **Description:** The bottom-most visible row before scrolling is partially clipped vertically by the scroll container boundary above the `กลับสู่ค่าเริ่มต้น` button (also present in English baseline layout).

---

## 3. Up to Five Representative Translation & Mixed-Language Issues

1. **Third-Party Credit / Watermark Injected into UI & Legal Strings ([01-main-menu.jpg](../../local/qa/WO-SMOKE-MERGE-001/01-main-menu.jpg), [01-main-menu-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/01-main-menu-r1.jpg)):**
   - The top-center greeting banner (`Welcome Back`) is replaced with `ม็อดจัดทำและแจกฟรีโดย ไม่เมาไม่แปล`.
   - The startup copyright splash screen appends `และม็อดเกมนี้ จัดทำและแจกฟรีโดย ไม่เมาไม่แปล ขอขอบคุณผู้ให้การสนับสนุนหลักของเพจ คุณ จิรากร โรมานอฟสกี้ไพร์ส` to the Microsoft Azure PlayFab notice.
2. **Untranslated Sub-Tab Header `Video` ([03-settings-video-tooltip.jpg](../../local/qa/WO-SMOKE-MERGE-001/03-settings-video-tooltip.jpg)):**
   - While `Settings` (`การตั้งค่า`), `Game` (`เกม`), and `Credits` (`เครดิต`) are translated, the Video sub-tab header remains `Video` in English.
3. **Bilingual Menu Button Label `ม็อด (Mods)` ([01-main-menu-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/01-main-menu-r1.jpg)):**
   - The main menu button displays `ม็อด (Mods)` (mixing Thai and parenthetical English), whereas the Mods screen header ([02-settings-general.jpg](../../local/qa/WO-SMOKE-MERGE-001/02-settings-general.jpg)) uses `ม็อดยอดนิยม` without parenthetical English.
4. **Inconsistent Phrasing Across Adjacent Autosave Labels ([02-settings-general-r1.jpg](../../local/qa/WO-SMOKE-MERGE-001/02-settings-general-r1.jpg)):**
   - `Game Autosave Frequency` is translated as `ความถี่การบันทึกอัตโนมัติของเกม` (with `การ`), while the adjacent `Career Autosave Frequency` is translated as `ความถี่บันทึกอัตโนมัติโหมดอาชีพ` (omitting `การ`).
5. **Literal / Wordy Section Heading `ค่าที่ตั้งไว้ล่วงหน้าของคุณภาพ` ([03-settings-video-tooltip.jpg](../../local/qa/WO-SMOKE-MERGE-001/03-settings-video-tooltip.jpg)):**
   - `Quality Presets` is translated literally as `ค่าที่ตั้งไว้ล่วงหน้าของคุณภาพ`, which reads unnaturally compared to concise UI headings like `การตั้งค่าพื้นฐาน` and `การตั้งค่าขั้นสูง`.

*(Additional mixed-language note: Live/external service content such as the right-hand Discord promo card on the Main Menu and mod item titles like `Arcade Machines - Pack 1 of 3` on the Mods screen remain in English, as expected.)*

---

## 4. Lifecycle & Restoration Verification Output

All lifecycle commands were executed with `TPC.exe` confirmed closed. Backups are retained under `local/backups/community-merge-002/`.

```json
// 1. Pre-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. Install community-merge-002
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 3. Post-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4–5. Steam launch, 3-view screening, normal Quit via main menu (TPC.exe exited cleanly)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
