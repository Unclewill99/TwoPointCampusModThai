# WO-GAMEPLAY-002 QA Report — Enter First Campus, Initial Text Trial (`community-merge-006`)

- **Date:** 2026-10-21
- **Candidate:** `community-merge-006`
- **Verdict:** **`USABLE_IN_OBSERVED_CONTEXT`** *(Initial campus entry and opening modal in `เฟรชลีห์ เมโดวส์` displayed readable Thai with zero blocking technical defects; mid-word wrapping and translation accuracy issues noted below; optional overview panel `NOT_RUN` due to blocking initial modal)*
- **Active Elapsed Time:** ~11 minutes (22:08–22:19 ICT; target cap: 15 minutes)
- **Capture & Recovery Counts:** 3 base captures + 3 recoveries = 6 image files under `local/qa/WO-GAMEPLAY-002/` (1 base + 1 recovery per step; logical View 3 optional overview panel `NOT_RUN`)

---

## 1. Environment, Campus/Pause State & Steps Advanced

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Raw Runtime Capture (`ImageGrab.grab()`):** `3840 x 2160` (Full Screen Window; `Medium` UI scale and graphics settings unchanged)
- **Saved Capture Dimensions & Resizing:** `1920 x 1080` JPEG, downsampled from `3840 x 2160` using `PIL.Image.Resampling.LANCZOS` in `tools/qa_driver.py`
- **Selected Career & Campus:** `Slot1` (`Two Point` career) -> **`เฟรชลีห์ เมโดวส์` (`Freshleigh Meadows`)**, persisted by the game as `Slot1/8000.sav`.
- **Actual Pause State:** **Simulation held/paused by the initial blocking campus modal (`วันแรกของการเปิดเรียน` / `First Day of School`).** Standard HUD speed/pause controls were not yet exposed behind the modal. Per Rule 2 (*"If a modal blocks pause, capture it; do not dismiss further gameplay instructions just to expose the HUD"*), the modal's `ตกลง` (`OK`) button was not dismissed.
- **Exact Steps Advanced:**
  1. Clicked `ดำเนินการต่อ` (`Continue`) on the Main Menu to enter `Slot1`.
  2. Clicked the green `ถัดไป ->` (`Next`) button **3 times** (cap: 10) to complete Albert Crank's initial Campaign Map dialogue, which automatically opened the `เฟรชลีห์ เมโดวส์` start panel.
  3. Clicked the green `เริ่ม` (`Start`) button on the `เฟรชลีห์ เมโดวส์` start panel.
  4. Waited for the campus level load and opening camera flyover to settle on the initial `วันแรกของการเปิดเรียน` modal.
  5. Closed the game normally via `WM_CLOSE` without building rooms, hiring staff, spending money, or starting the academic year.

---

## 2. Three-View Screening Table

| View # | Target View | Base Screenshot | Recovery Screenshot | Captures (Base + Recovery) | Status | Key Observations |
|:---:|---|---|---|:---:|---|---|
| **1** | **Campaign Map Dialogue & `เฟรชลีห์ เมโดวส์` Start Panel** | [01-campaign-map-start.jpg](../../local/qa/WO-GAMEPLAY-002/01-campaign-map-start.jpg) *(Advisor line 2)* | [01-campaign-map-start-r1.jpg](../../local/qa/WO-GAMEPLAY-002/01-campaign-map-start-r1.jpg) *(`เฟรชลีห์ เมโดวส์` Start Panel)* | 1 + 1 | **OBSERVED (`PASS`)** | After 3 `ถัดไป` clicks, the `เฟรชลีห์ เมโดวส์` panel opened showing title `เฟรชลีห์ เมโดวส์`, description (`วิทยาลัยในชนบทแห่งนี้มีความคาดหวังต่ำและมีคลองที่ดี\nเป็นสถานที่ที่สมบูรณ์แบบในการเริ่มต้นอาชีพของคุณ`), `เงินทุนเริ่มต้น` (`500,000`), and `เริ่ม` button. All Thai text is readable and contained. |
| **2** | **`เฟรชลีห์ เมโดวส์` Initial Campus Load & Opening Modal (`วันแรกของการเปิดเรียน`)** | [02-campus-initial.jpg](../../local/qa/WO-GAMEPLAY-002/02-campus-initial.jpg) / [03-campus-hud-or-modal.jpg](../../local/qa/WO-GAMEPLAY-002/03-campus-hud-or-modal.jpg) | [02-campus-initial-r1.jpg](../../local/qa/WO-GAMEPLAY-002/02-campus-initial-r1.jpg) *(Flyover)* / [03-campus-hud-or-modal-r1.jpg](../../local/qa/WO-GAMEPLAY-002/03-campus-hud-or-modal-r1.jpg) *(Modal)* | 2 + 2 | **OBSERVED (`PASS` with wrapping/translation notes)** | Campus loaded through the opening flyover into the `วันแรกของการเปิดเรียน` modal (`ยินดีต้อนรับสู่เฟรชลีห์ เมโดวส์...`, `ข้อมูลหลักสูตร`, `วิทยาศาสตร์แผนที่`, `การรับนักเรียน 10`, `ตกลง`). No missing glyphs, blank fields, or raw tags; one mid-word wrap (`ของคุ`\|`ณ`) observed. |
| **3** | **Optional Read-Only Overview / Objectives Panel** | — | — | 0 + 0 | **`NOT_RUN`** *(Blocked by Initial Modal)* | The `วันแรกของการเปิดเรียน` modal blocks the main campus HUD, and dismissing gameplay instructions to expose the HUD is disallowed by the brief. |

