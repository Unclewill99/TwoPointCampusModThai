# WO-SARA-AM-008 — candidate accepted (BUILD_READY); regression plan narrowed by PM

2026-10-26. PM (Claude): ACCEPT_BUILD for local/prototype/fresh-translation-006; regression plan ACCEPTED WITH NARROWING. BUG-THAI-003 OPEN.

## PM verification (independent)

- Re-hashed the three 006 bundles: fonts bundle is byte-identical to probe-sara-am-glyph-002's fonts bundle (and differs from 005); localisation bundle is byte-identical to 005 (differs from glyph-002, so the diagnostic specimen is absent); UI bundle identical to 005 and glyph-002. Text unchanged, fix lives only in the fonts bundle. Font content was previously verified by PM under WO-007 (same bytes).
- Reports reviewed: census cross-check 440 occurrences / 15 clusters / 0 outside-set and 0 collisions in stored text; manager check original/original/original; 29 protected hashes before/after per the analyst (local ones are re-checkable; game-folder files outside PM mount, re-checked by the runtime lifecycle).
- Not independently parsed by PM: TMP ligature readback (relies on the analyst and WO-007 verification of identical bytes), the 410-record screen map.

## Key finding from the plan (PM reading)

The real opening-course modal text of Freshleigh (I2LS_Levels 533, Level_Intro_Text) itself contains atomic ต่ำ ("...ความคาดหวังก็... ต่ำเตี้ย"). That is the original BUG-THAI-003 defect site seen in the user's image, and it is on the already proven navigation path. It is the most important real-screen check.

## Narrowing decision

Nine campus/menu contexts at three UI scales is too large for one bounded run, and most in-campus contexts (staff inspectors, event setup, item catalogue, course preview) need tutorial progression, hiring or other state changes that earlier QA rules forbid, and their reachability is unproven. PM splits the runtime work:

1. WO-SARA-AM-FRESH006-001 (this issue): install 006 once, Medium scale only, no setting changes. Menu-only contexts first (Settings > Game: P5 ซ่อนความสำคัญต่ำ with ต่ำ; controls C1, C2, C4; Settings > Video: P9 multi-line tooltip containing ต่ำ), then Continue -> the real opening modal (C3, ต่ำ at the original defect site, plus ordinary ที่/เตี้ย controls).
2. Later, depending on result and on a user decision: UI scale Small/Large (needs a Settings change, restore to Medium); in-campus contexts only if the user allows leaving the opening modal/tutorial; radio/character/DLC-only clusters stay NOT_TESTED unless naturally visible.
3. Install of 006 into the user's live game is a separate decision for the user after regression is accepted. The runtime WOs always restore originals at exit.

Cross-consumer collision and rich-text/fallback behavior remain UNKNOWN until runtime shows each surface; unreachable surfaces will be reported as NOT_TESTED, not inferred.
