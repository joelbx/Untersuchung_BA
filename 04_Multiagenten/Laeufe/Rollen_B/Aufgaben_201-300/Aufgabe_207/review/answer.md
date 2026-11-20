VERDICT: FIX

The feature consolidation patch has no confirmed code defect, but the full relevant test module did not complete.

**TEST_ENVIRONMENT_PROBLEM:** `QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/config/test_qtargs.py` exited 1. An isolated run of `TestDarkMode::test_new_chromium` exited 139 with a segfault in QtWebEngine user agent initialization at [webenginesettings.py:360](/app/qutebrowser/browser/webengine/webenginesettings.py:360).

`DISPLAY=:0 QT_QPA_PLATFORM=offscreen python -m pytest --no-xvfb -q tests/unit/config/test_qtargs.py -k 'not test_new_chromium'` passed: **82 passed, 1 deselected**. Rerun the full module in a working QtWebEngine environment to clear the test gate. No project code was changed during this review.