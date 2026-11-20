Task: Fix dark mode foreground brightness threshold for QtWebEngine 6.4+.
Status: Complete.
Changes: Added public threshold.foreground Int option (default 256), renamed-option migration for threshold.text, Qt 6.4 dark mode variant using ForegroundBrightnessThreshold, updated generated settings help and focused tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configfiles.py (272 passed, 1 skipped); QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_configdata.py (31 passed). git diff --check clean.
