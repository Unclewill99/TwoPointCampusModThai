# WO-SARA-AM-002-AB-R2 — Report (Atomic/Decomposed Text × Mark Pair, Natural Intro Wait)

- **Work Order:** `docs/qa/WO_SARA_AM_002_AB_R2.md` (revising `docs/qa/WO_SARA_AM_002_AB.md`, following `docs/SARA_AM_003_CONTROL_DISPOSITION.md`)
- **Date:** 2026-10-22
- **Agent:** Antigravity Desktop QA
- **Target Build:** Two Point Campus (`Build 10.3.169253+2024-12-06.1241`, Steam AppID `1649080`)
- **Parent Baseline:** `fresh-translation-005` (frozen)
- **Candidates Tested:** `probe-sara-am-001a` (control font) then `probe-sara-am-001b` (+1 TMP `MarkToMark` record `59 -> 42`)
- **Verdict:** `DIAGNOSTIC_RESULT` (`BUG-THAI-003` remains `OPEN` pending Controller analysis; no global fix or corpus rewrite claim)

---

## 1. Executive Summary & 2×3 Result Matrix

Both diagnostic variants (`probe-sara-am-001a` and `probe-sara-am-001b`) reached the opening `Freshleigh Meadows` course-information modal (`วันแรกของการเรียน`) after waiting naturally through the level load and opening camera flyover without any skip click or keypress.

The diagnostic lines (`A`, `B`, `C`) bound to `I2LS_Levels` segment `533` rendered directly inside the top blue description box of the opening modal. Comparing the exact modal specimen region (`x = 1780..2020, y = 810..1025`) between `01-modal-probe-sara-am-001a.png` and `02-modal-probe-sara-am-001b.png` shows:
- **Row A (`0` pixels changed):** Atomic `ต่ำ` (`U+0E15 U+0E48 U+0E33`) has `mai-ek` and the `nikkhahit` circle of `U+0E33` colliding at the same vertical band (`y = 839..847`, `0 px` separation) in **both** `001a` and `001b`.
- **Row B (`74` pixels changed):** Reordered decomposed `ตํ่า` (`U+0E15 U+0E4D U+0E48 U+0E32`) collides in `001a` (`y = 904..911`, `0 px` separation), but in `001b` (with the added `MarkToMark` pair `glyph 59 -> glyph 42`), `mai-ek` (`y = 895..900`) is lifted cleanly above `nikkhahit` (`y = 906..911`) with a **`5 px` clear vertical gap (`y = 901..905`)**, aligning horizontally with the `mai-ek` and `sara ii` bands of the adjacent `ถี่` control.
- **Row C (`0` pixels changed):** Original-order decomposed `ต่ํา` (`U+0E15 U+0E48 U+0E4D U+0E32`) stacks in inverted vertical order (`nikkhahit` at `y = 964..970` on top of `mai-ek` at `y = 975..981`, `4 px` gap) in **both** `001a` and `001b`.
- **Control `ถี่` (`0` pixels changed across all 3 rows):** Cleanly separated (`5 px` vertical gap between `sara ii` and `mai-ek`) in all rows of both `001a` and `001b`.

### 2×3 Diagnostic Matrix & Control Summary

