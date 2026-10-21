# WO-GAMEPLAY-002 scoped acceptance — 2026-10-21

ACCEPT_USABLE_INITIAL_CAMPUS_CONTEXT_WITH_KNOWN_ISSUES. Controller read report and inspected campaign start card, campus flyover and 03-campus-hud-or-modal-r1.jpg. Campus opens with readable Thai in initial modal/course labels; no blank text, missing glyph box or raw token observed in these images. Internal Thai split ของคุ / ณ is an observed technical wrapping defect, not a language-only note. It is consistent with still-open BUG-THAI-002; no global wrapping PASS. Optional overview/HUD remains NOT_RUN behind modal. Automatic simulation pause is tester-attributed; actual HUD pause control was not observed. Initial entry is not full practical gameplay acceptance.

Report records six image files and11 minutes; optional logical third view was not reached. Capture naming reflects flyover/modal recovery stages rather than three independent successful views. Do not infer extra coverage from file count. No repeated opening-modal WO assigned.

Controller verified six pre-run ZIP entries against manifest hashes and live inventory:3 changed,4 new,0 missing,3 unchanged. Campus8000.sav now exists. Live saves/backups retained unchanged by Controller. Fresh manager check confirms three installed original bundles. No install/game run/commit/push by Controller.

## Bounded correction backlog

1. Levels/Freshleigh/Level_Intro_Text (I2LS_Levels segment533): observed internal word split; prefer concise source-faithful rewriting and contextual review before opt-in breakpoint experiments. No automatic global ZWSP.
2. Courses/Courses/Science_Name (I2LS_Courses segment215): Scientography -> วิทยาศาสตร์แผนที่ is questionable for this fictional course; review project glossary/course description before deciding one consistent replacement.
3. Place-name consistency across advisor/campus text: identify exact records before editing, preserve proper-name policy.
4. Reported space in ผู้ บริหารวิทยาเขต: distinguish source whitespace from rich-text/font spacing before fixing.
5. ต่ำต้อย in opening modal is stylistically questionable, but English source actually says lowly (not merely low). Treat as contextual wording/pun review, not a proven literal mistranslation.

Next work: targeted text/context correction for observed records; no bulk retranslation or additional screen matrix. merge-006 remains current integrated trial baseline with known wrapping/language issues; not release approved. Entering HUD requires separately allowing dismissal of opening modal, not repeated capture of same blocked view.


## User correction — BUG-THAI-003

User supplied closer PNG showing mai ek/sara-am collision in ต่ำ of ต่ำต้อย. Record an observed shaping defect, not merely unresolved fine detail. Earlier absence of blank/glyph boxes does not imply correct marks. Initial-entry acceptance remains qualified by this additional defect. Exact screenshot preserved with hash; see qa/BUG_THAI_003.md. No unchanged reproduction run assigned.
