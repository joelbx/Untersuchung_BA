Implemented a Qt 6.4+ dark mode variant that emits `ForegroundBrightnessThreshold` for the text threshold, while retaining the Qt 6.3 key. Added regression coverage in [test_darkmode.py](/app/tests/unit/browser/webengine/test_darkmode.py).

Verified: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py` — 40 passed; `git diff --check` passed.