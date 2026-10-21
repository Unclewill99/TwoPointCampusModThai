# WO-DROPDOWN-002 QA Report — ASCII Marker Control (`community-merge-004`)

- **Date:** 2026-10-21
- **Candidate:** `community-merge-004` (Font/UI identical to `community-merge-002`; six `LogLevel` option translations replaced with `CHECK ` + original English)
- **Verdict:** **`CHECK_VISIBLE`**
- **Exact Visible Caption (`ระดับบันทึก` / `LogLevel`):** `CHECK Error`
- **Primary Evidence:** [01-settings-game-loglevel.jpg](../../local/qa/WO-DROPDOWN-002/01-settings-game-loglevel.jpg)
- **Active Elapsed Time:** ~3 minutes (21:33–21:36 ICT; target cap: 5 minutes)
- **Capture Count:** 1 primary screenshot, 0 recoveries (direct navigation from the Main Menu `การตั้งค่า` button to `การตั้งค่า > เกม`; no dropdown opened, no values modified, no tooltips triggered)

---

## 1. Environment, Capture Dimensions & UI Scale Uncertainty

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Raw Runtime Capture (`ImageGrab.grab()`):** `3840 x 2160` (Full Screen Window)
- **Saved Capture Dimensions & Resizing:** `1920 x 1080` JPEG, downsampled from `3840 x 2160` using `PIL.Image.Resampling.LANCZOS` in `tools/qa_driver.py`
- **UI Scale:** Expected `Medium` from unchanged host configuration, but **unverified in-screen** because the `ขนาด UI` (`UI Scale`) selected caption box remains blank (no inference made from the blank control).

---

## 2. Observation Summary (`Settings > เกม`)

| Control / Element | Candidate State in `community-merge-004` | Observed State in [01-settings-game-loglevel.jpg](../../local/qa/WO-DROPDOWN-002/01-settings-game-loglevel.jpg) | Notes |
|---|---|---|---|
| **`ระดับบันทึก` (`LogLevel`) Selected Caption** | 6 option strings set to `CHECK ` + original English (font/UI unchanged from `merge-002`) | **`CHECK_VISIBLE`** (`CHECK Error`) | Renders `CHECK Error` cleanly inside the orange dropdown box, proving the localisation bundle wire-up for `LogLevel` options is active at runtime when the string is ASCII. |
| **Adjacent Dropdowns (`ความถี่การบันทึกอัตโนมัติของเกม`, `ความถี่บันทึกอัตโนมัติโหมดอาชีพ`, `ภาษา`, `ภาษาเสียงพากย์`, `ขนาด UI`)** | Unchanged from `community-merge-002` | **Blank** | All 5 adjacent cyan dropdown boxes with Thai option strings remain blank. |
| **Static Row Labels & Toggles (`ระดับบันทึก`, `ปิด`/`เปิด`, `กลับสู่ค่าเริ่มต้น`)** | Unchanged from `community-merge-002` | **Visible Thai** | Left-hand labels, header (`การตั้งค่า`, `เกม`, `เครดิต`), and toggle buttons render readable Thai. |

*Scope Note:* No Thai dropdown fix is claimed by this control test. No dropdown lists were opened and no additional screens were tested.

---

## 3. Compact Lifecycle & Restoration Verification Output

All lifecycle commands were executed with `TPC.exe` closed. Original backups are retained under `local/backups/community-merge-004/`.

```json
// 1. Pre-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. Install community-merge-004
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 3. Post-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4–5. Steam launch, single capture of Settings > Game, normal Quit via Main Menu (TPC.exe exited cleanly)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
