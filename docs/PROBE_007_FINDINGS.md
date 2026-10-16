# Tag-free English control build and binding scan

Date: 2026-10-16. Two variants built/reloaded; not installed. Original installed bundle hashes verified.

tools/build_probe_007.py scans direct string fields in two UI bundles. Four Resolution-related components were found in ui-prefabs-general (localisation terms and text), but no complete runtime tooltip binding established. One MonoBehaviour could not be fully read (476 expected vs 352 bytes); its exact ID/error is retained in reports/settings-tooltip-binding-scan.json. The scan is deliberately incomplete and not evidence that binding is absent.

probe-007-short reuses the original English Resolution tooltip with probe-003 fonts and other pilot content. It changes zero source segments relative to probe-003. probe-007-long changes only the middle line of that one tooltip. Reload checks verify all other TextAssets/segments unchanged, two LF separators and no markup. Both fonts remain byte-identical to probe-003. This controls text length, not runtime width.

WO-VISUAL-007 first verifies the short three-line baseline, then (only if readable) tests the long middle segment. This separates the prior rich-text-width experiment from ordinary preferred-size/layout behavior. Any English automatic wrapping must be observed, not assumed from asset settings. No further broad menu scan or Thai A/B is requested.
