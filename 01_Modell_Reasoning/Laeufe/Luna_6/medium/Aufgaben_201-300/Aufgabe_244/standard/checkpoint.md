# Checkpoint

Implemented the public `colors.webpage.darkmode.threshold.foreground` integer option with default 256 and configured `threshold.text` as a renamed-option migration for compatibility. Dark mode uses `TextBrightnessThreshold` before QtWebEngine 6.4 and `ForegroundBrightnessThreshold` from 6.4 onward.

Added tests for threshold key selection and version detection. Verification passed: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configdata.py` (71 passed), and `git diff --check`.
