# WO-DROPDOWN-003 — Thai caption overflow control

2026-10-21. community-merge-005, NOT_RUN. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

Only LogLevel selected-caption object 295032210435112665 changes: m_overflowMode 1 to 0, matching working Thai row labels. Font/material/size/rect and Thai localisation identical to merge-002. CHECK marker removed by using merge-002 baseline. Expected current option from last observation: ข้อผิดพลาด (Error); record actual, do not change selection. Other dropdowns remain untouched and may stay blank.

One session, one view Settings > Game, five-minute observation target, one image plus at most one recovery. No dropdown opening/value changes, tooltip, other screens, save loading, sweeps or graphics changes. Verify real menu/navigation target; if unavailable within cap, stop INCONCLUSIVE. UI scale uncertain unless independently observed. No repair or automatic expansion.

With Campus normally closed, execute separately and inspect output:
1. python tools/manage_probe.py check --probe community-merge-005 (three original)
2. python tools/manage_probe.py install --probe community-merge-005 (three probe)
3. python tools/manage_probe.py check --probe community-merge-005
4. Launch Steam game, Settings > Game, capture LogLevel and adjacent unchanged controls. Record exact visible text, containment relative to orange box, clipping, text crossing arrow/other rows, obvious missing glyphs. Overflow-visible text is not automatically a layout PASS.
5. Quit normally and confirm TPC.exe absent.
6. python tools/manage_probe.py restore --probe community-merge-005
7. python tools/manage_probe.py check --probe community-merge-005 (three original)

Restore on all installed paths; normal exit/restoration takes priority over observation budget. Retain backups; no bypass/force-close/source edit/commit/push. Report failure to exit/restore immediately.

Deliver docs/qa/WO_DROPDOWN_003_REPORT.md, original evidence local/qa/WO-DROPDOWN-003/. Verdict THAI_VISIBLE_CONTAINED / THAI_VISIBLE_LAYOUT_FAIL / STILL_BLANK / INCONCLUSIVE. Include exact text, environment/capture resizing, scale uncertainty, duration/capture counts and compact restore evidence. One result cannot approve all dropdowns or fine shaping. Stop after report.