*Scope Disclaimer:* This screening covers initial campus entry text only and does not constitute full gameplay, long-session, translation-accuracy, fine-shaping, or release acceptance.

---

## 3. Visible Technical Issues & Up to Five Language Observations

### Technical Rendering Defects
- **None observed:** Across [01-campaign-map-start.jpg](../../local/qa/WO-GAMEPLAY-002/01-campaign-map-start.jpg), [01-campaign-map-start-r1.jpg](../../local/qa/WO-GAMEPLAY-002/01-campaign-map-start-r1.jpg), and [03-campus-hud-or-modal-r1.jpg](../../local/qa/WO-GAMEPLAY-002/03-campus-hud-or-modal-r1.jpg), there are **zero blank text fields, zero missing-glyph boxes, zero raw placeholders/tags, and no box overflow/clipping**.

### Representative Language & Wrapping Observations (Up to 5)
1. **Mid-Word Line Wrap in Opening Modal (`ของคุ` | `ณ` — [03-campus-hud-or-modal-r1.jpg](../../local/qa/WO-GAMEPLAY-002/03-campus-hud-or-modal-r1.jpg)):**
   - The second paragraph of `วันแรกของการเปิดเรียน` wraps in the middle of the word `ของคุณ`:
     - Line 1: `ชนบททูพอยต์เป็นสถานที่ที่สมบูรณ์แบบในการเริ่มต้นอาชีพของคุ`
     - Line 2: `ณ เรียนรู้เคล็ดลับต่างๆ ทำผิดพลาด และเริ่มต้นด้วยรอยยิ้ม`
2. **Mistranslation of Fictional Course `Scientography` as `วิทยาศาสตร์แผนที่` ([03-campus-hud-or-modal-r1.jpg](../../local/qa/WO-GAMEPLAY-002/03-campus-hud-or-modal-r1.jpg)):**
   - Under `ข้อมูลหลักสูตร` (`Course Info`), `Scientography` is translated as `วิทยาศาสตร์แผนที่` (`"Map Science"`), confusing `Scientography` with `Cartography`.
3. **Inconsistent Rendering of `Two Point County` / `Freshleigh` ([01-campaign-map-start.jpg](../../local/qa/WO-GAMEPLAY-002/01-campaign-map-start.jpg) vs. [03-campus-hud-or-modal-r1.jpg](../../local/qa/WO-GAMEPLAY-002/03-campus-hud-or-modal-r1.jpg)):**
   - The advisor header writes `Two Point เค้าตี้` (English + `เค้าตี้`), the advisor body writes `วิทยาลัยเฟรชลีห์เคาน์ตี้` (`เคาน์ตี้`), and the campus modal writes `ชนบททูพอยต์` (transliterating `Two Point` into Thai script).
4. **Extra Space Inside Bolded Term (`ผู้ บริหารวิทยาเขต` — [01-campaign-map-start.jpg](../../local/qa/WO-GAMEPLAY-002/01-campaign-map-start.jpg)):**
   - In `คุณอาจจะไม่มีประสบการณ์ในฐานะ ผู้บริหารวิทยาเขต`, an internal space appears between `ผู้` and `บริหารวิทยาเขต`.
