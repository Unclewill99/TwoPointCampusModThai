# Controller disposition — tooltip linguistic QA

Date: 2026-10-16. Original QA report preserved. Selected eight wording edits into NEW local/translations/TOOLTIPS-001.th.r2.json, retaining r1 and all source fields/flags. Independent structural validator passes all 20 with zero errors; exact hash in reports/tooltips-001-r2-validation.json. r2 accepted for visual-build preparation, not release/runtime approval.

## Selected changes

FullScreenMode uses เลือกโหมดการแสดงผล. Resolution uses กำหนดความละเอียดการแสดงผลของเกม (editorial clarity, not a verified claim about every display mode). WorldDetail uses ฉาก provisionally. AmbientOcclusionModeQuality, AnimationSkinningQuality and ShadowQuality use smoother comparative phrasing; QualityPresets removes the ต่ำลงลด repetition; MSAASamples explicitly says ลดจำนวนลง. Other optional style rewrites are not required.

Preserve all nine AMBIGUOUS flags. MaxFPS/VSync interaction remains unverified; no behavior rewrite. No global glossary promotion. Do not add “อาจ” to the low-quality visual claim where source states it directly; retain existing uncertainty only where supported. No ZWSP/manual-LF changes.

## Qualifications to QA report

Assertions that Resolution affects every mode and the exact FullScreenMode option list are not established by this linguistic review. Treat as contextual questions until direct evidence is cited. “source bytes verbatim” should be understood as decoded structural whitespace preservation, not a verified serialized-byte roundtrip of the translation. The note citing WO-008 as the latest width outcome is stale: WO-011 subsequently demonstrated bounded English wrapping, and WO-012 demonstrated scoped Thai wrapping. Neither establishes all real-tooltip scale behavior.

Next: integrate these actual translations with pilot r3 and the experimental bounded layout into a separately checked candidate, then issue Small/Medium/Large visual coverage. CharacterLimits variable substitution remains a separate runtime concern; source presence is not proof that its tooltip can be activated. No additional translator rewrite requested now. All three installed originals independently checked; no new build or installation in this review.
