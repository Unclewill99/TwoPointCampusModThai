# Probe-003 — serialized font-feature experiment

Date: 2026-10-15. Status: BUILT / RELOAD CHECKED / NOT INSTALLED / RUNTIME NOT_RUN.

Campus's reused dynamic TMP slot has empty serialized feature tables. Museum's static NotoSans_Thai contains 1,677 mark-to-base and 357 mark-to-mark records, 1,734 pair adjustments and 9 ligature substitutions. These are observed asset contents, not proof of Campus runtime support.

Probe-003 copies the feature-table data into the existing probe-002 dynamic font slot. Both source feature asset and target slot have nominal point size 30, matching font units-per-em; the target's embedded TTF bytes exactly equal Museum's NotoSansThai-Medium source bytes. Referenced feature glyph IDs are within that font's glyph count. No face metrics, material, fallback graph, locale mapping or translation changes are made in this experiment.

Reload assertions verify the full inserted feature table and that every other field of the target TMP asset is unchanged. Localisation bundle is byte-identical to probe-002. Font-feature import was already disabled (m_ShouldReimportFontFeatures=0) and remains unchanged. Actual runtime application, glyph variant availability and font-feature enablement remain open questions. A failed/no-change visual outcome would not disprove the general need for Thai mark positioning; it would constrain this injection approach.

Same-font-reference.html is generated locally with the identical embedded TTF and 20 reference sections (bug phrase plus synthetic corpus). Pillow RAQM is unavailable on this machine, so no BASIC-layout raster is passed off as a shaped reference. Browser rendering and successful custom-font loading must be inspected by the visual tester before use as reference evidence. No reference screenshot has yet been verified.

WO: docs/qa/WO_VISUAL_003.md. This is a narrower experiment before synthetic in-game corpus injection, keeping the existing user-reported phrase as the controlled stimulus. All installed originals still pass hash verification. Keep generated bundles/embedded-font HTML local; no distribution approved.
