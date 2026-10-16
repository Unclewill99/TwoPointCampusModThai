# Probe-004 — synthetic diagnostic build

Date: 2026-10-16. BUILT / RELOAD VERIFIED / NOT INSTALLED. Runtime NOT_RUN.

tools/build_probe_004.py derives from the accepted probe-003 font-feature experiment. Font bundle remains byte-identical. Only 12 unique Settings TextAsset segments change; all other segments and TextAssets compare equal after reload. Source/pilot translation files remain intact. Map with exact text, code points, locations, corpus IDs and zero-based ZWSP offsets stays in local/prototype/probe-004/diagnostic-map.json; its hash is in the manifest and reports/probe-004-build.json.

Coverage: four Controls labels for ascender/upper marks, stacked marks and two lower-mark groups; four Game labels for no-upper-vowel tones and standard/malformed/decomposed sara am; four candidate Video tooltips for unmodified/ZWSP/leading-vowel paragraphs and mixed-script text. UI slot visibility and actual tooltip wiring still require runtime confirmation. Short subsets are explicitly labelled in the map and do not pass entire corpus cases.

This experiment does not alter runtime parsers or prove plural/argument semantics. It is not a translation build. Tooltip containers may have different widths, so ZWSP comparison is observational pending a controlled same-container experiment. Use the previously generated same-font reference only after confirming browser loading/zoom. Full glyph substitution, atlas stress and universal Thai correctness remain unapproved.

Work order: docs/qa/WO_VISUAL_004.md. Current originals independently checked unchanged after staging. No game installation performed by Controller.
