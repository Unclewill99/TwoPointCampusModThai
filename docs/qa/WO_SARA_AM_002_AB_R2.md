# WO-SARA-AM-002-AB-R2 — wait through natural intro

2026-10-22. Antigravity Desktop QA. READY_FOR_HANDOFF. Read WO_SARA_AM_002_AB.md, previous A/B report and WO_SARA_AM_003_CONTROL_GATE_REPORT.md plus ../SARA_AM_003_CONTROL_DISPOSITION.md. This is revised authorization to resume existing staged A/B; no rebuild. Original A/B scope, specimen codepoints, hashes, per-variant backup/install/check/normal-exit/restore/check, save comparison and no-progression rules remain mandatory.

## Changes from original A/B WO

- Native navigation evidence now shows Continue can reach flyover. Do not rerun originals merely to reproduce the same gate. Use unchanged probe-sara-am-001a then b, restoring three originals between variants. Check each manifest hash, game closed and fresh verified backup before install.
- In every fresh subprocess call qa_driver.set_desktop() BEFORE foreground/cursor queries and capture/input. Record exact ordering/current driver hash. Retain unique exact-process foreground guard. Do not infer focus loss from a zero handle sampled before desktop attachment. Actual API names are qa_driver.send_mouse_event, click, move_mouse.
- Derive targets from fresh pixels with native dimensions/origin; normalized input=(native_x*1920/W,native_y*1080/H), retain precision until driver rounding. No hard-coded historical points, band indexes or floor rule. Verify hover then one click each at main-menu Continue and existing Slot1 campaign-card Continue. Record return counts, which prove injection acceptance only.
- After campaign Continue, allow **up to 60 seconds** for level loading AND natural opening camera flyover. Observe at intervals no longer than 15 seconds and stop waiting immediately when diagnostic modal appears. No skip/click/key during loading or narration. Waiting naturally consumes no recovery. Do not terminate at 30 seconds merely because flyover still runs.
- If 60 seconds expires without modal, retain a full-screen failure image and stop; no repeated click, navigation sweep or extra run. Do not predict or claim later modal timing. If modal appears but diagnostic A/B/C rows do not, BINDING_UNCONFIRMED and stop.
- Maximum 15 minutes active across both variants; one focus recovery total. Fresh observations for navigation/readiness are permitted. Retain max two primary evidence images total: modal per variant, or failure screen in place of unreached modal. Evidence cap does not forbid observing current state. Preserve earlier reports/images.

## At modal

Do not dismiss it. Capture original native PNG. Record rows A atomic ต่ำ, B reordered decomposed, C original-order decomposed and ถี่ controls exactly as original WO. Compare same row between candidates and existing offline reference; no Unicode production changes. Exit normally via Alt+F4/WM_CLOSE and restore before b. If input/control/normal exit fails after recovery, stop and report; no force termination or bypass.

If a succeeded, b is allowed only with usable control and confirmed originals after a. No font/source/on-the-fly changes. Still no hiring/building/year start/tutorial progression, save rollback, Cloud edits, commit or push.

## Report

NEW docs/qa/WO_SARA_AM_002_AB_R2_REPORT.md, images local/qa/WO-SARA-AM-002-AB-R2/. Include 2x3 result matrix/control, actual modal elapsed time if reached (not predicted), capture geometry/mapping, desktop/query order, guard/input errors and recovery count, variant hashes, lifecycle and save changed/new/missing summary. DIAGNOSTIC_RESULT / SETUP_LIMIT / BINDING_UNCONFIRMED / INCONCLUSIVE. BUG-THAI-003 remains OPEN pending Controller analysis; no global fix claim. Stop after report.
