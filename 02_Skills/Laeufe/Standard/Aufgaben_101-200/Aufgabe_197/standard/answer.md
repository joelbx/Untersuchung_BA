Updated the dark mode mapping so Qt 6.4 and later emit `ForegroundBrightnessThreshold` with the configured numeric value as a string. Earlier versions retain their existing key. Added version-specific regression tests.

The relevant test file passed: 43 tests. `git diff --check` also passed.