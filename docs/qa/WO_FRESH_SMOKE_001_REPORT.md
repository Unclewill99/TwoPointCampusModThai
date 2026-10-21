# WO-FRESH-SMOKE-001 QA Report — Full Fresh Corpus, Bounded Practical Sample (`fresh-translation-004`)

- **Date:** 2026-10-22
- **Candidate:** `fresh-translation-004` (First runtime check of full fresh translation corpus)
- **Verdict:** **`SETUP_LIMIT`** *(also **`INCONCLUSIVE`** for target Views 1–3; mouse-input delivery under `qa_driver.py` was blocked after the first Mods click and by a Windows Snipping Tool overlay / window-focus collision, leaving `Settings > เกม` and `Freshleigh Meadows` unreached within the strict 1-recovery-per-view cap)*
- **Active Elapsed Time:** ~4 minutes (00:32–00:36 ICT; target cap: 15 minutes)
- **Capture & Recovery Counts:** 2 base captures + 2 recoveries = 4 image files under `local/qa/WO-FRESH-SMOKE-001/` (strictly capped at 1 base + 1 recovery for attempted Views 1 and 2; View 3 `NOT_RUN` with 0 captures)

---

## 1. Environment, Settings, Capture Resizing & Campus/Pause State

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Raw Runtime Capture (`ImageGrab.grab()`):** `3840 x 2160` (Full Screen Window; graphics and UI settings untouched)
- **Saved Capture Dimensions & Resizing:** `1920 x 1080` JPEG, downsampled from `3840 x 2160` using `PIL.Image.Resampling.LANCZOS` in [`tools/qa_driver.py`](../../tools/qa_driver.py)
- **Actual UI Scale:** Not directly observed in-screen (`Settings > เกม` was not reached within the 1-recovery limit; `localpreferences.json` and `Cloud/<AccountID>/preferences.json` remained at the existing `Medium` baseline).
- **Campus & Pause State:** **`NOT_RUN`** (`Slot1 / Freshleigh Meadows` (`8000.sav`) was not entered because Main Menu navigation did not advance past the Main Menu within View 2's 1-recovery cap; zero simulation time elapsed in campus, zero rooms built, zero staff hired, zero money spent, academic year not started).

---

## 2. Three-View Screening Results Table

| View # | Target View | Base Screenshot | Recovery Screenshot | Captures (Base + Recovery) | Status | Key Observations |
|:---:|---|---|---|:---:|---|---|
| **1** | **Main-Menu `Settings > Game` (`การตั้งค่า > เกม`)** | [01-settings-game.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game.jpg) *(Main Menu)* | [01-settings-game-r1.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game-r1.jpg) *(Mods screen / `ม็อดแนะนำ`)* | 1 + 1 | **`SETUP_LIMIT` / `INCONCLUSIVE`** *(Target tab unreached within 1-recovery cap)* | Base capture landed on the Main Menu after splash dismissal. The 1 permitted recovery click hit `ม็อด` (`Mods`) just above `การตั้งค่า` (`Settings`), opening the Mods screen (`ย้อนกลับ`, `เรียกดู`, `คอลเลกชัน`, `ไปที่ Mod.io`, `ค้นหาและกรอง`, `ม็อดแนะนำ`, `สมัครรับ`, `ตัวเลือกเพิ่มเติม`, `คะแนนสูงสุด`). Stopped at 1 recovery per brief. |
| **2** | **Continue `Slot1` / `Freshleigh Meadows` (`8000.sav`) — Initial Campus Modal or Paused HUD** | [02-campus-initial.jpg](../../local/qa/WO-FRESH-SMOKE-001/02-campus-initial.jpg) *(Main Menu with Windows Snipping Tool overlay)* | [02-campus-initial-r1.jpg](../../local/qa/WO-FRESH-SMOKE-001/02-campus-initial-r1.jpg) *(Main Menu unchanged)* | 1 + 1 | **`SETUP_LIMIT` / `INCONCLUSIVE`** *(Campus unreached within 1-recovery cap)* | Returned from Mods to Main Menu, where `Slot1` (`Two Point`) is visible with button `ต่อไป` (`Continue`). A Windows `Snipping Tool` notification (`Screenshot copied to clipboard`) and a background window matching `'two point'` (`Two Point Campus Mod QA -...`) intercepted/prevented the click on `ต่อไป` (`x=142, y=390`) from registering in both base and recovery attempts. Stopped at 1 recovery per brief. |
| **3** | **Dismiss Initial Modal Once (`ตกลง`) -> Immediate Pause -> Read-Only Staff/Recruitment Overview (`อาจารย์`/`ผู้ช่วย`/`ภารโรง`) or HUD/Objective** | — | — | 0 + 0 | **`NOT_RUN`** | Unreached because View 2 did not enter `Freshleigh Meadows` within the 1-recovery cap. Per brief, unreached UI stays `NOT_RUN` rather than forcing extra recovery clicks. |

---

## 3. Visible Failures, Open Known Defects & Up to Five Language Observations

### Visible Technical Failures in Observed Screens (Main Menu & Mods Screen)
- **No new rendering crashes, missing-glyph boxes, or raw tags observed** on the two screens actually reached ([01-settings-game.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game.jpg) Main Menu and [01-settings-game-r1.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game-r1.jpg) Mods screen).
- **Unreached Target Checks (`NOT_RUN`):**
  - `Settings > เกม` fresh translated dropdown selected values/labels, blank-dropdown check, clipping, arrow overlap, and in-screen UI scale read: **`NOT_RUN`**.
  - `Freshleigh Meadows` initial campus modal (`วันแรกของการเปิดเรียน`), course name, dynamic number, pause control, and staff/recruitment categories (`อาจารย์`/`ผู้ช่วย`/`ภารโรง`): **`NOT_RUN`**.

### Status of Known Open Renderer Defects & Pending Terminology
1. **[`BUG-THAI-003`](BUG_THAI_003.md) — Tone Mark / Nikkhahit Collision in `ต่ำ` (`ต` + `่` + `ำ`):**
   - **Status:** Remains **OPEN** (`NOT_OBSERVED` in this run because `Freshleigh Meadows` modal was not reached). Not claimed fixed.
2. **[`BUG-THAI-002`](BUG_THAI_002.md) — Internal Thai Word Splitting at Line Wraps:**
   - **Status:** Remains **OPEN** (`NOT_OBSERVED` in this run because multi-line modal/tooltip text was not reached). Not claimed fixed.
3. **[`BUG-THAI-001`](BUG_THAI_001.md) — Upper Vowel / Tone Mark Positioning (`ถี่`):**
   - **Status:** Remains **OPEN for broader regression tracking** (`ความถี่...` labels on `Settings > เกม` were `NOT_RUN` in this session).
4. **Pending Terminology & Full Corpus Status:**
   - Course names, staff categories (`อาจารย์`/`ผู้ช่วย`/`ภารโรง`), settings labels, and full fresh translation corpus remain **unapproved / pending verification**.

### Representative Language Observations from Observed Fresh Corpus Screens (Up to 5)
1. **Third-Party Credit Banner Removed from Main Menu Greeting ([01-settings-game.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game.jpg)):**
   - Top-center greeting now reads **`ยินดีต้อนรับกลับมา Willy`** (`Welcome Back Willy`), replacing the old community-merge watermark (`ม็อดจัดทำและแจกฟรีโดย ไม่เมาไม่แปล`).
2. **Main Menu `Continue` Button Translated as `ต่อไป` Instead of `ดำเนินการต่อ` ([01-settings-game.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game.jpg)):**
   - In `fresh-translation-004`, the primary `Continue` button on the Main Menu reads **`ต่อไป`** (literally `"Next"`), which is less clear as a Main Menu resume action than `ดำเนินการต่อ` or `เล่นต่อ`.
3. **Clean Thai Button Labels on Main Menu ([01-settings-game.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game.jpg)):**
   - Main Menu buttons render as `ต่อไป`, `เกมใหม่`, `โหลดเกม`, `โหมดความท้าทาย`, `แซนด์บ็อกซ์`, `ม็อด` (parenthetical `(Mods)` removed), `การตั้งค่า`, and `ออก`, plus County panel `ออกจากระบบแล้ว` / `เข้าสู่ระบบ`.
4. **Mods Screen (`ม็อด`) Fresh Labels ([01-settings-game-r1.jpg](../../local/qa/WO-FRESH-SMOKE-001/01-settings-game-r1.jpg)):**
   - Navigation and action controls on the Mods screen render readably in Thai: `ย้อนกลับ`, `เรียกดู`, `คอลเลกชัน`, `ไปที่ Mod.io`, `ค้นหาและกรอง`, `ม็อดแนะนำ`, `สมัครรับ`, `ตัวเลือกเพิ่มเติม`, and `คะแนนสูงสุด`.

---

## 4. Fresh Save Backup & Post-Run Save File Hash Summary

### Fresh Pre-Run Save Snapshot
- **Command:** `python tools/backup_gameplay_saves.py` (executed with Campus closed prior to probe installation)
- **Verified Output:**
  ```json
  {"backup": "D:\\SteamLibrary\\steamapps\\common\\Two Point Campus\\ThaiCampusMod\\local\\backups\\gameplay-save-snapshots\\20261021T173138185026Z.zip", "files": 10, "verified": true}
  ```
- **Adjacent Manifest Path:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261021T173138185026Z.json`

### Post-Run Save File Comparison Against `20261021T173138185026Z.json`
*(Live saves and all backups retained untouched; numeric Steam account ID redacted as `<AccountID>`)*

| Relative Path | Status | Pre-Run SHA-256 (Size) | Post-Run SHA-256 (Size) | Notes |
|---|---|---|---|---|
| `Cloud/<AccountID>/preferences.json` | **CHANGED** | `b77254aacb67c47afc0dc8c63db13c4624408fa949a8ff4e87342311d7a3a9a8` (761 B) | `f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e` (761 B) | Normal timestamp/session update on exit; no user settings changed |
| `Cloud/<AccountID>/userprofile.sav` | **CHANGED** | `3cd23d0277804af12f246b63b3a5509961f95108f830a97b0ec0d596c4252423` (1,064 B) | `dba79c529bb12ba78d113fc7e65e1ac14bbfe99af23c0ec7da357b3cdef35b50` (1,064 B) | Normal profile metadata update on exit |
| `Cloud/<AccountID>/Saves/Slot1/8000.sav` | **UNCHANGED** | `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d` (179,866 B) | `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d` (179,866 B) | Unchanged (`Freshleigh Meadows` save preserved byte-for-byte) |
| `Cloud/<AccountID>/Saves/Slot1/career.csav` | **UNCHANGED** | `cbbded52fde65f46da0c874a403280936286b31746ea6f17b5b38d0acadafc0b` (18,521 B) | `cbbded52fde65f46da0c874a403280936286b31746ea6f17b5b38d0acadafc0b` (18,521 B) | Unchanged |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.2.bak` | **UNCHANGED** | `f9730de46047fd6673d6ab5e408c0c5a3c71468b310809f4643fb341bd84219f` (18,521 B) | `f9730de46047fd6673d6ab5e408c0c5a3c71468b310809f4643fb341bd84219f` (18,521 B) | Unchanged |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.3.bak` | **UNCHANGED** | `dfd0601d068aa18807108560da1e16ad21da553a63e95cd4ea5b6bafbb1d5bba` (10,128 B) | `dfd0601d068aa18807108560da1e16ad21da553a63e95cd4ea5b6bafbb1d5bba` (10,128 B) | Unchanged |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.4.bak` | **UNCHANGED** | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) | Unchanged |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.5.bak` | **UNCHANGED** | `0b1b806f610227302896505fc901e2dfbd2bee4ad3b97475f2800b9968e79f76` (10,048 B) | `0b1b806f610227302896505fc901e2dfbd2bee4ad3b97475f2800b9968e79f76` (10,048 B) | Unchanged |
| `Cloud/<AccountID>/steam_autocloud.vdf` | **UNCHANGED** | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) | Unchanged |
| `localpreferences.json` | **UNCHANGED** | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) | Unchanged |
| *(New / Missing save files)* | **NONE** | — | — | 0 new save files, 0 missing save files |

---

## 5. Compact Three-Bundle Lifecycle & Restoration Verification Output

All lifecycle commands were executed with `TPC.exe` confirmed closed. Original bundle backups are retained under `local/backups/fresh-translation-004/`.

```json
// 1. Pre-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. Install fresh-translation-004
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 3. Post-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4–5. Steam launch, bounded 1-recovery attempts on Views 1–2, clean window close via WM_CLOSE (TPC.exe confirmed absent)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