| Row | Specimen & Target Codepoints | `probe-sara-am-001a` (Unchanged `005` Font) | `probe-sara-am-001b` (+1 `MarkToMark` `59 -> 42`) | Cross-Variant Diff (`a` vs `b`) | Comparison vs. Offline Same-Font Reference (`WO-SARA-AM-001-REFERENCE`) |
|---|---|---|---|---|---|
| **A** | `A: ต่ำ ถี่`<br>Target: `0E15 0E48 0E33` (atomic `ต่ำ`) | **COLLISION / OVERLAP:** `mai-ek` and `nikkhahit` ring of `0E33` overlap in single band `y = 839..847` (`0 px` gap) above base `ต` (`y = 850..870`). No tofu/clipping. | **COLLISION / OVERLAP (Unchanged):** Identical single band `y = 839..847` (`0 px` gap). Adding `MarkToMark` `59 -> 42` has no effect on atomic `0E15 0E48 0E33`. | `0 px` changed in Row A | Reference (`#1 atomic_sara_am` in Edge/HarfBuzz) decomposes `0E33` and separates `mai-ek` above `nikkhahit` (`5 px` gap at 48px); in-game TMP does not separate atomic `0E15 0E48 0E33`. |
| **B** | `B: ตํ่า ถี่`<br>Target: `0E15 0E4D 0E48 0E32` (reordered decomposed) | **COLLISION / OVERLAP:** `nikkhahit` (`0E4D`) and `mai-ek` (`0E48`) overlap in single band `y = 904..911` (`0 px` gap) above base `ต` (`y = 915..935`). | **CLEAN VERTICAL SEPARATION:** `nikkhahit` (`glyph 59`) renders at `y = 906..911` (hollow ring) and `mai-ek` (`glyph 42`) renders above it at `y = 895..900` with a **`5 px` clear vertical gap** (`y = 901..905`). No overlap, tofu, or clipping. | **`74 px` changed** (`x = 1897..1902`, `y = 894..911`) | Matches the vertical mark order and clean separation of offline reference `#2 reordered_decomposed` (`ต` base -> `nikkhahit` -> `mai-ek` on top). |
| **C** | `C: ต่ํา ถี่`<br>Target: `0E15 0E48 0E4D 0E32` (original-order decomposed) | **INVERTED STACKING:** `mai-ek` (`0E48`) sits in lower mark band `y = 975..981` while `nikkhahit` (`0E4D`) stacks above `mai-ek` at `y = 964..970` (`4 px` gap `y = 971..974`). | **INVERTED STACKING (Unchanged):** Identical (`mai-ek` at `y = 975..981`, `nikkhahit` on top at `y = 964..970`, `4 px` gap). | `0 px` changed in Row C | Matches the inverted vertical stacking order (`nikkhahit` above `mai-ek`) seen in offline reference `#3 original_order_decomposed`. |
| **Control (`ถี่`)** | `ถี่` (`0E16 0E35 0E48`) in Rows A, B, C | **CLEAN SEPARATION** in all 3 rows (`5 px` vertical gap between `sara ii` and `mai-ek`: Row A `y=836..840`, Row B `y=901..905`, Row C `y=972..976`). | **CLEAN SEPARATION (Unchanged)** in all 3 rows (`0 px` diff vs `001a`; `5 px` vertical gap preserved). | `0 px` changed in any `ถี่` control | Matches clean separation of offline reference `#4 control_thi`. |

> **Diagnostic Interpretation (per WO Section "Report and interpretation"):**
> Because only decomposed Row B (`U+0E15 U+0E4D U+0E48 U+0E32`) improves when adding the `MarkToMark` pair (`glyph 59 -> glyph 42`), this supports placement-table (`m_MarkToMarkAdjustmentRecordLookup`) contribution for the reordered decomposed sequence (`U+0E4D U+0E48`), **not** an atomic `ต่ำ` (`U+0E15 U+0E48 U+0E33`) fix and **not** permission to rewrite the production corpus. `BUG-THAI-003` remains `OPEN` pending Controller analysis.

---

## 2. Candidate Manifest Hashes & Verification

| Bundle File | Original SHA-256 | `probe-sara-am-001a` SHA-256 | `probe-sara-am-001b` SHA-256 |
|---|---|---|---|
| `fonts_assets_all.bundle` | `33aa34892719fbc7caaabd0a292c32bb135bc61978a4cd3ce73c6c40da8f4e6e` | `588f15fad01635da3fb5b86d5c3946cbb7bd85b40304364294fb23d73c207f3e` | `6cb840337007c4fb7d6807828276ddef1ae51c2b7809e507f90a53b7c243b133` |
| `localisation_assets_localisationenglish.bundle` | `c1e7ca97f260813ccc9a1cf463f20d066631f8e5616bf797fe8d5ae93227878f` | `02a6d2864ea5fcef910e01644b224da2859df3aa58d54b25ed09e83a40727bf4` | `02a6d2864ea5fcef910e01644b224da2859df3aa58d54b25ed09e83a40727bf4` |
| `ui-prefabs-general_assets_all.bundle` | `2152e5ba289ccb0414c462371cfdfe05cc7ac589a10a75b8b46d359afd99786d` | `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df` | `34c9779682b146bbab82569789622b978f807ff0efeca00317694543713d59df` |

