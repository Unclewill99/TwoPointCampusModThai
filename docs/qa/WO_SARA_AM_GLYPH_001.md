# WO-SARA-AM-GLYPH-001 — appended composite glyph probe, single run

2026-10-26. Assigned Antigravity Desktop QA, or the tester the user explicitly authorizes (state who in the report). READY_FOR_HANDOFF; execution/receipt not confirmed. PM does no screen testing. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod. Read first: ../SARA_AM_006_ACCEPTANCE.md, ../SARA_AM_006_CENSUS_AND_GLYPH_PROBE.md, ../SARA_AM_LIG_001_ACCEPTANCE.md, WO_SARA_AM_LIG_001.md and its report (navigation, focus, input and lifecycle rules are identical and apply in full), reports/sara-am-glyph-001-build.json, local/prototype/probe-sara-am-glyph-001/manifest.json (expected hashes).

## Question

In the opening-course modal, does the game load and draw the NEW glyph 459 (reachable only through the ligature [118,42,82] -> 459, no cmap entry), and does it show ต่ำ with the tone mark above and clearly separated from the sara-am ring? Probe = frozen005 + diagnostic text for I2LS_Levels533 + one appended composite glyph in the embedded Thai font + one ligature record. A diagnostic, not a fix or a translation. Do not rebuild or alter it.

## Specimen rows (exact)

L1 ต่ำ (target) · L2 ต้ำ (negative: should look like the old crowded atomic form) · L3 ค่ำ (negative: same) · L4 ตา ถี่ (ordinary) · L5 ทำ (sara-am without tone, ordinary). Labels L1: to L5: are part of the text.

## Execution scope

One run, one variant only. At most 10 minutes active, one focus recovery total, at most two primary native PNGs (modal, plus one failure screen only if the modal is not reached). No other candidate/original/probe, no Settings or UI-scale change, no build/spend/hire/start year, no tutorial advance. Do not dismiss the modal. Navigation as in LIG-001: set_desktop() in every fresh subprocess before queries, unique exact-owner TPC.exe guard, targets from fresh pixels with explicit native-to-normalized mapping, one hover and one click each on main-menu Continue and the existing Slot1 campaign Continue (never Restart/New Game). After the campaign click wait up to 60 seconds without skip/click/key. **Observe at intervals of at most 15 seconds (LIG-001 exceeded this; keep to it, and if the tooling cannot, report the actual intervals).** No modal in 60 s: keep a full-screen failure image and stop. Modal without rows L1-L5: BINDING_UNCONFIRMED and stop.

## Lifecycle (game closed at each step; inspect each output)

1. `python tools/manage_probe.py check --probe probe-sara-am-glyph-001` requires original/original/original.
2. `python tools/backup_gameplay_saves.py` requires verified=true.
3. `python tools/manage_probe.py install --probe probe-sara-am-glyph-001`.
4. check again: probe/probe/probe and manifest hashes.
5. Launch via Steam, observe, capture at modal, exit normally (Alt+F4/WM_CLOSE), confirm TPC.exe is gone. If normal close is blocked after the one recovery, stop and report; no forced termination or guard bypass.
6. `python tools/manage_probe.py restore --probe probe-sara-am-glyph-001`.
7. check: original/original/original. Exit/restore takes priority over time and setup failures. Compare save hashes (changed/new/missing); keep live saves and backup; no rollback/deletion/Cloud edits/commit/push.

## Observation at the modal

Capture one original native PNG. Record what is visible per row; do not infer from a readable body alone. Derived native crops are allowed (state scale/interpolation); no extra game captures.

- L1: classify as (a) new composite glyph visibly stacked (tone above the ring, gap visible, base and aa on the normal baseline), (b) rendered but flawed (mis-stacked, wrong width/spacing, baseline shift, clipped top of the tone mark, line-height change), (c) old crowded atomic ต่ำ unchanged, (d) blank/tofu/partial/other.
- L2/L3: expected old crowded form; any change is a specificity finding. L4/L5 must be ordinary; note any baseline, spacing or line-height change versus the LIG-001 modal (compare to its saved image qualitatively).
- Explicitly record: top clipping of the tone mark in L1 (the glyph top exceeds the font ascent by 22 units; a deliberate known risk), horizontal advance of L1 versus neighbours, whether lines clip or wrap.
No conclusions about shaping correctness in general or a production fix.

## Report

NEW docs/qa/WO_SARA_AM_GLYPH_001_REPORT.md; images in local/qa/WO-SARA-AM-GLYPH-001/. Include tester identity, hashes, geometry/mapping, desktop/query order, guard/input errors, recoveries, observation times with actual intervals, L1-L5 table, lifecycle outputs, save comparison. Verdict: STACKED_OK (L1 a, controls intact) / RENDERED_FLAWED (L1 b) / NOT_APPLIED (L1 c) / FAILED (L1 d) / INCONCLUSIVE / SETUP_LIMIT / BINDING_UNCONFIRMED. Stop after the report; BUG-THAI-003 stays OPEN pending PM analysis.
