# WO-SARA-AM-LIG-001 — ligature executor probe, single run

2026-10-26. Assigned Antigravity Desktop QA. READY_FOR_HANDOFF; execution/receipt not confirmed. PM (Claude) does no screen testing. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod. Read first: ../SARA_AM_005_LIGATURE_PROBE_BUILD.md, ../SARA_AM_005_ACCEPTANCE.md, WO_SARA_AM_002_AB_R2.md and its report (same navigation/focus/input rules apply and are NOT repeated in full below), reports/sara-am-lig-001-build.json, local/prototype/probe-sara-am-lig-001/manifest.json (all expected hashes).

## Question

Does the game render the diagnostic intro modal with the serialized ligature [118,42,82] executed? Probe probe-sara-am-lig-001 = frozen005 + one I2LS_Levels533 diagnostic text + exactly one added TMP ligature record mapping ต่ำ (U+0E15 U+0E48 U+0E33) to the glyph of ก. It is a deliberately wrong sentinel, NOT a fix and not a translation. Do not rebuild or alter it.

## Specimen rows (exact, as built)

L1 ต่ำ (target) · L2 ต้ำ (negative control) · L3 ค่ำ (negative control) · L4 ตา ถี่ (ordinary controls) · L5 ก alone (sentinel reference). Row labels L1: to L5: are part of the text; do not rename or reorder.

## Execution scope

One variant only, one run. Maximum 10 minutes active, one focus recovery total, maximum two primary native PNGs (modal; plus one failure screen only if the modal is not reached). Do not run any other candidate, original or earlier probe. Do not change Settings/UI scale, build/spend/hire/start year, or advance tutorials. Do not dismiss the modal.

Navigation as in A/B R2: after set_desktop() in every fresh subprocess, verify unique TPC.exe owner path in the Campus folder, derive targets from fresh native pixels with explicit mapping (normalized = native*1920/W, *1080/H), hover then one click each on main-menu Continue and the existing Slot1 campaign-card Continue (never Restart/New Game). After Continue allow up to 60 seconds for loading and natural flyover, observing at intervals of at most 15 seconds, no skip/click/key. If 60 seconds pass without the modal, keep a full-screen failure image and stop. If the modal appears but rows L1-L5 are not present, mark BINDING_UNCONFIRMED and stop.

## Lifecycle (game closed at each step; inspect each output)

1. `python tools/manage_probe.py check --probe probe-sara-am-lig-001` requires original/original/original.
2. `python tools/backup_gameplay_saves.py` requires verified=true; record ZIP/manifest.
3. `python tools/manage_probe.py install --probe probe-sara-am-lig-001`.
4. check again: requires probe/probe/probe and manifest hashes.
5. Launch via Steam, observe, capture at modal, exit normally (Alt+F4/WM_CLOSE); confirm TPC.exe is gone. If normal close is blocked after the one recovery, stop and report; no forced termination or guard bypass.
6. `python tools/manage_probe.py restore --probe probe-sara-am-lig-001`.
7. check: requires three originals. Exit/restore takes priority over time and setup failures.

Compare save hashes changed/new/missing; keep live saves and backup, no rollback, deletion or Cloud edits, no commit/push.

## Observation (at the modal)

Capture the original native PNG. For each of L1-L5 record exactly what is visible; do not interpret from a readable body alone.

- L1: (a) single ก-shaped glyph replacing ต่ำ, matching L5; (b) original atomic ต่ำ still shown (note crowding/overlap as in A/B R2); (c) blank, tofu, partial or odd sequence, clipping.
- L2, L3, L4 must be unchanged. Any sentinel appearing there is a specificity violation: report it.
- L5: ก must be visible; if absent/tofu, glyph loading is unresolved and L1 cannot be read as a negative.
Record whether lines clip or wrap. Observed time of modal is an observation time only. Do not draw conclusions about correct Thai shaping, engine internals or a production fix.

## Report

NEW docs/qa/WO_SARA_AM_LIG_001_REPORT.md; images in local/qa/WO-SARA-AM-LIG-001/. Include hashes, geometry/mapping, desktop/query order, guard/input errors, recovery count, elapsed observation times, L1-L5 table, lifecycle outputs, save comparison. Verdict: EXECUTED (L1 a, L2-L4 intact, L5 visible) / NOT_EXECUTED (L1 b with L5 visible and L2-L4 intact) / INCONCLUSIVE (L1 c, L5 absent, controls changed) / SETUP_LIMIT / BINDING_UNCONFIRMED. Stop after report; BUG-THAI-003 stays OPEN pending PM analysis.
