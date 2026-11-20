Updated the setting to the string values `always`, `auto`, and `never`, with `auto` as the default. The WebEngine argument resolver now adds `--disable-accelerated-2d-canvas` in auto mode only for Qt 6 with a known Chromium major below 111.

Verification: 112 Qt argument tests and 31 configuration schema tests passed.