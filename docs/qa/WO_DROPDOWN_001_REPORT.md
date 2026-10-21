# WO-DROPDOWN-001 QA Report — One-Caption Font Diagnostic (`community-merge-003`)

- **Date:** 2026-10-21
- **Candidate:** `community-merge-003` (direct Thai primary-font/material `m_fontAsset`/`m_sharedMaterial` on `LogLevel` selected caption object `295032210435112665` only; localisation and font bundles identical to `community-merge-002`)
- **Result:** **`STILL_BLANK`**
- **Primary Evidence:** [01-settings-game-loglevel.jpg](../../local/qa/WO-DROPDOWN-001/01-settings-game-loglevel.jpg)
- **Active Elapsed Time:** ~3 minutes (21:20–21:23 ICT; budget cap: 10 minutes)
- **Capture Count:** 1 primary screenshot, 0 recoveries (direct navigation to `การตั้งค่า > เกม` via the `การตั้งค่า` button on the Main Menu; did not enter Mods, did not open dropdowns, did not trigger tooltips)

---

## 1. Environment & Capture Dimensions

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Raw Runtime Capture (`ImageGrab.grab()`):** `3840 x 2160` (Full Screen Window)
- **Saved Capture Dimensions & Resizing:** `1920 x 1080` JPEG, downsampled from `3840 x 2160` using `PIL.Image.Resampling.LANCZOS` in `tools/qa_driver.py`
- **UI Scale:** Expected `Medium` from unchanged host settings, but **unverified in-screen** because the `ขนาด UI` (`UI Scale`) selected caption remains blank (no inference made from the blank control).

---

## 2. Observation Summary (`Settings > เกม`)

| Control / Element | Patch State in `community-merge-003` | Observed State in [01-settings-game-loglevel.jpg](../../local/qa/WO-DROPDOWN-001/01-settings-game-loglevel.jpg) | Notes |
|---|---|---|---|
| **`ระดับบันทึก` (`LogLevel`) Selected Caption** | Patched (`m_fontAsset` / `m_sharedMaterial` on `295032210435112665`) | **`STILL_BLANK`** | Completely empty orange caption area (`x=565..860, y=258..284` has minimum R=236; zero dark or light glyph pixels). Readability, clipping, and apparent glyph size vs. row labels cannot be evaluated because no characters rendered. |
| **Adjacent Dropdowns (`ความถี่การบันทึกอัตโนมัติของเกม`, `ความถี่บันทึกอัตโนมัติโหมดอาชีพ`, `ภาษา`, `ภาษาเสียงพากย์`, `ขนาด UI`)** | Intentionally unchanged | **Blank** | All 5 adjacent cyan dropdown boxes remain completely blank, matching `community-merge-002`. |
| **Static Row Labels & Toggles (`ระดับบันทึก`, `ปิด`/`เปิด`, `กลับสู่ค่าเริ่มต้น`)** | Unchanged from `community-merge-002` | **Visible Thai** | Left-hand labels, header (`การตั้งค่า`, `เกม`, `เครดิต`), and toggle buttons render readable Thai. |

*Scope & Diagnostic Note:* Assigning the Thai primary font and material directly to caption object `295032210435112665` did not make the `ระดับบันทึก` selected caption appear at runtime. Fine shaping remains unverified. No dropdown lists were opened and no values were modified.

---

## 3. Lifecycle & Restoration Verification Output

All commands were executed with `TPC.exe` closed. Original backups are retained under `local/backups/community-merge-003/`.

```json
// 1. Pre-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. Install community-merge-003
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 3. Post-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4–5. Steam launch, single capture of Settings > Game, normal Quit via Main Menu (TPC.exe exited cleanly)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
