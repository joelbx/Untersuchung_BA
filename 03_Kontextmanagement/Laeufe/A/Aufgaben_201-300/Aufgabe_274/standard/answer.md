Updated `qt.workarounds.disable_accelerated_2d_canvas` to accept `always`, `auto`, and `never`, with `auto` as the default. In `auto`, the flag is added only on Qt 6 when the known Chromium major version is below 111.

Added boundary tests. The relevant test suites passed: **511 passed, 1 expected failure**.