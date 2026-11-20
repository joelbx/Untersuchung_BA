Updated the dark mode mapping so Qt 6.4 emits `("ForegroundBrightnessThreshold", "100")` for a text threshold of `100`. Earlier Qt versions retain their existing key. Added version-specific regression coverage in [test_darkmode.py](/app/tests/unit/browser/webengine/test_darkmode.py).

Verification: all 40 dark mode tests passed with Qt’s offscreen platform.