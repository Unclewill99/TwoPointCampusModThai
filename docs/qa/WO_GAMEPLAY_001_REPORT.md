# WO-GAMEPLAY-001 QA Report — Practical Merged-Mod Trial, Existing Career (`community-merge-006`)

- **Date:** 2026-10-21
- **Candidate:** `community-merge-006`
- **Verdict:** **`SETUP_LIMIT`** *(Campaign Map intro in `Slot1` rendered readable Thai with zero technical defects; no resumable campus save exists in `Slot1`, so Views 2 and 3 remain `NOT_RUN` per brief)*
- **Primary Evidence:** [01-career-view.jpg](../../local/qa/WO-GAMEPLAY-001/01-career-view.jpg)
- **Active Elapsed Time:** ~4 minutes (21:58–22:02 ICT; target budget: 15 minutes)
- **Capture Count:** 1 primary screenshot, 0 recoveries (Views 2 and 3 `NOT_RUN`)

---

## 1. Environment, Selected Career/Campus & Capture Dimensions

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Raw Runtime Capture (`ImageGrab.grab()`):** `3840 x 2160` (Full Screen Window; settings and `Medium` UI scale left unchanged)
- **Saved Capture Dimensions & Resizing:** `1920 x 1080` JPEG, downsampled from `3840 x 2160` using `PIL.Image.Resampling.LANCZOS` in `tools/qa_driver.py`
- **Selected Career:** Existing `Slot1` (`Two Point` career, 0 Stars / 0 Career Goals / 0 Kudosh), entered via the Main Menu `ดำเนินการต่อ` (`Continue`) button.
- **Selected / Resumable Campus:** **None available.** `Slot1` opens at the initial Campaign Map advisor introduction with the first campus pin (`Freshleigh Meadows`) unstarted at `0/3` stars (matching the absence of any separate campus `.csav` file in `Slot1`). Per brief rules (*"Do not start a new campus, spend money, build, hire, dismiss a tutorial, or advance academic time deliberately. If no resumable campus is offered, end at map; lack of an available save is a setup limit, not a translation failure"*), observation stopped at the Campaign Map without clicking `ถัดไป` (`Next`) or starting a new campus.
- **Pause State Established:** **Not applicable / Not established** (Session ended at the Campaign Map before any campus gameplay clock existed).

---

## 2. Three-View Screening Table

| View # | Target View | Primary Evidence | Captures (Primary + Recovery) | Status | Summary of Observations |
|:---:|---|---|:---:|---|---|
| **1** | **Continue Existing `Slot1` Career (Campaign Map / First Meaningful Career View)** | [01-career-view.jpg](../../local/qa/WO-GAMEPLAY-001/01-career-view.jpg) | 1 + 0 | **OBSERVED (`PASS` in view; `SETUP_LIMIT` for campus continuation)** | Entered `Slot1` Campaign Map. Advisor Albert Crank dialogue panel is visible (`ยินดีต้อนรับสู่ Two Point เค้าตี้`, `ฉัน อัลเบิร์ต แครงค์ ที่ปรึกษาส่วนตัวของคุณเอง`, `และฉันมาที่นี่เพื่อช่วยเหลือ`, button `ถัดไป`). All visible Thai strings are readable, contained, and free of missing glyphs, blank fields, or raw tags. Map shows only an unstarted 0-star campus pin. |
| **2** | **Resume Existing Campus & Pause (Initial Campus HUD / Objective)** | — | 0 + 0 | **`NOT_RUN`** *(Setup Limit)* | No existing resumable campus is present in `Slot1`, and dismissing the intro tutorial or starting a new campus is prohibited by the brief. |
| **3** | **Paused Read-Only Overview Panel** | — | 0 + 0 | **`NOT_RUN`** *(Setup Limit)* | Dependent on View 2 resumable campus. |

*Scope Disclaimer:* Map-only observation cannot approve campus gameplay. Fine vowel/tone shaping and exhaustive corpus accuracy remain unverified.

