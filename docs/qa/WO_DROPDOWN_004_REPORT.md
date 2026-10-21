# WO-DROPDOWN-004 QA Report — Settings Caption Mitigation, Two Views (`community-merge-006`)

- **Date:** 2026-10-21
- **Candidate:** `community-merge-006` (Selected-caption `m_overflowMode` changed to `0` across 19 Settings dropdown controls: 12 from `1`, 7 from `3`; original Thai text, font/material/size/rect, and item list templates retained)
- **Verdict:** **`VISIBLE_CAPTIONS_CONTAINED`** *(limited to observed selected values in the two initial views)*
- **Primary Evidence:**
  - View 1 (`Settings > เกม` initial view): [01-settings-game.jpg](../../local/qa/WO-DROPDOWN-004/01-settings-game.jpg)
  - View 2 (`Settings > Video` initial view): [02-settings-video.jpg](../../local/qa/WO-DROPDOWN-004/02-settings-video.jpg)
- **Active Elapsed Time:** ~4 minutes (21:48–21:52 ICT; target cap: 10 minutes)
- **Capture Count:** 2 primary screenshots (1 per view), 0 recoveries (no scrolling, no dropdown opening/selection, no tooltips)

---

## 1. Environment, Capture Dimensions & Verified UI Scale

- **Game Build:** `10.3.169253+2024-12-06.1241`
- **Raw Runtime Capture (`ImageGrab.grab()`):** `3840 x 2160` (Full Screen Window / `หน้าต่างเต็มหน้าจอ`)
- **Saved Capture Dimensions & Resizing:** `1920 x 1080` JPEG, downsampled from `3840 x 2160` using `PIL.Image.Resampling.LANCZOS` in `tools/qa_driver.py`
- **UI Scale (`ขนาด UI`):** Directly observed in-screen as **`กลาง`** (`Medium`) in [01-settings-game.jpg](../../local/qa/WO-DROPDOWN-004/01-settings-game.jpg) (not modified).

---

## 2. Control Visibility & Containment Table

| View | Control Label (Thai / English) | Observed Selected Caption | Visibility Status | Containment & Arrow/Edge Clearance | Clipping / Missing Glyphs |
|---|---|---|---|---|---|
| **1 (`เกม`)** | `ระดับบันทึก` (`Log Level`) | `ข้อผิดพลาด` | **VISIBLE (Thai)** | Contained inside orange box; wide clearance from right arrow and row edges | None |
| **1 (`เกม`)** | `ความถี่การบันทึกอัตโนมัติของเกม` (`Game Autosave Frequency`) | `ทุกๆ เดือน` | **VISIBLE (Thai)** | Contained inside cyan box; wide clearance from right arrow and row edges | None |
| **1 (`เกม`)** | `ความถี่บันทึกอัตโนมัติโหมดอาชีพ` (`Career Autosave Frequency`) | `ทุกการเปลี่ยนแปลง` | **VISIBLE (Thai)** | Contained inside cyan box; clear margin before right arrow and row edges | None |
| **1 (`เกม`)** | `ภาษา` (`Language`) | `อังกฤษ` | **VISIBLE (Thai)** | Contained inside cyan box; wide clearance from right arrow and row edges | None |
| **1 (`เกม`)** | `ภาษาเสียงพากย์` (`Voice Language`) | `อังกฤษ` | **VISIBLE (Thai)** | Contained inside cyan box; wide clearance from right arrow and row edges | None |
| **1 (`เกม`)** | `ขนาด UI` (`UI Scale`) | `กลาง` | **VISIBLE (Thai)** | Contained inside cyan box; wide clearance from right arrow and row edges | None |
| **2 (`Video`)** | `โหมดเต็มหน้าจอ` (`Fullscreen Mode`) | `หน้าต่างเต็มหน้าจอ` | **VISIBLE (Thai)** | Contained inside orange box; clear margin before right arrow and row edges | None |
| **2 (`Video`)** | `ความละเอียด` (`Resolution`) | `3840 x 2160 @ 60hz` | **VISIBLE (ASCII)** | Contained inside cyan box; normal baseline appearance | None |
| **2 (`Video`)** | `VSync` (`VSync`) | `เปิด` | **VISIBLE (Thai)** | Contained inside cyan box; wide clearance from right arrow and row edges | None |
| **2 (`Video`)** | `โหมดการลบรอยหยัก` (`Antialiasing Mode`) | `SMAA` | **VISIBLE (ASCII)** | Contained inside cyan box; normal baseline appearance | None |
| **2 (`Video`)** | `คุณภาพการลบรอยหยัก` (`Antialiasing Quality`) & lower Video controls | — | **`NOT_OBSERVED`** | Below initial unscrolled viewport boundary (obscured by bottom bar `กลับสู่ค่าเริ่มต้น`) | N/A (`NOT_OBSERVED` per brief) |

---

## 3. Scope Limits

- **Observed Selected Values Only:** The `VISIBLE_CAPTIONS_CONTAINED` verdict applies strictly to the 8 Thai and 2 ASCII selected captions naturally visible in the initial unscrolled views of `Settings > เกม` and `Settings > Video`.
- **Unapproved Areas:** All 19 dropdown controls across all tabs/scroll positions, longer alternate option strings, opened dropdown item lists (`Template`), fine Thai vowel/tone shaping (which cannot be approved from downsampled captures), and gameplay remain unverified/unapproved.

---

## 4. Compact Lifecycle & Restoration Verification Output

All lifecycle commands were executed with `TPC.exe` confirmed closed. Original backups are retained under `local/backups/community-merge-006/`.

```json
// 1. Pre-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 2. Install community-merge-006
{"action": "install", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 3. Post-install check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "probe"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "probe"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "probe"}]}

// 4–5. Steam launch, 2 initial-view captures (Settings > Game, Settings > Video), normal Quit via Main Menu (TPC.exe exited cleanly)

// 6. Restore original bundles
{"action": "restore", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}

// 7. Final post-restore verification check
{"action": "check", "files": [{"name": "fonts_assets_all.bundle", "state": "original"}, {"name": "localisation_assets_localisationenglish.bundle", "state": "original"}, {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}]}
```
