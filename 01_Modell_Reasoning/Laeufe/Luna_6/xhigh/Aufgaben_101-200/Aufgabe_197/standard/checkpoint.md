# Checkpoint

Task: Fix the Qt 6.4 mapping for `colors.webpage.darkmode.threshold.text` so it emits `ForegroundBrightnessThreshold` with the configured numeric value as a string.

Constraints: Use only local repository code and existing tests; do not alter git history, index baseline, or harness configuration.

Progress: Added a Qt 6.4 variant, switched it at QtWebEngine 6.4+, and mapped its text threshold to `ForegroundBrightnessThreshold`. Added regression coverage preserving the Qt 6.3 key and verifying Qt 6.4 emits the numeric value as a string. `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` passes (40 tests), and `git diff --check` passes.
