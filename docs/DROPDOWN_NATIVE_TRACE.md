# Dropdown native trace — 2026-10-21

Read-only investigation after WO-DROPDOWN-001 STILL_BLANK. No game execution.

## Established static path

TPC.PreferencesPanelGame::RefreshDropdownOptions at 0x1809E6560 builds LocalizedDropDownOptionDataWithID instances from serialized LocalisedString values. Serialized PreferencesPanelGame object 4789405553745755865 links LogLevel dropdown -6663759905669087527 and five configured option term IDs. IDs include Verbose -1492060410, Debug -426483460, Information -797548384, Warning -163356015, Error -1932900526.

LocalizedDropDownOptionDataWithID constructor 0x1812CBC90 copies the LocalisedString structure to option+0x38 and ID to +0x30. get_text at 0x180DD9A00 is a 3-instruction tail stub: add rcx,0x38; xor edx,edx; jmp 0x182B20B20. This leaf has no exact unwind entry; inspected only its first terminating jump, not treated as an unwind-validated function body.

TPS.Core.Localisation.LocalisedString::get_Translation at 0x182B20B20 reads numeric term ID at structure+8 and calls the integer overload I2.Loc.LocalizationManager::TryGetTranslation at 0x183EA33B0. That overload calls LanguageSourceData::GetTermData with the numeric ID. Runtime null fallback paths exist; these listings do not show which path the live game takes.

TMPro.TMP_Dropdown::RefreshShownValue at 0x182C007F0 selects an option, obtains text through virtual calls and supplies the result to the caption text setter (virtual dispatch at 0x182C00B27). A null-option/text branch supplies an empty/default string. The inspected slice does not perform direct font assignment; other lifecycle code may do so. No assertion that runtime font overrides are absent.

Listings remain local under local/tools/native-inspection/. Existing disassembler used PE exception/unwind bounds for non-leaf methods; shared names/overloads can overwrite generic listing filenames, so integer TryGetTranslation listing is preserved separately as dropdown-numeric-lookup.asm.txt. Static evidence is not live instrumentation.

## Next discriminating control

community-merge-004 derives from merge-002 (not the unsuccessful direct-font merge-003). Change exactly six LogLevel localisation option values to ASCII CHECK + original English. Other localisation segments/objects, UI and fonts identical to merge-002; reload comparison confirms isolation. Covers all source LogLevel options because current selection cannot be read from the blank box. Does not change stored settings, option keys, term IDs or selection order.

If CHECK appears, imported option text reaches this caption and ASCII can render there; investigate Thai-specific processing/rendering next. If blank persists, do not blame Thai glyph coverage alone: inspect population, term lookup, prefab instance/caption state and resource loading. If different unmarked text appears, candidate/key targeting is unresolved. No branch alone proves a universal root cause.

Read-only manager check for merge-004 passes, three installed originals. NOT_RUN; not a fix or production candidate. One-view test in qa/WO_DROPDOWN_002.md.
