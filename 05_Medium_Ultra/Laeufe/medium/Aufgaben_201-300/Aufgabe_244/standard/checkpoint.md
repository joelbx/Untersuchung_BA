Task: Fix the foreground dark mode threshold option and WebEngine 6.4 key mapping.
Status: Implemented public foreground option, migration from text, and version-specific Chromium keys. Updated settings documentation and tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configdata.py (75 passed); git diff --check passed.
Constraints: Edit checked-out files only; do not change git history, index baseline, or harness configuration.