5. **Unnatural Word Choice `ต่ำต้อย` for Low Expectations ([03-campus-hud-or-modal-r1.jpg](../../local/qa/WO-GAMEPLAY-002/03-campus-hud-or-modal-r1.jpg)):**
   - `และความคาดหวังก็... ต่ำต้อย` uses `ต่ำต้อย` (lowly/inferior in social standing) for `"and expectations are... low"`, whereas the start card ([01-campaign-map-start-r1.jpg](../../local/qa/WO-GAMEPLAY-002/01-campaign-map-start-r1.jpg)) translates the same concept more naturally as `มีความคาดหวังต่ำ`.

---

## 4. Save Backup & Post-Run Save File Hash Summary

### Fresh Pre-Run Save Snapshot
- **Command:** `python tools/backup_gameplay_saves.py` (executed with Campus closed before installing probe)
- **Verified Output:**
  ```json
  {"backup": "D:\\SteamLibrary\\steamapps\\common\\Two Point Campus\\ThaiCampusMod\\local\\backups\\gameplay-save-snapshots\\20261021T150813553956Z.zip", "files": 6, "verified": true}
  ```
- **Adjacent Manifest Path:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261021T150813553956Z.json`

### Post-Run Save File Comparison Against `20261021T150813553956Z.json`
*(Live files and all snapshots retained untouched; numeric account folder ID redacted as `<AccountID>`)*

| Relative Path | Status | Pre-Run SHA-256 (Size) | Post-Run SHA-256 (Size) | Notes |
|---|---|---|---|---|
| `Cloud/<AccountID>/Saves/Slot1/8000.sav` | **NEW** | — | `5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d` (179,866 B) | Newly created `Freshleigh Meadows` campus save in `Slot1` |
| `Cloud/<AccountID>/Saves/Slot1/career.csav` | **CHANGED** | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) | `cbbded52fde65f46da0c874a403280936286b31746ea6f17b5b38d0acadafc0b` (18,521 B) | Updated `Slot1` career state after entering first campus |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.2.bak` | **CHANGED** | `0b1b806f610227302896505fc901e2dfbd2bee4ad3b97475f2800b9968e79f76` (10,048 B) | `f9730de46047fd6673d6ab5e408c0c5a3c71468b310809f4643fb341bd84219f` (18,521 B) | Rolling career backup updated by game |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.3.bak` | **NEW** | — | `dfd0601d068aa18807108560da1e16ad21da553a63e95cd4ea5b6bafbb1d5bba` (10,128 B) | Rolling career backup created by game |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.4.bak` | **NEW** | — | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) | Rolling career backup matching pre-run `career.csav` |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.5.bak` | **NEW** | — | `0b1b806f610227302896505fc901e2dfbd2bee4ad3b97475f2800b9968e79f76` (10,048 B) | Rolling career backup matching original `career.csav` |
| `Cloud/<AccountID>/userprofile.sav` | **CHANGED** | `818d0f2926750225f9764180718fe5a7882cb83079bdab7942eac282722f8862` (1,064 B) | `3cd23d0277804af12f246b63b3a5509961f95108f830a97b0ec0d596c4252423` (1,064 B) | Normal profile update on session exit |
| `Cloud/<AccountID>/preferences.json` | **UNCHANGED** | `b77254aacb67c47afc0dc8c63db13c4624408fa949a8ff4e87342311d7a3a9a8` (761 B) | `b77254aacb67c47afc0dc8c63db13c4624408fa949a8ff4e87342311d7a3a9a8` (761 B) | Unchanged |
| `Cloud/<AccountID>/steam_autocloud.vdf` | **UNCHANGED** | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) | `b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124` (52 B) | Unchanged |
| `localpreferences.json` | **UNCHANGED** | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) | `3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b` (1,050 B) | Unchanged |
| *(Missing files)* | **NONE** | — | — | 0 files missing |

---

## 5. Compact Three-Bundle Lifecycle & Restoration Output

All bundle commands were executed with `TPC.exe` confirmed closed. Original bundle backups are retained under `local/backups/community-merge-006/`.

```json
// 1. Pre-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. Install community-merge-006
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 3. Post-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4–5. Steam launch, Slot1 Campaign Map intro -> start Freshleigh Meadows -> capture initial modal -> normal exit (TPC.exe exited cleanly)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
