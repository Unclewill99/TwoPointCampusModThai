# WO-DROPDOWN-002 — ASCII marker control, one view

Date 2026-10-21. Candidate community-merge-004, runtime NOT_RUN. Working directory D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

Goal: observe only LogLevel selected caption in Settings > Game. Its six possible option translations now read CHECK + original English. Font/UI equal merge-002, not merge-003. Other dropdowns may remain blank. No Thai fix is claimed.

One session, 5-minute active observation target, one image + at most one recovery. Navigate from actual visible main-menu Settings button. No coordinate sweeps, dropdown opening, option selection, tooltip, save loading, preset/graphics changes, source edits or automatic follow-up. If navigation/target fails within cap, report INCONCLUSIVE and restore. Do not infer UI scale from blank control.

With Campus closed, run separately, inspecting result:
1. python tools/manage_probe.py check --probe community-merge-004 (three original)
2. python tools/manage_probe.py install --probe community-merge-004 (three probe)
3. python tools/manage_probe.py check --probe community-merge-004
4. Launch via Steam; Settings > Game; capture LogLevel and adjacent controls once. Record exact visible caption if present.
5. Quit normally, confirm TPC.exe exited.
6. python tools/manage_probe.py restore --probe community-merge-004
7. python tools/manage_probe.py check --probe community-merge-004 (three original)

Always restore after installed paths including time/capture failure; restoration takes priority over observation budget. Keep backups, do not bypass guards or force-close. Report inability to exit/restore immediately. No commit/push.

Write docs/qa/WO_DROPDOWN_002_REPORT.md with verdict CHECK_VISIBLE / STILL_BLANK / OTHER_TEXT / INCONCLUSIVE, one original image under local/qa/WO-DROPDOWN-002/, exact caption, current build/capture/scale uncertainty, elapsed/capture counts and compact lifecycle outputs. Stop after report. No exhaustive review or additional screen test.
