# Checkpoint

Task: fix dark mode foreground threshold option, compatibility mapping, and QtWebEngine 6.4 key selection.
Status: implemented and verified.
Changes: foreground option with Int default 256; text-to-foreground migration for YAML and targeted runtime alias for config.py/:set; QtWebEngine 6.4 Chromium key variant; focused tests.
Verification: QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/webengine/test_darkmode.py tests/unit/config/test_configdata.py tests/unit/config/test_configfiles.py tests/unit/config/test_config.py — 435 passed, 1 skipped. git diff --check passed.
Delegation: none.
