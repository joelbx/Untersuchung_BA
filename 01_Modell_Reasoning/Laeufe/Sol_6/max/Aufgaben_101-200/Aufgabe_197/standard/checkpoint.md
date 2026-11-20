# Checkpoint

Issue: Qt 6.4 dark mode emits `TextBrightnessThreshold` for `colors.webpage.darkmode.threshold.text`; it should emit `ForegroundBrightnessThreshold` with the configured number converted to a string.

Completed: Added a Qt 6.4 variant whose text threshold key is `ForegroundBrightnessThreshold`, retaining the older key for Qt 6.3 and earlier. Added version boundary tests and checked the string value. `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` passed (42 tests); `git diff --check` passed.
