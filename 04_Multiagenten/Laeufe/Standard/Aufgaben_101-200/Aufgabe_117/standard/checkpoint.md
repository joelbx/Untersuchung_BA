# Checkpoint

Task: implement QtWebEngine 5.15.3 Linux locale workaround.
Status: complete. Added opt-in QtWebEngine-only setting, locale resource lookup and Chromium-style fallbacks, startup --lang argument, documentation, and unit coverage.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py (182 passed); git diff --check passed.
