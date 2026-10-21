# WO-DROPDOWN-003 QA Report — Thai Caption Overflow Control (`community-merge-005`)

- **Date:** 2026-10-21
- **Candidate:** `community-merge-005` (`LogLevel` selected-caption object `295032210435112665` `m_overflowMode` changed from `1` to `0`; font, material, size, rect, and Thai localisation identical to `community-merge-002`)
- **Verdict:** **`THAI_VISIBLE_CONTAINED`**
- **Exact Visible Text (`ระดับบันทึก` / `LogLevel`):** `ข้อผิดพลาด`
- **Primary Evidence:** [01-settings-game-loglevel.jpg](../../local/qa/WO-DROPDOWN-003/01-settings-game-loglevel.jpg)
- **Active Elapsed Time:** ~3 minutes (21:41–21:44 ICT; target cap: 5 minutes)
- **Capture Count:** 1 primary screenshot, 0 recoveries (direct navigation from Main Menu `การตั้งค่า` button to `การตั้งค่า > เกม`; no dropdown opened, no values modified, no tooltips triggered)

---

## 1. Environment, Capture Dimensions & UI Scale Uncertainty

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Raw Runtime Capture (`ImageGrab.grab()`):** `3840 x 2160` (Full Screen Window)
- **Saved Capture Dimensions & Resizing:** `1920 x 1080` JPEG, downsampled from `3840 x 2160` using `PIL.Image.Resampling.LANCZOS` in `tools/qa_driver.py`
- **UI Scale:** Expected `Medium` from unchanged host configuration, but **unverified in-screen** because the `ขนาด UI` (`UI Scale`) selected caption box remains blank (no inference made from the blank control).

---

## 2. Observation Summary (`Settings > เกม`)

| Control / Aspect | Observed Result in [01-settings-game-loglevel.jpg](../../local/qa/WO-DROPDOWN-003/01-settings-game-loglevel.jpg) | Details |
|---|---|---|
| **`ระดับบันทึก` (`LogLevel`) Selected Caption Text** | **`ข้อผิดพลาด`** (Visible Thai) | Matches expected Thai translation of `Error`. |
| **Containment Relative to Orange Box** | **Contained** | Text sits cleanly inside the left side of the orange dropdown box with normal padding and wide clearance before the right dropdown arrow. |
| **Clipping / Crossing Arrow or Other Rows** | **None** | Upper tone mark (`้`) and upper vowel (`ิ`) are fully visible with no top/bottom/side clipping; text does not cross the arrow icon or adjacent rows. |
| **Missing Glyphs / Apparent Size** | **None / Normal** | Zero missing-glyph boxes; apparent font size and weight match the left-hand Thai row labels (`ระดับบันทึก`). |
| **Adjacent Unchanged Dropdowns (`ความถี่การบันทึกอัตโนมัติของเกม`, `ความถี่บันทึกอัตโนมัติโหมดอาชีพ`, `ภาษา`, `ภาษาเสียงพากย์`, `ขนาด UI`)** | **Blank** | All 5 untouched dropdown captions with `m_overflowMode = 1` remain blank, providing a clear within-screen contrast. |

*Scope Disclaimer:* This single-control result confirms `m_overflowMode: 1 -> 0` makes the `LogLevel` selected caption visible and contained for `ข้อผิดพลาด`, but does not by itself approve all dropdown controls, opened dropdown item lists, longer option strings, or fine Thai shaping.

---

## 3. Compact Lifecycle & Restoration Verification Output

All lifecycle commands were executed with `TPC.exe` confirmed closed. Original backups are retained under `local/backups/community-merge-005/`.

```json
// 1. Pre-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. Install community-merge-005
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 3. Post-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4–5. Steam launch, single capture of Settings > Game, normal Quit via Main Menu (TPC.exe exited cleanly)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
