# Sara am â€” native/feature investigation 002

2026-10-22. No game input, asset changes or installed probe.

Exact embedded font GPOS MarkToMark lookup contains base glyph59 (uni0E4D) to combining glyph42 (uni0E48), while serialized TMP feature table has no such pair. Font units: base anchor (-115,772), tone anchor (-86,536); unitsPerEm1000 at TMP point30 implies anchors (-3.45,23.16) and (-2.58,16.08). Evidence reports/sara-am-native-feature-audit.json. This is an exact missing imported pair, not merely an empty MultipleSubstitution table.

Native symbol UpdateGSUBFontFeaturesForNewGlyphIndex resolves to a shared RET entry (bytes C2 00 00, RET with zero stack adjustment). Dedicated initialization methods lack exact unwind bounds in existing decoder and were not decoded speculatively. SetArraySizes listing generated successfully; GenerateTextMesh existing listing contains mark-adjustment getter calls. These facts do not prove a complete GSUB/shaping absence or runtime control flow.

Two unresolved mechanisms must be separated: atomic U+0E33 decomposition/reordering, and mark placement once separate nikkhahit exists. Injecting missing (59,42) alone may have no effect on atomic à¸•à¹ˆà¸³ if glyph82 remains composite. Conversely a diagnostic decomposed sequence may reveal placement differences but is not an approved corpus rewrite. Do not claim a font-feature-only fix before testing both questions.

Current blockers to a well-controlled runtime experiment: actual opening-modal font binding still not established, and atomic glyph processing not traced completely. Generic popup font references from investigation001 are candidates only. No new candidate/WO issued merely to rerun the defect. Existing same-font browser reference accepted; no repeated reference capture needed. BUG-THAI-003 remains OPEN.

Next: resolve modal provider from native metadata/type field relationships rather than prefab name searches; then design isolated atomic/decomposed diagnostic and exact-pair feature variants without altering frozen corpus or global glyph geometry. Antigravity owns screen execution; Controller owns staging and structural checks.
