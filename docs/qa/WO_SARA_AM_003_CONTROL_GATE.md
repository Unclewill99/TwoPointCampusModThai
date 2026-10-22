# WO-SARA-AM-003-CONTROL-GATE — originals only

2026-10-22. Antigravity Desktop QA. READY_FOR_HANDOFF. Read ../SARA_AM_002_AB_DISPOSITION.md. This WO supersedes any automatic retry of installed sara-am A/B. Controller does no UI testing.

Goal: establish reliable original-game navigation from main menu through existing Slot1 campaign card to opening modal, and capture enough evidence to localize any failure. No candidate install, rebuild, font change, configuration/Cloud edits or save rollback. Main-menu label is English on originals; this is not a translation test.

With game closed run manage_probe.py check --probe probe-sara-am-001a: require all three original. Run backup_gameplay_saves.py and retain verified fresh ZIP/manifest. Review current qa_driver input contract: normalized 1920x1080 full-primary-display coordinates; return-count guard now raises if SendInput accepts other than one event. Success count means queued event, not application action. Never bypass guards or automatically replay a failed click.

Budget: five minutes after menu ready; max three retained evidence images (main menu, campaign card with target, final modal or failure screen), one focus recovery total. Intermediate fresh observations permitted for navigation; evidence cap does not prohibit verifying the current screen. Use native dimensions/origin and explicit mapping, actual visible button text, verified process owner TPC.exe full Campus path, one unique window and foreground. Do not use color-band indexes, historical coordinates or center pixel alone to identify screen.

Launch through Steam. At main menu observe readiness then click Continue once; record accepted input events or exact exception. Allow loading to finish. If focus changes, use one recovery to activate the exact returned game window, wait for visible readiness and take a fresh observation. Verify campaign card and visible Continue target from current pixels; confirm cursor/hover at its center before one click. Record native cursor position, target box, normalized input and each SendInput count. Observe full resulting screen after bounded loading wait (up to 30 seconds), not just one pixel.

If the card does not transition, capture failure screen and STOP; no second/double click, keyboard workaround, modal hunting or reinstallation. Do not assert focus ate the click without evidence. If successful, capture opening original modal, do not dismiss or advance tutorial. Do not Restart/New Game, change slot, build/spend/hire/start year.

Exit normally (Alt+F4/WM_CLOSE permitted), confirm TPC.exe absent, manager check three originals; compare save changed/new/missing hashes and retain live saves/backup. If exit is blocked report immediately, no force kill. No commit/push.

Report docs/qa/WO_SARA_AM_003_CONTROL_GATE_REPORT.md with evidence local/qa/WO-SARA-AM-003-CONTROL-GATE/, version/hash of driver used, input return/error evidence, process/focus/capture mapping, full-screen before/after interpretation, timing/recovery and save/bundle checks. Verdict CONTROL_GATE_PASS / SETUP_LIMIT / INCONCLUSIVE. Do not install A/B in this WO even on success; Controller reviews evidence before resuming experiment.
