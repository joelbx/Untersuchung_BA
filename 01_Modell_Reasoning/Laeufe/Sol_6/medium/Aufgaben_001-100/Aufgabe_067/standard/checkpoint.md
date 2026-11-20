Task: Add scrolling.bar=overlay with QtWebEngine/Qt/platform gating, migrate booleans, and support @js_headers.
Status: Implemented and verified.
Changes: Added overlay config value, gated Chromium flag to QtWebEngine Qt >= 5.11 outside macOS, migrated False to overlay, added flag matrix tests, and registered/applied js_headers marker for QtWebEngine >= 5.13.
Verification: 234 passed, 1 skipped across tests/unit/config/test_configfiles.py and TestQtArgs; end-to-end feature collection succeeded; git diff --check and compileall passed.
Limitation: Full test_configinit.py process stops at existing TestDarkMode::test_new_chromium without pytest summary in this environment.