- Both `local/prototype/probe-sara-am-001a/manifest.json` and `local/prototype/probe-sara-am-001b/manifest.json` match `reports/sara-am-001-build.json`, and live bundle SHA-256 hashes were verified after each `install` and `restore`.

---

## 3. Driver Contract, Subprocess Ordering, Geometry & Timing

- **Driver Used:** `tools/qa_driver.py`
  - **SHA-256:** `6e243c022dfb80e5e13431dbadba917415c475daeb78e74994c05f282dfff78d`
  - **Functions Used:** `qa_driver.set_desktop()`, `qa_driver.find_tpc_window()`, `qa_driver.require_game_foreground()`, `qa_driver.activate_tpc()`, `qa_driver.move_mouse()`, `qa_driver.click()`, `qa_driver.send_mouse_event()`.
- **Subprocess Call Ordering:**
  - In every fresh Python subprocess, `qa_driver.set_desktop()` was called **first**, before `find_tpc_window()`, `u.GetForegroundWindow()`, `require_game_foreground()`, `GetCursorPos()`, `ImageGrab.grab()`, or any input call.
- **Display & Capture Geometry:**
  - Primary Display (`GetSystemMetrics(0) x GetSystemMetrics(1)`): `3840 x 2160`, origin `(0, 0)`.
  - Game Window `GetWindowRect`: `(0, 0, 3840, 2160)` (`3840 x 2160`).
  - UI Scale in `preferences.json` / `localpreferences.json`: default untouched (not modified).
  - Native-to-Normalized Coordinate Formula (floating point retained until `qa_driver.to_phys` rounding):
    $$\text{norm\_x} = \frac{\text{native\_x} \times 1920.0}{3840.0}, \quad \text{norm\_y} = \frac{\text{native\_y} \times 1080.0}{2160.0}$$
- **Focus Recovery & Guard Summary:**
  - Total focus recoveries used across both variants: **`1 / 1`**.
  - During `probe-sara-am-001a`: `0` recoveries needed (`fg == hwnd` on all checks).
  - During `probe-sara-am-001b`: Prior to clicking Campaign Card `ต่อไป`, `require_game_foreground()` caught `fg = 66072 != hwnd (2166076)` and blocked input (`RuntimeError: Foreground is not the verified TPC.exe window; no input sent`). Used the `1 / 1` permitted recovery (`qa_driver.activate_tpc()`), waited `1.5s`, captured a fresh Campaign Card observation (`b_card_recovered.png`), re-derived the button target from fresh pixels, verified hover, and clicked once.
- **Total Active Run Time:** `~11 minutes` across both variants (within the 15-minute budget).

### Navigation, Input Return Counts & Modal Timing Per Variant

| Step / Metric | `probe-sara-am-001a` | `probe-sara-am-001b` |
|---|---|---|
| **Process & Window** | `pid = 35788`, `hwnd = 1248532`, `TPC.exe` verified | `pid = 25912`, `hwnd = 2166076`, `TPC.exe` verified |
| **Main Menu `ต่อไป` (`Continue`) Box** | Native `(172, 794, 928, 866)`, center `(550.0, 830.0)` -> norm `(275.0, 415.0)` | Native `(172, 794, 928, 866)`, center `(550.0, 830.0)` -> norm `(275.0, 415.0)` |
| **Main Menu Hover & Click `SendInput` Counts** | `GetCursorPos = (550, 830)`, `SendInput` counts: `[1]` (hover move), `[1, 1, 1, 1]` (after click: move + down + up) | `GetCursorPos = (550, 830)`, `SendInput` counts: `[1]` (hover move), `[1, 1, 1, 1]` (after click: move + down + up) |
| **Campaign Card `ต่อไป` (`Continue`) Box** | Native `(223, 1634, 666, 1776)`, center `(444.5, 1705.0)` -> norm `(222.25, 852.5)` | Fresh post-recovery native `(222, 1634, 666, 1776)`, center `(444.0, 1705.0)` -> norm `(222.0, 852.5)` |
| **Campaign Card Hover Verification** | `GetCursorPos = (444, 1705)`, pixel `(260, 1705)` brightened `(63, 168, 66) -> (101, 201, 101)` | `GetCursorPos = (444, 1705)`, pixel `(260, 1705)` brightened `(63, 168, 66) -> (101, 201, 101)` |
| **Campaign Card Click `SendInput` Counts** | `SendInput` counts: `[1]` (hover move), `[1, 1, 1, 1]` (after click) | `SendInput` counts: `[1]` (hover move), `[1, 1, 1, 1]` (after click) |
| **Measured Modal Appearance Elapsed Time** | Modal first observed at **`t = 50.77s`** (`center_bright_ratio` rose from `0.004` at `45.69s` to `0.258` at `50.77s`; final PNG saved at `t = 61.02s`) | Modal first observed at **`t = 50.86s`** (`center_bright_ratio` rose from `0.004` at `45.76s` to `0.258` at `50.86s`; final PNG saved immediately at `t = 51.96s`) |
| **Retained Primary Evidence PNG** | `local/qa/WO-SARA-AM-002-AB-R2/01-modal-probe-sara-am-001a.png` (`3840 x 2160`, `7,103,010` bytes, SHA-256 `83d7fb278ccfc99e069a00da0ec8020bce93b3544c2449488dfe292181fd3d33`) | `local/qa/WO-SARA-AM-002-AB-R2/02-modal-probe-sara-am-001b.png` (`3840 x 2160`, `7,102,440` bytes, SHA-256 `de6285777a0917e051ad88c5777f2b7b6ab6bc3d8696bf396a03af7ea6e3948d`) |

