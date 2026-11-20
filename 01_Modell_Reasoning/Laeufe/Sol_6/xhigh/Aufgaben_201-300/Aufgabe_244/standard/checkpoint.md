Task: Fix dark mode foreground brightness threshold across QtWebEngine versions.
Status: Complete.
Changes: Added public Int foreground threshold (default 256); old text name migrates in autoconfig and resolves in live config APIs; WebEngine <6.4 emits TextBrightnessThreshold and >=6.4 emits ForegroundBrightnessThreshold. Updated generated settings documentation and focused tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configfiles.py tests/unit/config/test_configdata.py tests/unit/config/test_config.py — 437 passed, 1 skipped. Follow-up focused run after final test refinements — 51 passed. git diff --check passed.
Constraints: Local code/tests only; git history, index baseline, and harness configuration unchanged.
