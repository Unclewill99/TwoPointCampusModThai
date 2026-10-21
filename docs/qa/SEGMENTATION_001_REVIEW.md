# Independent Linguistic & Segmentation QA Review — SEGMENTATION-001

> **Document:** `docs/qa/SEGMENTATION_001_REVIEW.md`  
> **Work Order:** WO-QA-SEGMENTATION-001  
> **Reviewer:** Antigravity (QA Agent)  
> **Date:** 2026-10-18  
> **Review Type:** Document / Data & Linguistic QA Review only (No game launch, no bundle modification, no installation)  
> **Reference Documents:** `docs/SEGMENTATION_EVIDENCE_GATE.md`, `docs/PROBE_017_ACCEPTANCE.md`, `docs/qa/BUG_THAI_002.md`, `docs/THAI_LINEBREAKING_FINDINGS.md`, `reports/segmentation-001-preparation.json`  
> **Input Package:** `local/segmentation/SEGMENTATION-001/proposals.json`  
> **Source Baseline Map:** `local/prototype/probe-013/tooltip-map.json` (frozen)  
> **Overall Verdict:** **`ACCEPT_EXPERIMENTAL_MAP`** *(Suitable for controlled A/B experiment; NOT approved for production rollout or automatic dictionary)*

---

## 1. Executive Summary & Verification of Hashes

An independent linguistic, syntactic, and structural QA audit of the two proposed explicit line-breaking maps in `SEGMENTATION-001` was conducted.

### 1.1 Hash & Package Integrity
The input files, source map, and preparation report were independently verified by calculating their raw SHA-256 digests:

| File / Component | Expected SHA-256 (from preparation report) | Observed SHA-256 (Independently Computed) | Match Status |
| :--- | :--- | :--- | :---: |
| `proposals.json` | `883a24a3ff425e8ec16431b031adf9c9943b5750d20d9959a6b783008c7ceddd` | `883a24a3ff425e8ec16431b031adf9c9943b5750d20d9959a6b783008c7ceddd` | **PASS** |
| `tooltip-map.json` (probe-013) | `81d596fed3d94cfff34b011fdd5c42e46a7127bf9cfd998759920000b9953fda` | `81d596fed3d94cfff34b011fdd5c42e46a7127bf9cfd998759920000b9953fda` | **PASS** |
| `MSAASamples` Thai text hash | `d4edde11ed83def773bf0e13eef3ac0ff7fe138d625f4fdcc970f06cc7342f27` | `d4edde11ed83def773bf0e13eef3ac0ff7fe138d625f4fdcc970f06cc7342f27` | **PASS** |
| `WorldDetail` Thai text hash | `b2a79d0d559f5a20baa77f9b7de9747684daf59ebf9bd87ceef02c29aa02c480` | `b2a79d0d559f5a20baa77f9b7de9747684daf59ebf9bd87ceef02c29aa02c480` | **PASS** |

### 1.2 Structural & Phonological Safeguard Audit
- **Reversal Equality:** Stripping only `\u200b` (Zero-Width Space) from `marked_text` reproduces the frozen baseline `text` verbatim for both records (`marked.replace('\u200b', '') == text`).
- **Whitespace & LF Preservation:**
  - `MSAASamples`: 0 LFs in source; 0 LFs in marked text; 4 natural ASCII spaces preserved at exact indices.
  - `WorldDetail`: 2 LFs in source; 2 LFs in marked text; 2 natural ASCII spaces around `CPU` preserved at exact indices.
- **Protected Run Integrity:** No cut falls inside or directly adjacent to protected Latin alphanumeric tokens (`MSAA`, `Samples`, `CPU`).
- **Phonological Cluster Guards:**
  - Zero cuts follow a Thai leading vowel (`เ`, `แ`, `โ`, `ใ`, `ไ`).
  - Zero cuts precede a combining mark (vowel signs, tone marks, or diacritics of Unicode category `M`).
  - Zero cuts are adjacent to existing ASCII whitespace or linefeed characters (`\n`).
  - Zero duplicate or unsorted cut offsets.
