# WO-VISUAL-004 — synthetic Thai diagnostic coverage

Date: 2026-10-16. Controller: ChatGPT. Target: probe-004.

## Goal

Inspect broader mark positioning and observe Thai wrapping without loading gameplay. probe-004 keeps probe-003 fonts byte-identical and replaces 12 Settings label/tooltip strings with synthetic diagnostics. These are not translations or new menu meanings. All cases begin NOT_RUN.

## Read and preflight

Use the ThaiCampusMod project root. Read local/prototype/probe-004/diagnostic-map.json, manifest.json, docs/qa/CONTROLLER_ACCEPTANCE.md and docs/PROBE_003_ACCEPTANCE.md. Exact text, code points, keys and location hints are in the map. Verify map SHA-256 against diagnostic_map_sha256 in manifest before execution. Stop if mismatched.

Confirm real Windows game/screenshot access. With Campus closed, run `python tools/manage_probe.py check --probe probe-004`; both must be original. No force-closing unsaved gameplay, branch switching, code/translation edits or commit/push.

## Reference

Use local/prototype/probe-003/same-font-reference.html. It embeds the same font and corpus. Verify custom face loading from the existing visible evidence panel, record browser zoom, and save inspected reference images for the cases tested. If the panel/page is unavailable or local URL access is refused, ask the user to open it; do not bypass a tool security refusal. Mark reference conformance BLOCKED until evidence exists; game observations can still be recorded separately.

Some game labels are shortened corpus subsets; compare only matching glyph sequences. DESC groups are diagnostic combinations, not necessarily real words. Compare with the same-font reference rather than demanding a universal descender or vertical offset rule. Literal reference tags/placeholders are not game parser tests.

## Install and inspect

With game closed:

```
python tools/manage_probe.py install --probe probe-004
python tools/manage_probe.py check --probe probe-004
```

Both must be probe. Launch normally via Steam; English and Medium UI Scale, retain current resolution. No save loading, no resolution changes or Apply.

1. Game page: inspect Language label (tone marks without upper vowels), Audio Language label (standard sara am), Game Autosave label (MALFORMED input), Career Autosave label (decomposed sara am). Their contents deliberately differ from menu functions. Record each exact mapped case, clipping, glyph loss and mark placement. Do not alter autosave/language values accidentally.
2. Controls: inspect four camera sensitivity labels for ascenders, stacked marks, ญ/ฐ lower marks and ฎ/ฏ lower marks. Do not move sensitivity sliders. Capture full screens plus unmodified-source crops if useful; record crop and scaling method.
3. Video: hover Resolution, Fullscreen Mode, VSync and Antialiasing Mode labels/control areas for mapped synthetic tooltips. Do not click/apply settings. If a tooltip does not appear, mark BLOCKED; do not invent a screen location or require code changes mid-test. Record actual tooltip bounds, line breaks and whether leading vowels/combining marks are stranded. No assertion of dictionary-based breaking from one screenshot.
4. Resolution tooltip is the unmodified Thai paragraph; Fullscreen tooltip is the ZWSP variant with the same underlying text. Different containers may differ in width, so this is observational coverage, not a controlled width-matched A/B experiment. Record ZWSP glyph artifacts if present; no production ZWSP approval follows.
5. Check closed/open dropdown values still display. Restart once and repeat a representative valid stacked-mark and lower-mark case. Inspect Small/Large labels if safe; return Medium. Cold restart is not proof of cleared persistent cache. Do not claim atlas stress coverage from these visits alone.

## Results and limits

For each mapped case report display observed, reference available, mark/layout outcome, screenshot and status. Full-case PASS requires all relevant glyphs visible with supported comparison; a clipped diagnostic is not a shaping PASS. Distinguish test-container clipping from glyph positioning failure. MALFORMED and decomposed cases are diagnostic observations: report what happened without requiring automatic normalization. Do not modify text to make it pass. Matrix cases not injected or only partially represented remain NOT_RUN/partial coverage.

If valid upper/lower marks overlap, capture exact sequence/key and report FAIL. If the probe fails to load, gather evidence and restore rather than patching more files.

## Restore and delivery

Quit normally:

```
python tools/manage_probe.py restore --probe probe-004
python tools/manage_probe.py check --probe probe-004
```

Both must be original; retain backups. Save inspected images and command outputs under local/qa/WO-VISUAL-004/. Write docs/qa/WO_VISUAL_004_REPORT.md with build/manifest hashes, diagnostic-map hash, environment/actual UI scale, per-case observations, reference/zoom evidence and final restoration. Do not upload bundles/fonts or the embedded-font reference to GitHub. No important-save writes or permanent installation.
