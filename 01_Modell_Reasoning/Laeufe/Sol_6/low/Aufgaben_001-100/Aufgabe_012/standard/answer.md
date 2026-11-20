Updated `custom_headers` so XHR requests omit the global `Accept-Language` value when a URL has no matching domain override. Domain overrides still apply, and other requests retain the global fallback. Added regression coverage for those cases.

All 26 relevant tests pass with `QT_QPA_PLATFORM=offscreen`; `git diff --check` is clean.