---

## 4. Per-Variant Bundle & Save Lifecycle Log

### 4.1 Variant A (`probe-sara-am-001a`) Lifecycle
1. **Pre-Install Check (`TPC.exe` closed):**
   `python tools/manage_probe.py check --probe probe-sara-am-001a` -> `original / original / original`.
2. **Pre-Install Save Backup:**
   `python tools/backup_gameplay_saves.py` -> `local/backups/gameplay-save-snapshots/20261022T155048899070Z.zip` (`files: 11, verified: true`), manifest `20261022T155048899070Z.json`.
3. **Install:**
   `python tools/manage_probe.py install --probe probe-sara-am-001a` -> `probe / probe / probe`.
4. **Post-Install Check & Hash Verification:**
   `python tools/manage_probe.py check --probe probe-sara-am-001a` -> `probe / probe / probe` (all 3 live SHA-256 hashes verified against `local/prototype/probe-sara-am-001a/manifest.json`).
5. **Run & Normal Exit:**
   Captured `01-modal-probe-sara-am-001a.png` without dismissing modal; closed via `PostMessageW(1248532, WM_CLOSE, 0, 0)`; confirmed `find_tpc_window() == []`.
6. **Restore:**
   `python tools/manage_probe.py restore --probe probe-sara-am-001a` -> `original / original / original`.
7. **Post-Restore Check:**
   `python tools/manage_probe.py check --probe probe-sara-am-001a` -> `original / original / original`.
8. **Save Hash Comparison (vs. `20261022T155048899070Z.json`):**
   - **Unchanged (4 files, including `Slot1/8000.sav`):**
     - `Cloud/210252614/Saves/Slot1/8000.sav` (`5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d`)
     - `Cloud/210252614/preferences.json` (`f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e`)
     - `Cloud/210252614/steam_autocloud.vdf` (`b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124`)
     - `localpreferences.json` (`3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b`)
   - **Changed (7 files — routine `career.csav` backup chain rotation & `userprofile.sav`):**
     - `Cloud/210252614/Saves/Slot1/career.csav`: `5067a7b0...` -> `8069d679fe7c50fec9f54e14f319d103b017ae5c05513264086772630e96d129`
     - `Cloud/210252614/Saves/Slot1/career.csav.2.bak`: `26339e1c...` -> `2af271e97ad2053f229b97f9a864883ebe1087f942075826e9a463e96a771781`
     - `Cloud/210252614/Saves/Slot1/career.csav.3.bak`: `072f2ac9...` -> `5067a7b0ef3ffde5f603e894108a985227a06275ef50d0e242b832030809c3a8`
     - `Cloud/210252614/Saves/Slot1/career.csav.4.bak`: `d61a300f...` -> `26339e1c0dee45e54ee5bbb88c85e493b00c43fb09d2a057a6567f5cb92ce60d`
     - `Cloud/210252614/Saves/Slot1/career.csav.5.bak`: `c51ca1bc...` -> `072f2ac9449f60467140e5e08576e85d14c253afefd60cfdccf68b8f371fa16d`
     - `Cloud/210252614/Saves/Slot1/career.csav.6.bak`: `27fd1082...` -> `d61a300fd9156feec475b10ba9fb65a34163bcc507f49c12afe7ca124c37dd00`
     - `Cloud/210252614/userprofile.sav`: `ba5d458d...` -> `9a09419e361d0067d7de73efa6b7557de29d883049c3ea7e5a2a7dfa8adfd256`
   - **New / Missing Files:** `0 new`, `0 missing`.

