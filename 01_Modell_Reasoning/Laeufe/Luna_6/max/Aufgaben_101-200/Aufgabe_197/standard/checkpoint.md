# Checkpoint

Resolved: added a Qt 6.4 dark mode variant using `ForegroundBrightnessThreshold` for `threshold.text`; Qt 6.3 retains `TextBrightnessThreshold`. Added version selection and regression coverage for both key names and the numeric string value.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` — 40 passed.
