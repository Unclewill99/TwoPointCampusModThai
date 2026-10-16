# WO-VISUAL-010 — one-field wrapping-mode candidate

Date: 2026-10-16. Target probe-010. Read reports/probe-010-build.json and manifest. This changes only traced TMP m_TextWrappingMode raw 1 to 0 versus original UI, with probe-007-long's identical English input/fonts. No fixed-width edit or magenta marker included. Numeric enum interpretation remains unverified; grade observed behavior, not assumed mode semantics.

With Campus closed normally, run from project root:

```
python tools/manage_probe.py check --probe probe-010
python tools/manage_probe.py install --probe probe-010
python tools/manage_probe.py check --probe probe-010
```

Require originals for all THREE before install, probe for all THREE afterward. Launch through Steam, English/Medium, resolution unchanged. No gameplay/save load or Apply/settings changes. Hover Settings > Video > Resolution at the same position as WO-007; capture full readable tooltip and compare existing 17-long-tooltip.jpg. Record actual visible bounds, complete/partial lines, clipping, blankness and glyph scale. Determine whether any extra break occurs within the newline-free repeated middle source segment (local/prototype/probe-007-long/diagnostic-map.json).

Do not claim automatic-wrap PASS from a shorter box alone. If multiple readable lines appear, record exact line starts/ends and whether all original first/middle/last segments are present. If unchanged, report NO OBSERVED IMPROVEMENT, not proof that enum has no effect in all contexts. If single-field patch fails to constrain width, do not combine patches or change values during testing.

Inspect original Antialiasing tooltip separately for shared-path regressions; label its image with actual content. No need to chase Quality Presets again. This is English only; no Thai, dictionary or ZWSP conclusion.

Quit normally, then:

```
python tools/manage_probe.py restore --probe probe-010
python tools/manage_probe.py check --probe probe-010
```

Require ALL THREE original, backups retained. Stop/report any failure. Save inspected images and exact outputs in local/qa/WO-VISUAL-010/; write docs/qa/WO_VISUAL_010_REPORT.md with hashes, actual environment, comparison and restoration. No branch switch, commit/push, code/translation edits, loader installation, force-close or asset uploads.
