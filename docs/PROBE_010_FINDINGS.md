# Wrapping-mode evidence and candidate experiment

Date: 2026-10-16. Build/reload/preflight passed; no installation.

Local Campus IL2CPP metadata header version is 27 and includes Unity.TextMeshPro.dll, TextWrappingModes, NoWrap and PreserveWhitespaceNoWrap strings. This identifies relevant names but not numeric enum values or exact package version. Official TMP 4.0.0-pre.2 documentation lists Normal, NoWrap, PreserveWhitespace and PreserveWhitespaceNoWrap, but its value cells are blank: https://docs.unity3d.com/Packages/com.unity.textmeshpro@4.0/api/TMPro.TextWrappingModes.html . Do not substitute unrelated UIElements.WhiteSpace or legacy HorizontalWrapMode enums.

Exact numeric mapping remains unresolved. Instead of claiming a verified enable flag, probe-010 tests raw m_TextWrappingMode 1 to 0 as an explicit hypothesis. Only one field in TMP object 2671690608638065206 changes. Reload verification checks the entire object and all UI object payloads: no other modifications. UI starts from original, not probe-008's width edits or probe-009's colour marker. Long English localisation/font bytes match probe-007-long. Existing positive-marker evidence supports this serialized path being consumed, not this field's runtime semantics.

The build is a reversible candidate experiment, not a known fix. Original fitter/layout/rect settings remain; absence of improvement may require either actual enum decoding, effective-width instrumentation or verified paired constraints. WO-VISUAL-010 permits only this single-factor run. All three original hashes independently verified before handoff.
