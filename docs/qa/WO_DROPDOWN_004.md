# WO-DROPDOWN-004 — Settings caption mitigation, two views

2026-10-21. community-merge-006 NOT_RUN. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

Selected-caption overflow changed to0 for19 Settings controls (12 from1, seven from3). Original Thai text, font/material/size/rect and item list templates retained. LogLevel already demonstrated scoped benefit; other controls remain unverified. No hidden controls enabled.

One session, ten-minute observation target, two views: Settings > Game initial view; Settings > Video initial view. One image each, one recovery maximum per view. No scrolling needed, no dropdown opening or selection, no tooltip, gameplay/save loading, graphics/preset changes, source editing or automatic expansion. Identify actual navigation target; no coordinate sweeps. If unavailable within cap, report UNRESOLVED and restore.

In Game view inspect six selected captions, recording visible text/blankness/containment, overlap with arrow/row edge, obvious clipping/missing glyphs. In Video inspect Fullscreen Mode and VSync Thai captions plus ASCII resolution/antialiasing if naturally visible. A value present only below viewport is NOT_OBSERVED, not failed. If UI Scale now readable, record actual value without changing it. No fine shaping approval based on resized captures. Any remaining blank or overflow is valid evidence; do not repair.

With Campus closed, run separately and inspect outputs:
1. python tools/manage_probe.py check --probe community-merge-006 (three original)
2. python tools/manage_probe.py install --probe community-merge-006 (three probe)
3. python tools/manage_probe.py check --probe community-merge-006
4. Launch via Steam, observe/capture the two views only.
5. Quit normally; confirm TPC.exe absent.
6. python tools/manage_probe.py restore --probe community-merge-006
7. python tools/manage_probe.py check --probe community-merge-006 (three original)

Always exit/restore after installed paths, including failures/time limit; restoration takes priority. Retain backups, no force-close/bypass/commit/push. Report inability to restore immediately.

Deliver docs/qa/WO_DROPDOWN_004_REPORT.md with two original image links under local/qa/WO-DROPDOWN-004/, compact control/text/visibility/containment table, actual environment/capture resize/scale, duration/capture count and lifecycle outputs. Verdict VISIBLE_CAPTIONS_CONTAINED / PARTIAL_OR_LAYOUT_FAIL / INCONCLUSIVE, limited to observed selected values. All19 controls, long alternate options, opened lists and gameplay remain unapproved. Stop after report.