- **Fixture Verification:** `CharacterLimits` identity control validated; no breaks proposed, preserved strictly as an identity test fixture.

---

## 2. Per-Cut Linguistic Assessment: `UI/Settings/Tooltips/MSAASamples`

- **Key:** `UI/Settings/Tooltips/MSAASamples`
- **Source Thai:** `เพิ่มจำนวน MSAA Samples เพื่อลดรอยหยัก หรือลดจำนวนลงเพื่อเพิ่มประสิทธิภาพกราฟิก` (79 Unicode codepoints)
- **Natural Spaces:** 4 existing spaces (after `จำนวน`, between `MSAA` and `Samples`, after `Samples`, after `รอยหยัก`)
- **Proposed Cuts:** 10 non-whitespace insertion offsets

| Cut # | Codepoint Offset | Left Context (before cut) | Right Context (after cut) | Linguistic Boundary Type | Cluster / Phonological Check | Decision | QA Rationale |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **01** | **5** | `เพิ่ม` (`...พ-ิ-่-ม`) | `จำนวน` (`จ-ำ-น-ว-น...`) | Verb + Noun object (`เพิ่ม` \| `จำนวน`) | Consonant `ม` $\rightarrow$ Consonant `จ` | **ACCEPT** | Clean compound verb boundary. Both are independent dictionary words. |
| — | *10* | `จำนวน ` | `MSAA` | *Existing natural space* | Space boundary | *Natural* | Native space already breaks here; no insertion needed. |
| — | *23* | `Samples ` | `เพื่อ` | *Existing natural space* | Space boundary | *Natural* | Native space already breaks here; no insertion needed. |
| **02** | **29** | `เพื่อ` (`...พ-ื-่-อ`) | `ลด` (`ล-ด...`) | Preposition / Conjunction + Verb (`เพื่อ` \| `ลด`) | Consonant `อ` $\rightarrow$ Consonant `ล` | **ACCEPT** | Standard syntactic clause boundary ("in order to" + "reduce"). |
| **03** | **31** | `ลด` (`ล-ด`) | `รอยหยัก` (`ร-อ-ย-ห-ย-ั-ก...`) | Verb + Noun object (`ลด` \| `รอยหยัก`) | Consonant `ด` $\rightarrow$ Consonant `ร` | **ACCEPT** | Natural verb-object break. `รอยหยัก` is kept intact as an indivisible compound noun. |
| — | *38* | `รอยหยัก ` | `หรือ` | *Existing natural space* | Space boundary | *Natural* | Native space already breaks here; no insertion needed. |
| **04** | **43** | `หรือ` (`ห-ร-ื-อ`) | `ลด` (`ล-ด...`) | Conjunction + Verb (`หรือ` \| `ลด`) | Consonant `อ` $\rightarrow$ Consonant `ล` | **ACCEPT** | Conjunction boundary introducing alternative predicate. |
| **05** | **45** | `ลด` (`ล-ด`) | `จำนวน` (`จ-ำ-น-ว-น...`) | Verb + Noun object (`ลด` \| `จำนวน`) | Consonant `ด` $\rightarrow$ Consonant `จ` | **ACCEPT** | Direct verb-object boundary. |
| **06** | **50** | `จำนวน` (`...น`) | `ลง` (`ล-ง...`) | Noun object + Directional particle (`จำนวน` \| `ลง`) | Consonant `น` $\rightarrow$ Consonant `ล` | **ACCEPT** *(Optional)* | In the discontinuous verb construction `ลด...ลง`, breaking between noun and aspect particle is an optional sub-compound boundary. Valid for narrow containers. |
| **07** | **52** | `ลง` (`ล-ง`) | `เพื่อ` (`เ-พ-ื-่-อ...`) | Particle + Preposition (`ลง` \| `เพื่อ`) | Consonant `ง` $\rightarrow$ Leading vowel `เ` | **ACCEPT** | Major clause boundary. Cut precedes leading vowel `เ`, correctly placing `เพื่อ` at line start. |
| **08** | **57** | `เพื่อ` (`...พ-ื-่-อ`) | `เพิ่ม` (`เ-พ-ิ-่-ม...`) | Preposition + Verb (`เพื่อ` \| `เพิ่ม`) | Consonant `อ` $\rightarrow$ Leading vowel `เ` | **ACCEPT** | Standard clause boundary. Correctly precedes leading vowel `เ`. |
| **09** | **62** | `เพิ่ม` (`...พ-ิ-่-ม`) | `ประสิทธิภาพ` (`ป-ร-ะ...`) | Verb + Noun object (`เพิ่ม` \| `ประสิทธิภาพ`) | Consonant `ม` $\rightarrow$ Consonant `ป` | **ACCEPT** | Clean verb-object boundary. `ประสิทธิภาพ` is kept intact. |
| **10** | **73** | `ประสิทธิภาพ` (`...ภ-า-พ`) | `กราฟิก` (`ก-ร-า-ฟ-ิ-ก`) | Noun + Modifier noun (`ประสิทธิภาพ` \| `กราฟิก`) | Consonant `พ` $\rightarrow$ Consonant `ก` | **ACCEPT** | Standard compound noun boundary ("performance" + "graphics"). `กราฟิก` loanword preserved intact. |

