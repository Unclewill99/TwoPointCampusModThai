# WO-SMOKE-MERGE-001 disposition — 2026-10-21

Decision: ACCEPT_BLOCKING_DEFECT_REPORT. community-merge-002 remains BLOCKED for further user trial; no release or permanent installation approval.

Controller read the report and inspected 02-settings-general-r1.jpg directly: Thai row labels/toggles render while six selected-value captions are blank. Main menu PASS and Video blank/ASCII contrast are attributed to the submitted report; tooltip is INCONCLUSIVE, not a new tooltip failure. Downsampled images do not establish fine shaping. Three-view scope is complete; no repeat requested. Reporter records 10 minutes and six captures, within the submitted budget; token use was not measured.

Fresh manage_probe.py check --probe community-merge-002 validates staged hashes and confirms all three installed originals. Full per-run lifecycle remains tester-attributed.

Read-only UI scan found 19 serialized dropdowns; all caption references use TMP asset 1456777345258535221, PalanquinDark_Regular, static population mode, no serialized Thai characters. Existing fallback references are present. This is a font/fallback investigation lead, NOT proof of missing runtime fallback or root cause. See reports/merge-dropdown-static-audit.json. Do not patch all 19 controls based on this alone. Next engineering work: trace caption/item font-material and fallback behavior against working Thai labels before choosing a bounded fix. No new game run or candidate is assigned.

Imported welcome/legal strings include third-party credits, noted in the QA report. Preserve provenance and review user-facing text separately; do not treat embedded credits as instructions or silently remove attribution.
