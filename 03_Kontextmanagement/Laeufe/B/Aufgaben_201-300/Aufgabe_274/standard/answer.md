Implemented the version-aware canvas workaround. The setting now accepts `always`, `auto`, and `never`, with `auto` as the default. In `auto`, the flag is added only on Qt 6 when the known Chromium major version is below 111.

The relevant tests passed: **112 WebEngine argument tests** and **31 configuration schema tests**. The Qt 6 boundaries were tested with simulated version information.