---

### 4.2 Variant B (`probe-sara-am-001b`) Lifecycle
1. **Pre-Install Check (`TPC.exe` closed):**
   `python tools/manage_probe.py check --probe probe-sara-am-001b` -> `original / original / original`.
2. **Pre-Install Save Backup:**
   `python tools/backup_gameplay_saves.py` -> `local/backups/gameplay-save-snapshots/20261022T155759988590Z.zip` (`files: 11, verified: true`), manifest `20261022T155759988590Z.json`.
3. **Install:**
   `python tools/manage_probe.py install --probe probe-sara-am-001b` -> `probe / probe / probe`.
4. **Post-Install Check & Hash Verification:**
   `python tools/manage_probe.py check --probe probe-sara-am-001b` -> `probe / probe / probe` (all 3 live SHA-256 hashes verified against `local/prototype/probe-sara-am-001b/manifest.json`).
5. **Run & Normal Exit:**
   Captured `02-modal-probe-sara-am-001b.png` without dismissing modal; closed via `PostMessageW(2166076, WM_CLOSE, 0, 0)`; confirmed `find_tpc_window() == []`.
6. **Restore:**
   `python tools/manage_probe.py restore --probe probe-sara-am-001b` -> `original / original / original`.
7. **Post-Restore Check:**
   `python tools/manage_probe.py check --probe probe-sara-am-001b` -> `original / original / original`.
8. **Save Hash Comparison (vs. `20261022T155759988590Z.json`):**
   - **Unchanged (4 files, including `Slot1/8000.sav`):**
     - `Cloud/210252614/Saves/Slot1/8000.sav` (`5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d`)
     - `Cloud/210252614/preferences.json` (`f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e`)
     - `Cloud/210252614/steam_autocloud.vdf` (`b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124`)
     - `localpreferences.json` (`3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b`)
   - **Changed (7 files — routine `career.csav` backup chain rotation & `userprofile.sav`):**
     - `Cloud/210252614/Saves/Slot1/career.csav`: `8069d679...` -> `7cbd47721b20b8cef98ba4c892d9c009a256f8d1f82308b1cb5d0e2f583d6c28`
     - `Cloud/210252614/Saves/Slot1/career.csav.2.bak`: `2af271e9...` -> `24e093ef8510486564363f197834b00a00a79afc67b3246eaf45cf4139bdb71c`
     - `Cloud/210252614/Saves/Slot1/career.csav.3.bak`: `5067a7b0...` -> `8069d679fe7c50fec9f54e14f319d103b017ae5c05513264086772630e96d129`
     - `Cloud/210252614/Saves/Slot1/career.csav.4.bak`: `26339e1c...` -> `2af271e97ad2053f229b97f9a864883ebe1087f942075826e9a463e96a771781`
     - `Cloud/210252614/Saves/Slot1/career.csav.5.bak`: `072f2ac9...` -> `5067a7b0ef3ffde5f603e894108a985227a06275ef50d0e242b832030809c3a8`
     - `Cloud/210252614/Saves/Slot1/career.csav.6.bak`: `d61a300f...` -> `26339e1c0dee45e54ee5bbb88c85e493b00c43fb09d2a057a6567f5cb92ce60d`
     - `Cloud/210252614/userprofile.sav`: `9a09419e...` -> `063746abc25c97fc0e73bc874fc12d6e7accb8a152528445d6640de31d292e7f`
   - **New / Missing Files:** `0 new`, `0 missing`.
   - All live saves and both pre-variant backup ZIPs/manifests are retained untouched.
