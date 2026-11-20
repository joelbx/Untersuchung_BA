Task: Implement QtWebEngine 5.15.3 locale workaround.
Status: Complete.
Changes: Added qt.workarounds.locale (default false, QtWebEngine only); added locale pak path and Chromium-compatible language fallback helpers; added --lang argument when the enabled Linux/5.15.3 workaround finds a missing locale pack; added focused tests.
Verification: QT_QPA_PLATFORM=offscreen python -m pytest tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py -q (182 passed); git diff --check and compileall passed. flake8 unavailable in environment.
