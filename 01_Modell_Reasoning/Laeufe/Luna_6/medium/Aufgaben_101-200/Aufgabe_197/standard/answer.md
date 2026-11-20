Implemented a Qt 6.4 dark mode variant that emits `ForegroundBrightnessThreshold` for `threshold.text`, while preserving the Qt 6.3 mapping. Added tests for the emitted key and Qt version detection.

Validation: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` passed (39 tests). `git diff --check` passed.