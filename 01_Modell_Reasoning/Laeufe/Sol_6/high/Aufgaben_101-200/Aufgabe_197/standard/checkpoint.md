# Checkpoint

Completed the Qt 6.4 dark mode text threshold fix. Added a Qt 6.4 definition that emits `ForegroundBrightnessThreshold` for `colors.webpage.darkmode.threshold.text` while retaining earlier version mappings. Added version-specific regression coverage.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` passed (41 tests). `git diff --check` passed.
