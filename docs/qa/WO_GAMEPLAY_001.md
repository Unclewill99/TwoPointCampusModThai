# WO-GAMEPLAY-001 — practical merged-mod trial, existing career

Date 2026-10-21. Candidate community-merge-006. Gameplay NOT_RUN. Working directory D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

## Goal and save context

Check initial campaign/gameplay text under actual use, not a Settings regression. Existing local Cloud/210252614/Saves/Slot1/career.csav was found; no separate campus save was found in that directory. A verified five-file snapshot is under local/backups/gameplay-save-snapshots/20261021T145707742752Z.zip with adjacent hash manifest. Do not assume Slot1 already contains a playable campus.

Before each run, with Campus closed, execute python tools/backup_gameplay_saves.py and require verified=true; record its new backup/manifest path. It copies Cloud files and local preferences locally and never changes sources. Stop before installing if it fails. Do not delete or restore save files automatically, disable Steam Cloud, or overwrite an occupied slot. Loading/normal exit may update profile/autosaves; record changed hashes against the fresh snapshot after exit, retain both live files and backup. Bundle restore does NOT restore saves.

## Budget and views

One session, 15-minute active observation target, at most THREE primary screenshots and one recovery per view. No coordinate sweeps, tooltip hunting, source edits or repairs.

1. Continue existing Slot1 career using visible UI. If a slot picker appears choose Slot1 only. Capture campaign map or first meaningful career view: names, objective/progression labels and obvious raw tokens/blank text. If no Continue/existing route, or creation/overwrite confirmation is required, stop at that screen; remaining views NOT_RUN. Do not create a new career.
2. If there is an existing resumable campus, resume it and pause using a visibly identified pause control; capture initial campus HUD/objective or tutorial panel. Do not start a new campus, spend money, build, hire, dismiss a tutorial, or advance academic time deliberately. If no resumable campus is offered, end at map; lack of an available save is a setup limit, not a translation failure.
3. If accessible while paused, open ONE read-only overview panel with visible text (objectives/finance summary/student overview; choose first obvious non-transactional option). Capture its heading and body. Do not open sale/build/hire controls or chase inaccessible menus. No gameplay progress is required.

Inspect for missing glyphs, blank expected text, raw placeholders/tags, severe clipping and readability. List at most five concrete translation issues with view/key uncertainty; do not retranslate the screen. Record ASCII/proper names as observations, not automatic failures. Fine shaping and exhaustive language coverage unverified. Keep current settings unchanged; no graphics/scale/preset adjustments.

## Bundle lifecycle

After successful fresh save backup and with Campus closed, execute separately and inspect:
1. python tools/manage_probe.py check --probe community-merge-006 (three original)
2. python tools/manage_probe.py install --probe community-merge-006 (three probe)
3. python tools/manage_probe.py check --probe community-merge-006
4. Launch via Steam and perform bounded views above.
5. Quit normally; confirm TPC.exe absent. If game asks to save, use a clearly offered Quit Without Saving when available; never overwrite another slot. If no safe exit choice is clear, report/ask rather than force-close. Normal automatic profile writes may still occur and must be recorded.
6. python tools/manage_probe.py restore --probe community-merge-006
7. python tools/manage_probe.py check --probe community-merge-006 (three original)

Always normal-exit/restore after any installed path, including time/capture/setup failure. Exit/restoration takes priority over observation budget. Retain original bundle backups. No force-close, bypass, cache deletion, commit/push or cloud/saves cleanup.

## Report

Write docs/qa/WO_GAMEPLAY_001_REPORT.md; original evidence local/qa/WO-GAMEPLAY-001/. Include up to three view/status rows, actual selected career/campus, whether pause established, exact visible failures and up to five language issues, image links/environment/resizing, duration/capture counts, fresh save backup path and post-run changed/new/missing save-file hash summary, compact three-bundle restoration output. Avoid dumping save contents or account identifiers unnecessarily.

Verdict USABLE_IN_OBSERVED_CONTEXT / BLOCKING_DEFECT / SETUP_LIMIT / INCONCLUSIVE. Map-only observation cannot approve campus gameplay. Screens not reached stay NOT_RUN. Stop after report; do not automatically create a career or add tests to fill gaps.