---

## 3. Per-Cut Linguistic Assessment: `UI/Settings/Tooltips/WorldDetail`

- **Key:** `UI/Settings/Tooltips/WorldDetail`
- **Source Thai:** 3 lines separated by 2 `\n` characters (156 Unicode codepoints):
  - Line 0 (0–32): `เลือกระดับรายละเอียดโดยรวมของฉาก`
  - Line 1 (33–97): `ระดับรายละเอียดฉากที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น`
  - Line 2 (98–156): `เลือกการตั้งค่าที่ต่ำลงเพื่อเพิ่มประสิทธิภาพ CPU และกราฟิก`
- **Natural Spaces:** 2 existing spaces (surrounding `CPU` at indices 142 and 146)
- **Proposed Cuts:** 24 non-whitespace insertion offsets (5 in Line 0, 12 in Line 1, 7 in Line 2)

| Cut # | Codepoint Offset | Left Context (before cut) | Right Context (after cut) | Linguistic Boundary Type | Cluster / Phonological Check | Decision | QA Rationale |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| **Line 0** | | | | | | | |
| **01** | **5** | `เลือก` (`เ-ล-ื-อ-ก`) | `ระดับ` (`ร-ะ-ด-ั-บ...`) | Verb + Noun (`เลือก` \| `ระดับ`) | Consonant `ก` $\rightarrow$ Consonant `ร` | **ACCEPT** | Verb-object boundary. |
| **02** | **10** | `ระดับ` (`...ด-ั-บ`) | `รายละเอียด` (`ร-า-ย...`) | Noun + Noun modifier (`ระดับ` \| `รายละเอียด`) | Consonant `บ` $\rightarrow$ Consonant `ร` | **ACCEPT** | Clean compound noun break ("level" + "detail"). |
| **03** | **20** | `รายละเอียด` (`...ย-ด`) | `โดยรวม` (`โ-ด-ย-ร-ว-ม...`) | Noun + Adverbial modifier (`รายละเอียด` \| `โดยรวม`) | Consonant `ด` $\rightarrow$ Leading vowel `โ` | **ACCEPT** | Noun-modifier boundary. Precedes leading vowel `โ` cleanly. |
| **04** | **26** | `โดยรวม` (`...ร-ว-ม`) | `ของ` (`ข-อ-ง...`) | Modifier + Preposition (`โดยรวม` \| `ของ`) | Consonant `ม` $\rightarrow$ Consonant `ข` | **ACCEPT** | Prepositional phrase boundary. |
| **05** | **29** | `ของ` (`ข-อ-ง`) | `ฉาก` (`ฉ-า-ก...`) | Preposition + Noun (`ของ` \| `ฉาก`) | Consonant `ง` $\rightarrow$ Consonant `ฉ` | **ACCEPT** | Standard prepositional object boundary. |
| — | *32* | `ฉาก` | `\n` | *Source Linefeed* | Linebreak boundary | *Preserved* | Source LF preserved verbatim; no cut inserted. |
| **Line 1** | | | | | | | |
| **06** | **38** | `ระดับ` (`...ด-ั-บ`) | `รายละเอียด` (`ร-า-ย...`) | Noun + Noun modifier (`ระดับ` \| `รายละเอียด`) | Consonant `บ` $\rightarrow$ Consonant `ร` | **ACCEPT** | Compound noun break ("level" + "detail"). |
| **07** | **48** | `รายละเอียด` (`...ย-ด`) | `ฉาก` (`ฉ-า-ก...`) | Noun + Noun modifier (`รายละเอียด` \| `ฉาก`) | Consonant `ด` $\rightarrow$ Consonant `ฉ` | **ACCEPT** | Compound noun break ("detail" + "scene"). |
| **08** | **51** | `ฉาก` (`ฉ-า-ก`) | `ที่` (`ท-ี-่...`) | Noun + Relative pronoun (`ฉาก` \| `ที่`) | Consonant `ก` $\rightarrow$ Consonant `ท` | **ACCEPT** | Relative clause boundary. |
| **09** | **54** | `ที่` (`ท-ี-่`) | `สูงขึ้น` (`ส-ู-ง-ข-ึ-้-น...`) | Rel. Pronoun + Predicate Adj (`ที่` \| `สูงขึ้น`) | Tone mark `่` $\rightarrow$ Consonant `ส` | **ACCEPT** | Cut follows complete cluster `ที่` and precedes consonant `ส`. Tone mark intact. |
| **10** | **61** | `สูงขึ้น` (`...้-น`) | `จะ` (`จ-ะ...`) | Predicate + Auxiliary verb (`สูงขึ้น` \| `จะ`) | Consonant `น` $\rightarrow$ Consonant `จ` | **ACCEPT** | Major syntactic clause boundary. |
| **11** | **63** | `จะ` (`จ-ะ`) | `คง` (`ค-ง...`) | Auxiliary verb + Main verb (`จะ` \| `คง`) | Spacing vowel `ะ` $\rightarrow$ Consonant `ค` | **ACCEPT** *(Optional)* | Auxiliary-to-verb boundary. Both are separate lexical words; valid granularity for tight containers. |
| **12** | **65** | `คง` (`ค-ง`) | `รายละเอียด` (`ร-า-ย...`) | Verb + Noun object (`คง` \| `รายละเอียด`) | Consonant `ง` $\rightarrow$ Consonant `ร` | **ACCEPT** | Main verb-object boundary. `รายละเอียด` kept intact. |
| **13** | **75** | `รายละเอียด` (`...ย-ด`) | `ไว้` (`ไ-ว-้...`) | Noun object + Aspect particle (`รายละเอียด` \| `ไว้`) | Consonant `ด` $\rightarrow$ Leading vowel `ไ` | **ACCEPT** | Discontinuous verb construction (`คง...ไว้`). Precedes leading vowel `ไ` cleanly. |
| **14** | **78** | `ไว้` (`ไ-ว-้`) | `ใน` (`ใ-น...`) | Particle + Preposition (`ไว้` \| `ใน`) | Tone mark `้` $\rightarrow$ Leading vowel `ใ` | **ACCEPT** | Prepositional phrase boundary. Follows complete cluster `ไว้`, precedes `ใ`. |
| **15** | **80** | `ใน` (`ใ-น`) | `ระยะมอง` (`ร-ะ-ย-ะ-ม-อ-ง...`) | Preposition + Noun phrase (`ใน` \| `ระยะมอง`) | Consonant `น` $\rightarrow$ Consonant `ร` | **ACCEPT** | Prepositional object break. `ระยะมอง` kept intact as compound noun ("view distance"). |
| **16** | **87** | `ระยะมอง` (`...ม-อ-ง`) | `ที่` (`ท-ี-่...`) | Noun + Relative pronoun (`ระยะมอง` \| `ที่`) | Consonant `ง` $\rightarrow$ Consonant `ท` | **ACCEPT** | Relative clause boundary. |
| **17** | **90** | `ที่` (`ท-ี-่`) | `ไกลขึ้น` (`ไ-ก-ล-ข-ึ-้-น...`) | Rel. Pronoun + Predicate Adj (`ที่` \| `ไกลขึ้น`) | Tone mark `่` $\rightarrow$ Leading vowel `ไ` | **ACCEPT** | Precedes leading vowel `ไ` cleanly. `ไกลขึ้น` kept intact. |
| — | *97* | `ไกลขึ้น` | `\n` | *Source Linefeed* | Linebreak boundary | *Preserved* | Source LF preserved verbatim; no cut inserted. |
| **Line 2** | | | | | | | |
| **18** | **103** | `เลือก` (`เ-ล-ื-อ-ก`) | `การตั้งค่า` (`ก-า-ร-ต-ั-้-ง...`) | Verb + Noun object (`เลือก` \| `การตั้งค่า`) | Consonant `ก` $\rightarrow$ Consonant `ก` | **ACCEPT** | Verb-object boundary. `การตั้งค่า` kept intact as a single nominalized term. |
| **19** | **113** | `การตั้งค่า` (`...ค-่-า`) | `ที่` (`ท-ี-่...`) | Noun + Relative pronoun (`การตั้งค่า` \| `ที่`) | Spacing vowel `า` $\rightarrow$ Consonant `ท` | **ACCEPT** | Relative clause boundary. |
| **20** | **116** | `ที่` (`ท-ี-่`) | `ต่ำลง` (`ต-่-ำ-ล-ง...`) | Rel. Pronoun + Predicate Adj (`ที่` \| `ต่ำลง`) | Tone mark `่` $\rightarrow$ Consonant `ต` | **ACCEPT** | Relative clause predicate break. |
| **21** | **121** | `ต่ำลง` (`...ล-ง`) | `เพื่อ` (`เ-พ-ื-่-อ...`) | Predicate + Preposition (`ต่ำลง` \| `เพื่อ`) | Consonant `ง` $\rightarrow$ Leading vowel `เ` | **ACCEPT** | Major clause boundary. Precedes leading vowel `เ`. |
| **22** | **126** | `เพื่อ` (`...พ-ื-่-อ`) | `เพิ่ม` (`เ-พ-ิ-่-ม...`) | Preposition + Verb (`เพื่อ` \| `เพิ่ม`) | Consonant `อ` $\rightarrow$ Leading vowel `เ` | **ACCEPT** | Standard clause boundary. Precedes leading vowel `เ`. |
| **23** | **131** | `เพิ่ม` (`...พ-ิ-่-ม`) | `ประสิทธิภาพ` (`ป-ร-ะ...`) | Verb + Noun object (`เพิ่ม` \| `ประสิทธิภาพ`) | Consonant `ม` $\rightarrow$ Consonant `ป` | **ACCEPT** | Verb-object boundary. `ประสิทธิภาพ` kept intact. |
| — | *142* | `ประสิทธิภาพ ` | `CPU` | *Existing natural space* | Space boundary | *Natural* | Native space already breaks here; no insertion needed. |
| — | *146* | `CPU ` | `และ` | *Existing natural space* | Space boundary | *Natural* | Native space already breaks here; no insertion needed. |
| **24** | **150** | `และ` (`แ-ล-ะ`) | `กราฟิก` (`ก-ร-า-ฟ-ิ-ก`) | Conjunction + Noun (`และ` \| `กราฟิก`) | Spacing vowel `ะ` $\rightarrow$ Consonant `ก` | **ACCEPT** | Conjunction boundary ("and" + "graphics"). `กราฟิก` loanword preserved intact. |

