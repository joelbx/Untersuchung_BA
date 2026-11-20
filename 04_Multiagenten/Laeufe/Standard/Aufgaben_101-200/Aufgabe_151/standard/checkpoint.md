Task: Fix image-restricted file picker suffix handling in qutebrowser/browser/webengine/webview.py.
Status: Complete. Added extra_suffixes_workaround with runtime Qt 6.2.3–6.6.x gate, MIME-specific and wildcard expansion, and existing-extension subtraction. chooseFiles now appends missing suffixes before calling Qt's parent implementation. Added unit coverage for version bounds and MIME/wildcard cases.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/webengine/test_webview.py (11 passed); git diff --check (clean).
