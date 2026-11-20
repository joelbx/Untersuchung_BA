Updated the [dark mode mapping](/app/qutebrowser/browser/webengine/darkmode.py:296) so Qt 6.4 and later emit `ForegroundBrightnessThreshold` with the configured numeric value as a string. Added [version boundary tests](/app/tests/unit/browser/webengine/test_darkmode.py:171).

Verification: 42 dark mode tests passed; `git diff --check` passed.