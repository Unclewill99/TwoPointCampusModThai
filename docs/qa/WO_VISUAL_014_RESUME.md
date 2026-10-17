# WO-VISUAL-014 resume — capability gate first

Date: 2026-10-17. Same task, same unchanged probe-013, same coverage gaps. Previous attempt BLOCKED before install. Preserve report/evidence history.

Before any install, on the receiving desktop agent's current tool session:

1. Read its current computer-use skill/API documentation. Verify that Windows native apps are supported; browser-only access is insufficient.
2. Obtain a fresh window inventory and a screenshot of the selected Steam window. Inspect image content; a returned chat/browser screenshot does not qualify merely because the requested window ID was Steam. Do not send input to an unverified target.
3. Establish a documented pointer-placement/hover capability without activating a control or altering settings. An explicit hover method is not required if the CURRENT documented API provides another supported, non-mutating pointer placement method. Do not assume prior sessions' zero-delta scroll remains supported, guess undocumented calls or use native input scripts as a bypass.
4. If capture or pointer placement remains unavailable, stop before install and report capability BLOCKED. Move this WO to a desktop-capable agent or let the user perform documented manual hover/capture; do not change probe code to solve tool limitations.

Only after this gate succeeds follow WO_VISUAL_014.md unchanged. Do not repeat accepted primary matrix. Use --probe probe-013 for every action and separate inspected install/check before launch. If original assets already installed there is nothing to restore just to end preflight; verify original hashes instead.

Save retry evidence under local/qa/WO-VISUAL-014/retry/ and append results to WO_VISUAL_014_REPORT.md. Distinguish new current environment observations from historical WO-013 settings. Return Medium only if actually changed; don't claim current Medium without seeing it. No commit/push, branch switch, in-session code edits or asset upload.