---

## 4. Linguistic Quality & Compound Boundary Analysis

### 4.1 Evaluation of Invalid vs. Optional Cuts
- **Zero Invalid Cuts:** None of the 34 total proposed cuts splits an indivisible morpheme, divides a consonant cluster, separates a tone mark or combining mark from its base consonant, or cuts directly after a Thai leading vowel.
- **Optional Granularity Cuts:**
  - `MSAASamples` Offset 50 (`จำนวน` \| `ลง`): In the discontinuous verb construction `ลดจำนวนลง` ("decrease the count"), keeping `จำนวนลง` together is a stylistic preference, but treating `ลง` as an optional break point is linguistically valid and useful for narrow text containers.
  - `WorldDetail` Offset 63 (`จะ` \| `คง`): In formal typography, keeping auxiliary `จะ` with main verb `คง` (`จะคง`) is preferred; however, `จะ` and `คง` are distinct lexical words. As an optional opportunity, it poses no grammatical defect.
- **Indivisible Words Preserved Intact:**
  - `รอยหยัก` (7 codepoints) — kept intact (no cut at `รอย` \| `หยัก`).
  - `การตั้งค่า` (10 codepoints) — kept intact (no cut at `การ` \| `ตั้ง` \| `ค่า`).
  - `รายละเอียด` (10 codepoints) — kept intact in all 3 occurrences.
  - `ระยะมอง` (7 codepoints) — kept intact as a single technical compound ("view distance").
  - `ประสิทธิภาพ` (11 codepoints) — kept intact in both records.
  - `กราฟิก` (6 codepoints) — loanword kept intact in both records.

