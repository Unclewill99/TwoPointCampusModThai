# WO-VISUAL-019 — fresh-translation-007 scoped screen check (BUG-THAI-002)

Date issued: 2026-10-26. Owner: user / desktop QA. Candidate: fresh-translation-007 (006 text + SEGMENTATION-002 U+200B). Prerequisite: tools/build_fresh_translation_007.py has run on Windows and reports/fresh-translation-007-build.json exists.

## Setup

1. Close Campus completely. `python tools/manage_probe.py restore --probe fresh-translation-006` then `python tools/manage_probe.py check --probe fresh-translation-006` → all three `original`.
2. `python tools/manage_probe.py install --probe fresh-translation-007` then `check --probe fresh-translation-007` → all three `probe`.
3. Launch the game. Record build string, display resolution and UI Scale for every capture. Captures are full-frame native PNG (no crop, no downscale); crops may be added as extra files.

## Primary cells (must run)

| Cell | Screen | Record | Scale | Pass condition |
|---|---|---|---|---|
| P1 | Loading screen tip "ปูทางไป" (campus map load; may need several loads to reach this tip) | Meta/LoadingScreen/Tips_LS_Paths_Text | Small | No cut inside วิทยาเขต / ภูมิทัศน์ / ภูมิประเทศ; all text present; no visible box/blank glyph |
| P2 | Campus map → Freshleigh Meadows card | Levels/Freshleigh/Level_Description | Small | No cut inside และ / ความคาดหวัง; ต่ำ renders as in 006; all text present |
| P3 | Same as P1 | same | Medium | same |
| P4 | Same as P2 | same | Medium | same |

For each cell, transcribe every visible row exactly and note every line boundary as `word | word`. If a tip or card does not wrap at all, mark NOT_EXERCISED, not PASS.

## Regression cells (Medium, same as FRESH006-001 scope)

R1 Settings > Game page; R2 Settings > Video "Vsync"/"Resolution" tooltips; R3 the real opening modal; R4 any two of the ต่ำ/น้ำ sites listed in reports/sara-am-008-screen-map.json. Pass = identical readability to the 006 acceptance, no new artifact, no missing glyph, no visible U+200B.

## Fail conditions (stop and report)

Any visible glyph where a U+200B sits (box, dot, extra gap), text missing or truncated, a break immediately after เ/แ/โ/ใ/ไ, a detached tone/vowel mark, crash or freeze, or a ต่ำ/น้ำ cluster rendering differently from 006.

## Teardown

Restore UI Scale to Medium. Close the game. `python tools/manage_probe.py restore --probe fresh-translation-007` → `check` → all `original`; then `install --probe fresh-translation-006` → `check` → all `probe`. Report: docs/qa/WO_VISUAL_019_REPORT.md, images under local/qa/WO-VISUAL-019/.
