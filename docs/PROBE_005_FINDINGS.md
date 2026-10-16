# Probe-005 — same-slot text-width experiment

Date: 2026-10-16. Three local variants built and reloaded; none installed. Original game hashes verified. Runtime status NOT_RUN.

The exact-match reference page for the two probe-004 partial cases is generated at local/qa/references/WO-VISUAL-005/exact-reference.html. It embeds the same TTF but avoids the fixed evidence overlay. Successful page generation is not a reference comparison PASS; browser face loading/zoom and visual inspection remain required.

Each of probe-005-control, probe-005a and probe-005b derives from probe-003, changing exactly one Settings segment: UI/Settings/Tooltips/Resolution. All other TextAssets/segments are verified unchanged on reload and font bytes are identical. Control uses spaced English; A/B use twice-repeated underlying Thai text, with only U+200B differences. No manual newlines. Per-variant manifests and exact input maps remain local; build metadata is reports/probe-005-build.json.

The `<width=400>` wrapper is an experimental way to request reduced text width without editing game prefabs. Unity's TMP documentation describes the width tag and restoring width with its closing tag: https://docs.unity.cn/Packages/com.unity.textmeshpro%402.2/manual/RichTextWidth.html . This documentation does not establish the game's runtime configuration, wrapping flag, tag parsing or resulting container width. English control must first demonstrate usable multiple lines. Equal runtime widths/font scales must then be checked before causal A/B claims.

If tag parsing or wrapping is disabled on this path, stop at control and investigate a genuine bounded/wrapping-enabled game text component next. Do not infer a Thai-specific failure from failed control. No release changes or invisible-character policy changes are approved.
