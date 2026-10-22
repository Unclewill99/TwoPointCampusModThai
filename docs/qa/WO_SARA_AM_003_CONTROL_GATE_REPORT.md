# WO-SARA-AM-003-CONTROL-GATE — Report (Originals Only)

- **Work Order:** `docs/qa/WO_SARA_AM_003_CONTROL_GATE.md` (superseding automatic retry of `WO_SARA_AM_002_AB.md`, per `docs/SARA_AM_002_AB_DISPOSITION.md`)
- **Date:** 2026-10-22
- **Agent:** Antigravity Desktop QA
- **Target Build:** Two Point Campus (`Build 10.3.169253+2024-12-06.1241`, Steam AppID `1649080`)
- **Game Bundle State:** All 3 bundles verified `original` before and after run (no A/B candidate installed)
- **Verdict:** `SETUP_LIMIT` (Campaign Card `Continue` click succeeded with `SendInput` `1/1` and entered `Freshleigh Meadows`, but the WO's 30-second bounded post-click wait expired during the final subtitle of the opening camera flyover cutscene `~5–8s` before the `First Day of School` modal appears)

---

## 1. Driver Version & Input Contract Verification

- **Driver Script:** `tools/qa_driver.py`
  - **SHA-256:** `6e243c022dfb80e5e13431dbadba917415c475daeb78e74994c05f282dfff78d`
- **Coordinate Contract:**
  - `qa_driver.py` maps normalized `(x, y)` on a `1920 x 1080` reference grid across the full primary display (`GetSystemMetrics(0)=3840`, `GetSystemMetrics(1)=2160`) to `MOUSEEVENTF_ABSOLUTE` (`0..65535`).
  - Explicit native-to-normalized conversion on this `3840 x 2160` display (`origin = (0, 0)`):
    $$\text{norm\_x} = \left\lfloor \frac{\text{native\_x}}{2} \right\rfloor, \quad \text{norm\_y} = \left\lfloor \frac{\text{native\_y}}{2} \right\rfloor$$
- **SendInput Return-Count Guard:**
  - `_send_mouse_event()` checks `sent = u.SendInput(1, ctypes.byref(inp), ctypes.sizeof(INPUT))` and raises `RuntimeError` if `sent != 1`.
- **Root Cause Identified for Previous Subprocess `GetForegroundWindow() == None` (`0`) Reports:**
  - In fresh Python subprocesses invoked via `run_command`, calling `user32.GetForegroundWindow()` **before** `qa_driver.set_desktop()` returns `None` (`0`) because the thread has not yet attached to the `Default` interactive desktop (`OpenInputDesktop` / `SetThreadDesktop`).
  - Calling `qa_driver.set_desktop()` first immediately resolves `u.GetForegroundWindow() == 658710` (`TPC.exe`) without needing `SetForegroundWindow`.

---

## 2. Pre-Run Bundle & Save Snapshot Checks

### 2.1 Pre-Run Bundle Check (`TPC.exe` Closed)
Command: `python tools/manage_probe.py check --probe probe-sara-am-001a`
```json
{
  "action": "check",
  "files": [
    {"name": "fonts_assets_all.bundle", "state": "original"},
    {"name": "localisation_assets_localisationenglish.bundle", "state": "original"},
    {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}
  ]
}
```

### 2.2 Pre-Run Gameplay Save Backup
Command: `python tools/backup_gameplay_saves.py`
- **Backup ZIP:** `local/backups/gameplay-save-snapshots/20261022T154008228446Z.zip` (`verified: true`, 11 files)
- **Adjacent Manifest:** `local/backups/gameplay-save-snapshots/20261022T154008228446Z.json`

---

## 3. Process, Window, Focus & Navigation Evidence

### 3.1 Process & Window Identity
- **Launch Method:** `Start-Process 'steam://rungameid/1649080'`
- **Verified Process Owner:** `pid = 34812`, `exe = D:\SteamLibrary\steamapps\common\Two Point Campus\TPC.exe`
- **Unique Game Window:** `hwnd = 658710`, `title = 'Two Point Campus'`
- **Window & Display Geometry:**
  - `GetWindowRect(658710) = (0, 0, 3840, 2160)` (`3840 x 2160`, origin `(0, 0)`)
  - Primary Display Metrics: `3840 x 2160`
- **Focus Recovery Count Used:** `1 / 1` (used prior to the Main Menu `Continue` click when `GetForegroundWindow()` was queried before `set_desktop()`; zero additional focus recoveries were used for the rest of the run).

### 3.2 Step 1 — Main Menu Observation & `Continue` Click (`01-main-menu.png`)
- **Retained Evidence 1:** `local/qa/WO-SARA-AM-003-CONTROL-GATE/01-main-menu.png`
  - **Dimensions:** `3840 x 2160` PNG (`4,658,835` bytes, SHA-256 `a0484a13db7ff2ccf5c45c6c1b1110f3bfc7370f5032a3c1d7858bd7bea8dc83`)
  - **Full-Screen Interpretation:** Original English Main Menu (`Build 10.3.169253+2024-12-06.1241` bottom-right). Left menu card under `Two Point` header displays visible English buttons: `Continue`, `Load Game`, `New Game`, `Sandbox`, `Settings`, `Mods`, `Quit`.
- **Target Button Measurement (`Continue`):**
  - Native bounding box: `x = 171..928, y = 793..882` (width `758 px`, height `90 px`)
  - Native center: `(549, 837)`
  - Normalized `qa_driver` target: `(274, 418)`
- **Input Execution & Return Count Evidence:**
  - Pre-click `move_mouse(274, 418)` -> `GetCursorPos()` confirmed `(548, 836)` inside the `Continue` button box.
  - Executed single `click(274, 418)` -> no exception raised; `SendInput` return-count guard accepted `1/1` for all events (`MOVE`, `LEFTDOWN`, `LEFTUP`).
  - Game transitioned immediately into the Campaign Map loading screen and opened the `FRESHLEIGH MEADOWS` campaign card within `10.0s`.

### 3.3 Step 2 — Campaign Card Observation, Hover Verification & `Continue` Click (`02-campaign-card.png`)
- **Retained Evidence 2:** `local/qa/WO-SARA-AM-003-CONTROL-GATE/02-campaign-card.png`
  - **Dimensions:** `3840 x 2160` PNG (`4,096,218` bytes, SHA-256 `15516e383f00794971e9bf8b0392107fd5e4f10e663551e54d9e1c326d8184bb`)
  - **Full-Screen Interpretation:** Campaign Map showing the `FRESHLEIGH MEADOWS` card on the left with `LAST SAVED 10/21/2026 10:15 PM`, `Year 1 AUG`, `$500,000`, `Campus Level 1`, a green `Continue` button on the bottom-left of the card, and a red `Restart` button on the bottom-right of the card.
- **Target Button Measurement (Campaign Card Green `Continue` Button):**
  - Native bounding box: `x = 227..666, y = 1634..1766` (width `440 px`, height `133 px`)
  - Native center: `(446, 1700)`
  - Normalized `qa_driver` target: `(223, 850)`
- **Foreground & Hover Confirmation Before Click:**
  - After `qa_driver.set_desktop()`, `u.GetForegroundWindow()` returned `658710` (`fg == hwnd: True`, 0 recoveries needed).
  - Pre-hover pixel on green button face `(260, 1700)` was `RGB (63, 168, 66)`.
  - Moved cursor via `SendInput` to normalized `(223, 850)` (`SendInput[MOVE_PRE_HOVER] returned: 1/1`):
    - `GetCursorPos()` confirmed native cursor at `(446, 1700)` (exact center of green `Continue` button).
    - Post-hover pixel at `(260, 1700)` brightened to `RGB (101, 201, 101)`, proving the game window actively received cursor hover over the `Continue` button.
- **Single Click Execution & `SendInput` Return Evidence:**
  - Executed exactly 1 click at normalized `(223, 850)` with explicit per-event return logging:
    - `SendInput[MOVE] returned: 1/1`
    - `SendInput[LEFTDOWN] returned: 1/1`
    - `SendInput[LEFTUP] returned: 1/1`
  - Post-click `GetCursorPos()` remained `(446, 1700)`.

### 3.4 Step 3 — Bounded 30-Second Wait & Resulting Screen (`03-result-screen.png`)
- **Post-Click Progression During the 30-Second Bounded Wait (`t = 0s .. 31.3s`):**
  - `t = 2.0s .. 12.5s`: The Campaign Card closed immediately after the single click and displayed the `Freshleigh Meadows` level loading screen (`top-left RGB (56, 168, 188)`).
  - `t = 14.6s .. 31.3s`: The `Freshleigh Meadows` 3D campus finished loading and played the opening guided camera flyover cutscene across the campus grounds with voiceover and bottom subtitles.
- **Retained Evidence 3:** `local/qa/WO-SARA-AM-003-CONTROL-GATE/03-result-screen.png`
  - **Dimensions:** `3840 x 2160` PNG (`12,687,410` bytes, SHA-256 `cac75dad048467d05cb26d79bade95a280fa28578e346652e75383dfe2462d01`)
  - **Full-Screen Interpretation:** Captured at the end of the 30-second bounded wait (`t = 31.3s` after clicking Campaign Card `Continue`). The full screen shows the live 3D `Freshleigh Meadows` campus exterior during the final subtitle line of the opening camera flyover:
    > *"long ago, by dignified people who wore bowler hats and spoke via subtitle. The world is a creation of the past, and it is our job to keep it all going and try not to touch anything."*
  - **Why the Opening Modal Was Not Yet Visible at `t = 30s`:**
    - Clicking `Continue` on the `Slot1` `Freshleigh Meadows` save (which was saved at the very start of the level before dismissing the initial modal) replays the `~12.5s` level load plus the `~24–28s` opening camera flyover (`~37–40s` total) before the `First Day of School` (`Scientography`) modal pops up.
    - Therefore, the Campaign Card `Continue` click **succeeded completely**, and a post-click wait of **45–50 seconds** (instead of 30 seconds) is sufficient for the camera flyover to finish and display the opening modal automatically without any extra clicks.

---

## 4. Normal Exit, Post-Run Bundle Check & Save Hash Comparison

### 4.1 Normal Exit
- Closed `TPC.exe` cleanly via `PostMessageW(658710, WM_CLOSE, 0, 0)`.
- Confirmed `TPC.exe` exited within 5 seconds (`find_game_windows() == []`).

### 4.2 Post-Run Bundle Check
Command: `python tools/manage_probe.py check --probe probe-sara-am-001a`
```json
{
  "action": "check",
  "files": [
    {"name": "fonts_assets_all.bundle", "state": "original"},
    {"name": "localisation_assets_localisationenglish.bundle", "state": "original"},
    {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}
  ]
}
```

### 4.3 Live Save Hash Comparison vs. Pre-Run Manifest (`20261022T154008228446Z.json`)
- **Unchanged (4 files — including the `Slot1/8000.sav` campus save):**
  - `Cloud/210252614/Saves/Slot1/8000.sav` (`5b4dac72e35d877f6b7f2d6933a8b0c44717ec2578052d1d9f218f983d050d0d`)
  - `Cloud/210252614/preferences.json` (`f2ff575ab51636cd0b380f6f12f9221b905acce7e89a4677824d16e118877c9e`)
  - `Cloud/210252614/steam_autocloud.vdf` (`b5d31412181fb1e37bed11e0bfbc2ed973c01ba5eb4aa00b3da786a625ded124`)
  - `localpreferences.json` (`3a32b89c9050ee0dea84c4ba8b632e0f81d82da25da517babd0442b5889fab8b`)
- **Changed (7 files — routine `career.csav` backup rotation on level entry and `userprofile.sav`):**
  - `Cloud/210252614/Saves/Slot1/career.csav`: `072f2ac9...` -> `5067a7b0ef3ffde5f603e894108a985227a06275ef50d0e242b832030809c3a8`
  - `Cloud/210252614/Saves/Slot1/career.csav.2.bak`: `d61a300f...` -> `26339e1c0dee45e54ee5bbb88c85e493b00c43fb09d2a057a6567f5cb92ce60d`
  - `Cloud/210252614/Saves/Slot1/career.csav.3.bak`: `c51ca1bc...` -> `072f2ac9449f60467140e5e08576e85d14c253afefd60cfdccf68b8f371fa16d`
  - `Cloud/210252614/Saves/Slot1/career.csav.4.bak`: `27fd1082...` -> `d61a300fd9156feec475b10ba9fb65a34163bcc507f49c12afe7ca124c37dd00`
  - `Cloud/210252614/Saves/Slot1/career.csav.5.bak`: `cbbded52...` -> `c51ca1bc4f0fcb92a45e285ba530bb02adeb47babf87556d5dbade325cc808d9`
  - `Cloud/210252614/Saves/Slot1/career.csav.6.bak`: `f9730de4...` -> `27fd1082d3b44549301f56fe4308fd5238d92e1f3c73a19287ae1f4d7e39ed51`
  - `Cloud/210252614/userprofile.sav`: `df3dcfc0...` -> `ba5d458d3904904778ef6f875bb42edd26400c3e44b32cf5892df9cb7ffb397e`
- **New Files:** `[]`
- **Missing Files:** `[]`
- Live saves and the verified pre-run backup ZIP/manifest are retained untouched.

---

## 5. Summary & Recommendation for Controller

1. **Navigation & Click Reliability Confirmed:**
   - Calling `qa_driver.set_desktop()` at the start of each Python subprocess attaches to the interactive desktop so `GetForegroundWindow()` accurately reports `TPC.exe` (`hwnd`), eliminating false focus-loss readings.
   - Single-clicking Main Menu `Continue` at normalized `(274, 418)` (native `(549, 837)`) and Campaign Card `Continue` at normalized `(223, 850)` (native `(446, 1700)`) both succeeded on the first click with `SendInput` returning `1/1` for every event and visible button hover brightening (`RGB (63, 168, 66) -> (101, 201, 101)`).
2. **Wait Window Adjustment Needed for Opening Modal Capture:**
   - Because `Slot1` (`8000.sav`) was saved prior to the initial modal, loading `Freshleigh Meadows` takes `~12.5s` for the loading screen plus `~24–28s` for the opening camera flyover cutscene (`~37–40s` total).
   - Extending the post-click bounded wait on Campaign Card `Continue` from **30 seconds to 45–50 seconds** will allow the opening camera flyover to finish and land directly on the `First Day of School` (`Scientography`) modal without any additional clicks.