---

## 5. Contextual Value Beyond WO-017

These two candidates provide substantial experimental coverage that was not exercised in WO-016 / WO-017:

1. **Source-LF Preservation (`WorldDetail`):**
   - WO-016/017 tested a continuous single-paragraph text without linebreaks.
   - `WorldDetail` tests whether the experimental map preserves explicit author-defined paragraphs (`\n` at offsets 32 and 97) while allowing dynamic wrapping within lines 0, 1, and 2.
2. **Mixed Thai/English and Natural Spaces (`MSAASamples` & `WorldDetail`):**
   - WO-016/017 contained 100% Thai text with zero spaces.
   - `MSAASamples` tests line-breaking with an English Latin run (`MSAA Samples`) flanked by natural ASCII spaces.
   - `WorldDetail` tests line-breaking with an English acronym (`CPU`) flanked by natural ASCII spaces.
   - This provides critical evidence on whether Unity TMP correctly coordinates natural whitespace wrapping with U+200B zero-width break opportunities.
3. **Continuous Unspaced Clauses:**
   - Line 1 of `WorldDetail` contains 64 consecutive unspaced Thai codepoints (`ระดับรายละเอียดฉากที่สูงขึ้นจะคงรายละเอียดไว้ในระยะมองที่ไกลขึ้น`), providing an ideal real-world test for edge-split prevention under bounded widths.

