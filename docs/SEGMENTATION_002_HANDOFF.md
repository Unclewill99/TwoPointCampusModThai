# SEGMENTATION-002 — corpus-wide break opportunities, candidate fresh-translation-007

Date: 2026-10-26 (Asia/Bangkok). PM/Controller: Claude. Status: candidate PREPARED, build NOT_RUN on Windows, runtime NOT_RUN. BUG-THAI-002 remains OPEN.

## Trigger

User reported two production screens on installed fresh-translation-006 at UI Scale Small: the loading-screen tip Meta/LoadingScreen/Tips_LS_Paths_Text wraps as `รอบวิ | ทยาเขต` (inside วิทยาเขต) and Levels/Freshleigh/Level_Description wraps as `ต่ำแล | ะมี` (inside และ). Evidence and codepoint offsets: local/qa/BUG-THAI-002/evidence.json plus the two user PNGs there. This is the first BUG-THAI-002 observation on production text and containers; previous evidence was the synthetic probe-016 tooltip only. The ต่ำ ligature (BUG-THAI-003 fix) renders correctly at that edge.

## Decision

The 2026-10-18 gate asked for evidence on real text before widening ZWSP beyond experiments; WO-017 and WO-018 already showed that explicit U+200B opportunities move breaks to the proposed boundaries without visible artifacts, in the same font lineage. With production failures now observed, Controller (with the user's explicit choice in chat) prepares a corpus-wide experimental candidate rather than patching two records. Ordinary Thai (006) stays installed until the candidate passes a scoped screen check; the gate's other reservations (no dictionary claim, no release approval, no global width/layout change) are unchanged.

## What was produced

- tools/segmentation_guard_002.py — shared structural guard. A cut is rejected when it is adjacent to whitespace, after a leading vowel (เแโใไ), before a combining mark, before ะ า ำ ๅ ๆ ฯ, after ั or ็, before closing or after opening punctuation, not between two Thai letters, or inside a `{token}`, `<tag>`, `[i2…]` or Latin/number run. `validate()` also requires the exact source SHA-256, sorted unique offsets, literal equality after stripping U+200B, unchanged token/tag sequence and unchanged LF/tab counts. 16 negative controls (including ต่ำ at both internal offsets, ชนะ, ซ้ำๆ, วันนี้, quotes and Thai–Latin adjacency) are rejected by self_test().
- tools/segment_corpus_002.py — offline proposal generator (PyThaiNLP 5.4.0 newmm; dictionary = thai_words() + local/segmentation/SEGMENTATION-002/extra-words.txt, 69 curated Campus loanwords/proper nouns such as ไอเท็ม, เคาน์ตี, เลเวล, แซนด์บ็อกซ์, เอ็กโทพลาซึม, ลิมเพตต์, แคสเซอโรล). Input is the r5 corpus with the one approved 005 override (I2LS_UI segment 964 = Mod), i.e. exactly the 006 text. Tokens are proposed only inside non-protected spans; every boundary goes through the guard. Run in Controller's Linux environment, not on the game machine; it does not need UnityPy.
- local/segmentation/SEGMENTATION-002/cut-map.json — 15,677 records keyed by (asset, segment_index, key) with source SHA-256, codepoint cut offsets and marked-text SHA-256. Stats: 11,429 records with cuts, 84,223 cuts; guard rejections 28,182 whitespace-adjacent, 2,775 before closing punctuation, 610 after opening punctuation, 464 after ั/็, 435 non-Thai boundary, 40 before ะ/ๆ. preparation.json records the map hash; review-marked.tsv shows every marked record with `|` at each cut for human review.
- Independent check: all 440 BUG-THAI-003 clusters ([consonant][tone]ำ) contain no cut, so the 15 exact 3-component TMP ligatures still match.
- The newmm units for the WO-017 paragraph equal the 16 units Controller specified by hand on 2026-10-18, and both reported records receive `รอบ|วิทยาเขต` and `ต่ำ|และ|มี`.
- tools/build_fresh_translation_007.py — stages fresh-translation-007 from frozen 006: fonts/UI copied byte-identical, only the localisation bundle rewritten. For every segment it re-validates the cut with the guard, checks the marked SHA-256, and after reload asserts that stripping U+200B from every segment reproduces the 006 text literally and that untouched segments are byte-equal. Manifest and reports/fresh-translation-007-build.json are written. Controller dry-ran the script against the real 006 localisation bundle (UnityPy 1.25.4, Linux): 15,677 segments reloaded, 11,429 marked, 84,223 U+200B, strip-check passed. The Windows run is still required so the staged candidate carries all three files and hashes on the game machine.
- tools/manage_probe.py now accepts `--probe fresh-translation-007`.

## Not done / limits

No game file was touched; 006 remains installed. No translation wording, font, UI, LF, token or tag changed. Segmentation is dictionary-based and structurally guarded; it is not a Thai-language review of every boundary (random review samples looked acceptable; compounds such as ปรับ|แต่ง were fixed through the extra-word list, residual cases such as เอ็ก|โท in two records remain). Whether TMP consumes U+200B identically in every container (rich-text styled runs, scrolling lists, VO captions) is untested. Any render of a visible glyph for U+200B would be a fail condition.

## Next

1. User (Windows, game closed): `python tools/build_fresh_translation_007.py`. Because 006 is installed, run `python tools/manage_probe.py restore --probe fresh-translation-006` → `check --probe fresh-translation-006` (all three `original`) → `install --probe fresh-translation-007` → `check --probe fresh-translation-007` (all three `probe`). The manager refuses any unknown installed hash, so a Steam update must be re-checked first.
2. WO-VISUAL-019 (docs/qa/WO_VISUAL_019.md): re-open the same two screens at Small and Medium and capture native frames; then a short regression sweep of the 006-verified screens (Settings > Game, Video tooltip, opening modal, the 15 ต่ำ/น้ำ sites).
3. Revert: close game, `python tools/manage_probe.py restore --probe fresh-translation-007` → `check` (all original) → `install --probe fresh-translation-006`.
