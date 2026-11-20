Updated `qt.workarounds.disable_accelerated_2d_canvas` to accept `always`, `auto`, and `never`, with `auto` as the default. In `auto`, the flag is added only on Qt 6 when the known Chromium major version is below 111.

Added tests for the requested Qt version boundaries and unknown Chromium versions. Verification passed: 372 tests passed, 1 skipped.