# Controller disposition — independent pilot QA

Date: 2026-10-15
Reviewed: docs/qa/PILOT_001_LINGUISTIC_REVIEW.md (original preserved).
Decision: Incorporate four naturalness edits in a new local r3 baseline. No further translator revision required at this stage. Not a production or runtime approval.

## Accepted changes

- AudioLanuuage: ภาษาเสียงพากย์, provisional for spoken-audio language selection. Verify actual setting scope; this is an editorial choice, not a universal game-UI standard or Critical defect.
- CameraShake: การสั่นของกล้อง, an optional nominal label. กล้องสั่น was understandable; both remain subject to UI-width QA.
- Advisor_Favourite_Student_Class_Complete and Class_Risk: เรียนจบคาบ replaces เรียนจบคาบเรียน, preserving tokens and line breaks.

## Deferred suggestions

- Keep ขุดแล้วเข้าใจไหม? for this prototype baseline. ขุดแล้วเก็ตไหม? remains a candidate, not a proven improvement or resolution of the joke.
- Keep ค่อย ๆ ขุด: ทำพังแล้วก็พลาดเลย; defer เสียของ wording until deciding whether the additional object-loss implication is desirable.
- Dating Algorithms retains the current age-determination wording. All three JOKE_UNRESOLVED flags remain.

## Qualifications on QA claims

Token integrity is structurally checked, not runtime substitution verified. The report's Critical/Moderate summary wording is inconsistent with its Moderate table entry; no Critical gameplay defect is established. Audio terminology and humor preferences are editorial suggestions. The proposed 1970s-slang origin and specific idiom/romantic interpretations have not been independently established and are not acceptance evidence. The source English Audio Language has no typo; the internal key AudioLanuuage does. Recruitment Fee does not itself translate Staff, so it does not establish G003 glossary compliance. Plural branch switching remains unknown.

## Baseline and remaining work

New baseline: local/translations/PILOT-001.th.r3.json. r1 and r2 retained. tools/integrate_pilot_qa.py records exactly the four selected changes; reports/pilot-001-r3-validation.json records the structural check and reviewed input hash. Original translation status and unresolved flags remain; do not interpret them as production approval.

Antigravity need not repeat the complete linguistic review before prototype testing. Additional linguistic work is limited to new evidence or changed strings. Runtime tests remain NOT_RUN. Controller now prioritizes Museum font mapping, the Campus font-loading path, reversible import and a rendering prototype.
