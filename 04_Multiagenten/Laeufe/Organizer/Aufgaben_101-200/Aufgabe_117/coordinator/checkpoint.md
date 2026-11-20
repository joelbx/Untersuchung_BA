Task: implement QtWebEngine 5.15.3 locale workaround.
Status: complete. Added qt.workarounds.locale (false by default, QtWebEngine only), locale .pak lookup and Chromium-compatible fallback mapping, conditional --lang integration, and focused tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/config/test_qtargs.py tests/unit/config/test_configdata.py (184 passed).
Delegation: none.
