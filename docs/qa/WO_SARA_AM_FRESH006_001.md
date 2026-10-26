# WO-SARA-AM-FRESH006-001 — fresh-translation-006, menu surfaces + real opening modal, Medium scale

2026-10-26. Assigned Antigravity Desktop QA, or the tester the user explicitly authorizes (state who in the report). READY_FOR_HANDOFF; execution/receipt not confirmed. PM does no screen testing. Workdir D:/SteamLibrary/steamapps/common/Two Point Campus/ThaiCampusMod. Read first: ../SARA_AM_008_ACCEPTANCE.md, ../SARA_AM_008_PRODUCTION_CANDIDATE.md (plan entries P5, P9, C1-C4 with exact text/codepoints; reports/sara-am-008-regression-plan.json), WO_SARA_AM_GLYPH_002.md and its report (navigation, guard, mapping, cadence and lifecycle rules apply), local/prototype/fresh-translation-006/manifest.json (expected hashes). Candidate = frozen 005 text/UI + fonts bundle with 15 cluster composites/ligatures. NOT a diagnostic probe: the real game text is shown. Do not rebuild or alter it.

## Question

On real screens, do the clusters render correctly stacked (tone above the ring, clear gap, normal baseline, no clipped tone tops, no tofu/overlap/new wrap) with the candidate installed, and does unaffected Thai text (ถี่, ที่, เตี้ย, etc.) stay normal?

## Scope

One run, one candidate, Medium UI scale as found (read the current UI Scale caption, do not change it). NO Settings changes, no graphics/language/autosave/filter changes, no tutorial progression, no build/spend/hire/year start, no dismissing the opening modal. At most 15 minutes active, one focus recovery total, at most 5 primary native PNGs (suggested: Settings > Game, Settings > Video tooltip, opening modal, plus up to two more only if needed). Navigation as in GLYPH-002 (set_desktop() first, unique exact-owner guard, fresh-pixel targets, hover then one click, normalized = native*1920/W,*1080/H). Observation intervals while waiting for the modal at most 15 s; keep actual intervals in the report. If any step cannot be reached after reasonable effort within the budget, mark that cell NOT_REACHED and continue with the next; never create state to reach it.

## Sequence (all read-only)

A. From the main menu open Settings > Game. Inspect: P5 AdvisorFilter_HideLowPriority option label "ซ่อนความสำคัญต่ำ" (target ต่ำ, atomic U+0E15 U+0E48 U+0E33); controls C1 "ความถี่บันทึกอัตโนมัติของโหมดอาชีพ" and C2 "ความถี่บันทึกอัตโนมัติของเกม" (ถี่, accepted BUG-THAI-001 control), C4 "ตัวกรองที่ปรึกษา". Do not open dropdowns beyond what is needed to read a label; do not select any value. Record the UI Scale caption.
B. Settings > Video: find the Ambient Occlusion Quality row and hover its tooltip (P9, three lines; target ต่ำ in "การตั้งค่าต่ำภาพสวยน้อยกว่า..." plus ordinary ค่า). Hover only; no value change. If the tooltip cannot be shown without changing a value, mark NOT_REACHED.
C. Leave Settings (Back/close without Apply changes if prompted; if a prompt would apply changes, choose the option that does not). Main-menu Continue, then existing Slot1 campaign Continue (never Restart/New Game). Natural wait up to 60 s without skip/click/key. At the real opening-course modal capture one native PNG without dismissing it. Inspect the intro body text: "ยินดีต้อนรับสู่ Freshleigh Meadows ที่ชีวิตเคลื่อนไปอย่างเชื่องช้าและความคาดหวังก็... ต่ำเตี้ย" (target ต่ำ before เตี้ย: this is the original BUG-THAI-003 defect site) and the second paragraph. Report ordinary controls ที่, เตี้ย, ซึ่ง-type shapes, wrap/line breaks, clipping.

## Lifecycle (game closed at each step; inspect each output)

1. `python tools/manage_probe.py check --probe fresh-translation-006` requires original/original/original.
2. `python tools/backup_gameplay_saves.py` requires verified=true.
3. `python tools/manage_probe.py install --probe fresh-translation-006`.
4. check again: probe/probe/probe, manifest hashes.
5. Launch via Steam, steps A-C, normal Alt+F4 exit, confirm TPC.exe gone. No forced termination or guard bypass.
6. `python tools/manage_probe.py restore --probe fresh-translation-006`.
7. check: original/original/original. Exit/restore takes priority over time. Compare saves; keep live saves and backup; no rollback/deletion/Cloud edits/commit/push.

## Observation rules

Classify every inspected target: (a) stacked correctly, (b) flawed (mis-stack, clipped tone top, wrong spacing/baseline, overlap, wrap), (c) old crowded form, (d) blank/tofu/missing, plus NOT_REACHED. Controls: unchanged/normal or deviation. Compare surrounding text with the previous accepted look where you have an image. Native crops/nearest-neighbour enlargements allowed (state scale); no extra game captures beyond the cap. No claims about other scales, in-campus screens, radio/character/DLC-only clusters or production safety.

## Report

NEW docs/qa/WO_SARA_AM_FRESH006_001_REPORT.md; images in local/qa/WO-SARA-AM-FRESH006-001/. Include tester identity, hashes, geometry/mapping, order/guard/input, recoveries, actual intervals, per-surface table (surface, exact text, target, class, notes), controls, UI Scale caption, lifecycle outputs, save comparison. Verdict: PASS_SCOPED (all reached targets class a, controls normal, list of NOT_REACHED cells) / PARTIAL (list) / FAIL (list) / INCONCLUSIVE / SETUP_LIMIT. Stop after the report; BUG-THAI-003 stays OPEN pending PM analysis and the user's decision on further coverage.
