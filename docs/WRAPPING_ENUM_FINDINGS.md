# Actual Campus wrapping enum constants

Date: 2026-10-16. tools/decode_wrapping_enum.py reads the installed IL2CPP v27 metadata, locates the unique TMPro.TextWrappingModes definition, its five fields (underlying value plus four members), and each member's signed Int32 default. Strict bounds, names/counts and known header checks are included. Exact metadata hash/indices/default offsets appear in reports/wrapping-enum-decoded.json.

| Member | Actual local constant |
|---|---|
| NoWrap | 0 |
| Normal | 1 |
| PreserveWhitespace | 2 |
| PreserveWhitespaceNoWrap | 3 |

This is stronger build-specific evidence than inferring numeric values from another package's documentation order. Original traced tooltip m_TextWrappingMode=1 corresponds to Normal in this build. Probe-010's 1 to 0 candidate therefore requests NoWrap; it did not test enabling Normal. Its no-improvement result is preserved, but must not be interpreted as a failed enable-wrapping fix. Earlier explicit statements that numeric mapping was unknown remain historical, superseded by this decoding.

Normal being serialized does not establish actual runtime mode, bounded text width or automatic wrapping. The colour marker confirms consumption of this TMP path, not every property surviving runtime overrides. Root/fitter changes in probe-008 also did not establish bounds. No reason to repeat those unchanged tests or guess alternative enum values.

Next focus is effective width ownership: inspect the text object's layout-element/preferred-width inputs and custom wrapper constraints along the resolved path. If static evidence cannot establish a controlled width, scope live read-only component diagnostics before modifying more properties. No implicit permission to install a loader/assembly hook is introduced here. No new visual WO issued; all three original game bundles verified unchanged.