---

## 6. Explicit Unresolved Linguistic & Runtime Ambiguities

1. **Terminology Ambiguity in `WorldDetail` (Unresolved from Prior Reviews):**
   - The word `ฉาก` (scene) was provisionally accepted in `probe-013` as a translation for `WorldDetail`.
   - The alternative `สภาพแวดล้อม` (environment) remains pending menu-label synchronization.
   - *QA Decision:* Selecting cut offsets does **not** resolve this terminology ambiguity. The break map operates strictly on the existing frozen wording.
2. **Experimental vs. Production Scope:**
   - This review assesses explicit, manually mapped break opportunities for a future controlled A/B experiment.
   - It does **not** endorse or evaluate any automatic dictionary, tokenizer library, or production pipeline change.
   - `BUG-THAI-002` remains **OPEN**.

---

## 7. QA Verdict & Recommendations

### Overall Verdict: **`ACCEPT_EXPERIMENTAL_MAP`**

### Summary of Verdict:
- The proposal package `SEGMENTATION-001` (`proposals.json`) matches all required baseline hashes and strict structural constraints.
- All 10 proposed cuts in `MSAASamples` and all 24 proposed cuts in `WorldDetail` represent linguistically sound, phonologically safe optional word/compound boundaries.
- No text rewriting, manual linefeeds, or source alterations are recommended.
- The map is accepted as experimental input for the upcoming 8-cell (2 texts × 2 widths × A/B variants) controlled experiment under the Segmentation Evidence Gate.
