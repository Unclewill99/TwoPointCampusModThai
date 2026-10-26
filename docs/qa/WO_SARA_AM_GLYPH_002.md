# WO-SARA-AM-GLYPH-002 — 15-cluster probe, single run

2026-10-26. Assigned Antigravity Desktop QA, or the tester the user explicitly authorizes (state who in the report). READY_FOR_HANDOFF; execution/receipt not confirmed. PM does no screen testing. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod. Read first: ../SARA_AM_007_ACCEPTANCE.md, ../SARA_AM_007_CLUSTER_SET_PROBE.md, WO_SARA_AM_GLYPH_001.md and its report (navigation, focus, input, cadence and lifecycle rules apply in full), reports/sara-am-glyph-002-build.json, local/prototype/probe-sara-am-glyph-002/manifest.json (expected hashes).

## Question

In the opening-course modal, does each of the 15 census clusters render with the appended composite glyph (tone above the ring, clear gap, normal baseline, no clipping), while out-of-set and ordinary text stays unchanged? Diagnostic only: not a fix, not a translation. Do not rebuild or alter the probe.

## Specimen (exact, five lines; labels are part of the text)

L1: น้ำ ซ้ำ ต่ำ ล้ำ · L2: ร่ำ ค่ำ ถ้ำ ด่ำ · L3: ฉ่ำ ล่ำ ค้ำ ย้ำ · L4: ว่ำ น่ำ ม่ำ ท่ำ · L5: ตา ถี่ ทำ นำ. ท่ำ is NOT in the set and is the negative control (expected old crowded form). L5 are ordinary controls.

## Execution scope

One run, one variant. At most 10 minutes active, one focus recovery total, at most two primary native PNGs (modal; plus a failure screen only if the modal is not reached). No other candidate/original/probe, no Settings or UI-scale change, no build/spend/hire/start year, no tutorial advance, do not dismiss the modal. Navigation, guard, mapping, 60 s natural wait and observation cadence as in GLYPH-001 (observation intervals at most 15 s; report actual intervals). No modal within 60 s: keep a full-screen failure image and stop. Modal without the L1-L5 rows: BINDING_UNCONFIRMED and stop.

## Lifecycle (game closed at each step; inspect each output)

1. `python tools/manage_probe.py check --probe probe-sara-am-glyph-002` requires original/original/original.
2. `python tools/backup_gameplay_saves.py` requires verified=true.
3. `python tools/manage_probe.py install --probe probe-sara-am-glyph-002`.
4. check again: probe/probe/probe and manifest hashes.
5. Launch via Steam, observe, capture at modal, exit normally (Alt+F4/WM_CLOSE), confirm TPC.exe gone. No forced termination or guard bypass; if normal close is blocked after the one recovery, stop and report.
6. `python tools/manage_probe.py restore --probe probe-sara-am-glyph-002`.
7. check: original/original/original. Exit/restore takes priority. Compare saves (changed/new/missing); keep live saves and backup; no rollback/deletion/Cloud edits/commit/push.

## Observation

Capture one original native PNG. Derived native crops (and nearest-neighbour enlargements, stated) are allowed; no extra game captures. Classify EACH of the 15 targets individually: (a) stacked (tone above ring, gap visible, base and aa on baseline, complete), (b) flawed (mis-stack, wrong width/spacing, baseline shift, clipped tone top, overlap with neighbour), (c) old crowded form unchanged, (d) blank/tofu/partial/missing. Also: ท่ำ (expect crowded), L5 controls (expect ordinary), whether any line wraps, clips or shifts, line spacing versus the GLYPH-001 modal (qualitative; note that line count and text differ). Check the tone-top region of every item for clipping; the known ascent excess (19-22 units) was left unmodified. Compare identical-word renderings where possible (ต่ำ here is a re-geometry of the glyph-001 result: compare it qualitatively with that modal image). No conclusions about other UI scales, other consumers or production safety.

## Report

NEW docs/qa/WO_SARA_AM_GLYPH_002_REPORT.md; images in local/qa/WO-SARA-AM-GLYPH-002/. Include tester identity, hashes, geometry/mapping, desktop/query order, guard/input errors, recoveries, observation times with actual intervals, a 15-row table of target -> class (a-d) with notes, controls, lifecycle outputs, save comparison. Verdict: ALL_STACKED_OK (15/15 class a, controls intact) / PARTIAL (list failing clusters and class) / NOT_APPLIED / FAILED / INCONCLUSIVE / SETUP_LIMIT / BINDING_UNCONFIRMED. Stop after the report; BUG-THAI-003 stays OPEN pending PM analysis.