---

## 3. Visible Technical Failures & Language Observations (View 1)

### Visible Technical Failures
- **None observed in [01-career-view.jpg](../../local/qa/WO-GAMEPLAY-001/01-career-view.jpg):** Zero missing-glyph boxes, zero blank expected text fields, zero raw placeholders/tags, and no text clipping on the advisor dialogue heading, body, or `ถัดไป` button.

### Representative Language / Translation Observations (Key IDs Uncertain from Runtime View)
1. **Mixed English + Non-Standard Transliteration in Header (`ยินดีต้อนรับสู่ Two Point เค้าตี้` — View 1 Campaign Map Advisor Header, key uncertain):**
   - Retains `Two Point` in English while transliterating `County` as `เค้าตี้` (spelled with `ไม้โท` instead of standard `เคาน์ตี` / `เคาน์ตี้`).
2. **Literal Pronoun & Appositive Phrasing (`ฉัน อัลเบิร์ต แครงค์ ที่ปรึกษาส่วนตัวของคุณเอง` — View 1 Campaign Map Advisor Body, line 1, key uncertain):**
   - Uses first-person pronoun `ฉัน` without a linking verb (`คือ` / `ชื่อ`) for advisor Albert Crank, and translates `"your personal advisor"` literally with `ของคุณเอง`.
3. **Literal Clause Continuation (`และฉันมาที่นี่เพื่อช่วยเหลือ` — View 1 Campaign Map Advisor Body, line 2, key uncertain):**
   - Translates `"and I'm here to help"` word-for-word as `และฉันมาที่นี่เพื่อช่วยเหลือ`, which is understandable but slightly abrupt without a trailing object (`คุณ`).

---

## 4. Save Backup & Post-Run Save File Hash Summary

### Fresh Pre-Run Save Snapshot
- **Command:** `python tools/backup_gameplay_saves.py` (executed with Campus closed before installing probe)
- **Verified Output:**
  ```json
  {"backup": "D:\\SteamLibrary\\steamapps\\common\\Two Point Campus\\ThaiCampusMod\\local\\backups\\gameplay-save-snapshots\\20261021T145837044362Z.zip", "files": 5, "verified": true}
  ```
- **Adjacent Manifest Path:** `D:\SteamLibrary\steamapps\common\Two Point Campus\ThaiCampusMod\local\backups\gameplay-save-snapshots\20261021T145837044362Z.json`

### Post-Run Save File Comparison Against `20261021T145837044362Z.json`
*(Both live files and the pre-run snapshot are retained untouched; numeric account folder ID redacted as `<AccountID>`)*

| Relative Path | Status | Pre-Run SHA-256 (Size) | Post-Run SHA-256 (Size) | Notes |
|---|---|---|---|---|
| `Cloud/<AccountID>/Saves/Slot1/career.csav` | **CHANGED** | `0b1b806f610227302896505fc901e2dfbd2bee4ad3b97475f2800b9968e79f76` (10,048 B) | `91998459ebcd62690c4cd54ef4d9ed16b9e0f379360c791a5709c4d1ee1f8e7c` (10,128 B) | Updated automatically by game upon loading/exiting `Slot1` |
| `Cloud/<AccountID>/Saves/Slot1/career.csav.2.bak` | **NEW** | — | `0b1b806f610227302896505fc901e2dfbd2bee4ad3b97475f2800b9968e79f76` (10,048 B) | Game's automatic backup of the exact pre-run `career.csav` |
| `Cloud/<AccountID>/userprofile.sav` | **CHANGED** | `fef866bef63824284eb97024958ddf7bb394b9989e02aef6731422bbec1ba5c1` (1,064 B) | `818d0f2926750225f9764180718fe5a7882cb83079bdab7942eac282722f8862` (1,064 B) | Normal profile update on session exit |
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

// 4–5. Steam launch, Continue Slot1 career to Campaign Map intro, normal window exit via WM_CLOSE (TPC.exe exited cleanly)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
