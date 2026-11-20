Implemented the foreground threshold option with default `256`, retained `threshold.text` through the config migration, and selected the Chromium setting key based on the QtWebEngine version.

Verification passed: **71 tests** across the dark mode and config data suites; `git diff --check` passed.