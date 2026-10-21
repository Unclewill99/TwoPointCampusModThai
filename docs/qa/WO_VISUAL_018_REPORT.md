# WO-VISUAL-018 QA Report: Reviewed Maps at 800 Width (Screening Run)

- **Date:** 2026-10-21
- **Status:** COMPLETED (Screening Scope)
- **Active Scope Revision:** 2026-10-21 (probe-018-800a vs probe-018-800b at Medium UI Scale; probe-018-600 series DEFERRED)
- **Target Game:** Two Point Campus (Steam AppID 1649080)
- **Runtime Environment:**
  - Game Build: `10.3.169253+2024-12-06.1241`
  - Display: Full Screen Window, 3840x2160 (LANCZOS downsampled to standard 1920x1080 capture space)
  - UI Scale: Medium
  - Language: English (mod target)

---

## 1. Input & Lifecycle Verification

Both candidate variants were verified against their frozen manifests and diagnostic maps before installation. After each run, files were completely restored to their original state and independently verified via `tools/manage_probe.py check`.

- **probe-018-800a Input Verification:** [01-input-verification.json](../../local/qa/WO-VISUAL-018/probe-018-800a/01-input-verification.json) (All 3 bundles verified)
- **probe-018-800b Input Verification:** [01-input-verification.json](../../local/qa/WO-VISUAL-018/probe-018-800b/01-input-verification.json) (All 3 bundles verified)
- **Font & UI Prefab Identity:** Fonts (`fonts_assets_all.bundle`) and UI Prefabs (`ui-prefabs-general_assets_all.bundle`) are byte-for-byte identical between 800a and 800b. Variant B differs strictly by reviewed U+200B marks in localisation text.
- **Restoration State:** All three game bundles (`fonts_assets_all.bundle`, `localisation_assets_localisationenglish.bundle`, `ui-prefabs-general_assets_all.bundle`) are confirmed in **`original`** state.

---

## 2. Results Matrix

Per the active scope revision dated 2026-10-21, exactly 4 cells across two runs were executed. The 600 width candidate series was deferred.

| Probe Variant | UI Scale | Key (`UI/Settings/Tooltips/`) | Observed Lines | Primary Capture Evidence | Cell Status |
|---|---|---|:---:|---|---|
| **probe-018-800a** (Baseline A) | Medium | `MSAASamples` | 2 | [07-A-MSAASamples.jpg](../../local/qa/WO-VISUAL-018/probe-018-800a/07-A-MSAASamples.jpg) | BASELINE_OBSERVED |
| **probe-018-800a** (Baseline A) | Medium | `WorldDetail` | 4 | [10-A-WorldDetail.jpg](../../local/qa/WO-VISUAL-018/probe-018-800a/10-A-WorldDetail.jpg) | BASELINE_OBSERVED |
| **probe-018-800b** (Marked B) | Medium | `MSAASamples` | 2 | [07-B-MSAASamples.jpg](../../local/qa/WO-VISUAL-018/probe-018-800b/07-B-MSAASamples.jpg) | PASS (Break Active) |
| **probe-018-800b** (Marked B) | Medium | `WorldDetail` | 4 | [10-B-WorldDetail.jpg](../../local/qa/WO-VISUAL-018/probe-018-800b/10-B-WorldDetail.jpg) | PASS (Clean Match) |
| *probe-018-600a* | Medium | `MSAASamples` | - | - | **DEFERRED** |
| *probe-018-600a* | Medium | `WorldDetail` | - | - | **DEFERRED** |
| *probe-018-600b* | Medium | `MSAASamples` | - | - | **DEFERRED** |
| *probe-018-600b* | Medium | `WorldDetail` | - | - | **DEFERRED** |

---

## 3. Visual & Text Breakdown

### Key 1: `UI/Settings/Tooltips/MSAASamples`
- **Source text:** `เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก` (0 source LFs)
- **probe-018-800a (Baseline A):**
  - Line 1: `เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก `
  - Line 2: `หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก`
  - *Break location:* Broke at the space character after `เพื่อลดรอยหยัก`.
- **probe-018-800b (Marked B):**
  - Line 1: `เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก หรือลดจำนวน`
  - Line 2: `ลงเพื่อเพิ่มประสิทธิภาพกราฟิก`
  - *Break location:* Broke at underlying codepoint offset 50 (between `หรือลดจำนวน` and `ลงเพื่อ...`).
  - *Alignment with diagnostic map:* Offset 50 is an exact member of `proposed_cut_offsets` in `diagnostic-map.json`.
  - *Evaluation:* Unity UI actively exercised the inserted ZWSP opportunity. The line broke at a natural word boundary without any internal word splits, orphan vowels, or missing-glyph boxes.

### Key 2: `UI/Settings/Tooltips/WorldDetail`
- **Source text:** `เลือกระดับรายละเอียดโดยรวมของฉาก\nระดับรายละเอียดฉากที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น\nเลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก` (2 source LFs)
- **probe-018-800a (Baseline A):**
  - Line 1: `เลือกระดับรายละเอียดโดยรวมของฉาก` (Source LF)
  - Line 2: `ระดับรายละเอียดฉากที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมอง` (Runtime automatic break)
  - Line 3: `ที่ไกลขึ้น` (Source LF)
  - Line 4: `เลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก`
- **probe-018-800b (Marked B):**
  - Line 1: `เลือกระดับรายละเอียดโดยรวมของฉาก` (Source LF)
  - Line 2: `ระดับรายละเอียดฉากที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมอง` (Runtime automatic break)
  - Line 3: `ที่ไกลขึ้น` (Source LF)
  - Line 4: `เลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก`
  - *Break location:* Runtime automatic break occurred at offset 87 (between `ระยะมอง` and `ที่ไกลขึ้น`), matching proposed cut offset 87.
  - *Evaluation:* Exactly identical line breaking to Baseline A. Zero visual regressions, no word splits, and perfect containment within the tooltip container.

---

## 4. A/B Comparative Conclusion

**Screening Verdict:** `BENEFIT_OBSERVED`

**Summary Assessment:**
1. **Active ZWSP Adoption:** In `MSAASamples`, the game engine actively honored the reviewed zero-width break opportunity at offset 50 (`หรือลดจำนวน` | `ลง`), breaking later and packing more text onto the first line than baseline A without word fragmentation.
2. **Zero Rendering Regressions:** No missing-glyph boxes, detached upper/lower vowels, stranded tone marks, or box-overflow defects were observed in either key for probe-018-800b.
3. **WorldDetail Consistency:** In `WorldDetail`, the line wrapping matched the clean baseline break at offset 87, demonstrating stability across source LFs and automatic wrapping.

---

## 5. Unresolved Points & Scope Limits

1. **600 Width Untested:** The 600 width series (`probe-018-600a`, `probe-018-600b`) remains untested and recorded as `DEFERRED` per the 2026-10-21 active revision. A second effective width factor is not yet established.
2. **Single Scale Only:** Only Medium UI Scale was screened; behavior at Small and Large UI Scales remains unobserved for probe-018.
3. **Screening Purpose Only:** This result supports the viability of explicit reviewed break opportunities in Unity UI, but does not authorize automatic production ZWSP deployment, global width changes, or bug closure.

---

## 6. Restoration Verification

```json
{"action": "check", "files": [
  {"name": "fonts_assets_all.bundle", "state": "original"},
  {"name": "localisation_assets_localisationenglish.bundle", "state": "original"},
  {"name": "ui-prefabs-general_assets_all.bundle", "state": "original"}
]}
```
*Confirmed: Two Point Campus game files are 100% clean and restored to original state.*
