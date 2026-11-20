Added a Qt 6.4 dark mode variant that emits `ForegroundBrightnessThreshold` with the numeric value converted to a string. Qt 6.3 retains `TextBrightnessThreshold`.

Added regression tests covering both versions in [test_darkmode.py](/app/tests/unit/browser/webengine/test_darkmode.py).

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` — **40 passed**.