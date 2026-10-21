# WO-GAMEPLAY-002 — enter first campus, initial text trial

Date 2026-10-21. Candidate community-merge-006. Runtime NOT_RUN. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod.

## User-authorized setup change

User explicitly said to continue after being informed that advancing introduction and starting the first campus updates Slot1 progress. Unlike WO-GAMEPLAY-001, this assignment allows Next/continue through the initial advisor introduction and starting Freshleigh Meadows in the existing Slot1 career. Normal profile/autosave/new campus files may be created. Do not create another career, overwrite a slot, delete saves, or roll back automatically. Retain prior snapshots/live files. Back up again before installation using python tools/backup_gameplay_saves.py; require verified=true and record fresh ZIP/manifest path. If backup fails or Campus running, stop before install. Steam Cloud settings unchanged.

## Bounded observation

One session, 15-minute active observation target. Up to three primary images, one recovery per view. No coordinate sweeps, tooltip hunting, repairs or extra matrix.

1. Continue Slot1. Advance only initial advisor dialogue with visible Next/continue controls (maximum ten advances). Use the visibly named first campus Freshleigh Meadows entry/start control. If any overwrite/reset/new-career confirmation, unexpected transaction or unclear target appears, stop and report SETUP_LIMIT. Starting this first campus is allowed; buying land, building, hiring or choosing other campuses is not.
2. Once campus loads, pause using a visible pause control if available; record actual pause state. Capture initial campus HUD/objective/tutorial panel and readable text. If a modal blocks pause, capture it; do not dismiss further gameplay instructions just to expose the HUD. If unable to pause, stop observation promptly and exit; do not let the simulation run while hunting controls.
3. If paused and an obvious read-only overview/objectives panel is accessible, open ONE and capture it. If not, leave NOT_RUN. No building/hiring/student actions, spending, academic-year start, objective completion or deliberate progress beyond loading first campus. An unopened panel is a valid scope limit, not a failure.

Maximum three captured views total; map/start screen may count as one, campus initial/modal as second, optional read-only panel as third. Inspect for blank text, missing glyphs, raw tokens/tags, severe clipping/readability and at most five language issues. No full transcription/retranslation or fine-shaping approval from resized captures. Keep settings unchanged. Stop after useful initial-campus evidence; do not fill budget with extra activity.

## Lifecycle

With Campus closed, after fresh verified save snapshot, execute separately and inspect output:
1. python tools/manage_probe.py check --probe community-merge-006 (three original)
2. python tools/manage_probe.py install --probe community-merge-006 (three probe)
3. python tools/manage_probe.py check --probe community-merge-006
4. Launch through Steam; perform bounded intro/first-campus trial.
5. Quit normally using visible menu controls. Saving the initial-campus progress to current Slot1 is authorized; do not overwrite another slot. If exit requires a new slot, reset, or unclear destructive action, ask/report rather than guess. Confirm TPC.exe absent.
6. python tools/manage_probe.py restore --probe community-merge-006
7. python tools/manage_probe.py check --probe community-merge-006 (three original)

Normal exit and restoration required on every installed path, including capture/time/setup failure; these take priority over observation budget. Retain backups. No force-close, guard bypass, cache deletion, candidate edit, commit/push or save cleanup. Report inability to exit/restore immediately.

## Deliverable

Write docs/qa/WO_GAMEPLAY_002_REPORT.md with original images under local/qa/WO-GAMEPLAY-002/. Include up to three view/result rows, exact campus and pause state, steps actually advanced, visible technical issues (at most five language observations), actual environment/capture resizing, elapsed/capture/recovery counts, fresh save snapshot path, post-run changed/new/missing save-file hash summary and compact bundle lifecycle output. Save updates are expected; report, do not auto-restore. Do not expose full save contents.

Verdict USABLE_IN_OBSERVED_CONTEXT / BLOCKING_DEFECT / SETUP_LIMIT / INCONCLUSIVE. Unreached views NOT_RUN. This is initial-campus text screening only, not full gameplay/long-session/translation/release acceptance. Stop after report and return path; no automatic follow-up work.
