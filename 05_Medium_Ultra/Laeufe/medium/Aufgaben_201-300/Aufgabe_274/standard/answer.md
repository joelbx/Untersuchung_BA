Updated `qt.workarounds.disable_accelerated_2d_canvas` to accept `always`, `auto`, and `never`, with `auto` as the default. In `auto`, the flag is added only on Qt 6 when the detected Chromium major version is known and below 111. Added tests for the requested Qt versions and Chromium boundary.

Verification: 144 relevant tests passed with `QT_QPA_PLATFORM=offscreen`; `git diff --check` passed.