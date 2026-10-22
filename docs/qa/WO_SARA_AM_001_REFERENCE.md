# WO-SARA-AM-001-REFERENCE — offline comparison

2026-10-22. Antigravity visual QA. READY_FOR_HANDOFF, receipt not confirmed. No game launch, install, save edits or new defect reproduction.

Read ../SARA_AM_001_FINDINGS.md and BUG_THAI_003.md. Open local/review/sara-am-001/reference.html in a browser. This self-contained page uses the exact embedded Thai-capable font from fresh-translation-005, SHA256 f9855a702e9899b9cfa1e8cb7cbf36c2c7bb6fe31ee0cd6860ae61ae012155d0. Verify manifest hash and visible Font loaded: true before capture. If font loading cannot be confirmed, report INCONCLUSIVE, do not substitute a system font.

Compare atomic ต่ำ with two explicitly labeled decomposed diagnostic sequences and ถี่ regression/control samples. Record visible relative mark placement, overlap/separation, and differences between cases. Decomposed strings are diagnostic only, not permission to change localization Unicode. Compare with existing local/qa/BUG-THAI-003/user-native-evidence.png and local/qa/WO-FRESH-SMOKE-001-RESUME/02-campus-modal.png. Preserve originals; any crop/enlargement must be labeled with scale/interpolation and cannot prove native pixel equivalence. Different size/rendering engine prevents a pixel-equality claim.

Maximum 10 minutes, two new reference captures, no game captures. Do not claim browser result proves TMP behavior, actual game font binding, engine deficiency or a fix. If atomic reference is separated while user evidence collides, record that comparison and limits; do not mark BUG-THAI-003 resolved. Do not modify font, game files or reference page. No network uploads, commit or push.

Deliver docs/qa/WO_SARA_AM_001_REFERENCE_REPORT.md with captures under local/qa/WO-SARA-AM-001-REFERENCE/. Include browser/version, zoom, font-ready evidence, hashes, case/codepoints, actual placement observations and comparison limits. Verdict REFERENCE_ESTABLISHED / INCONCLUSIVE. Stop after report for Controller review.
