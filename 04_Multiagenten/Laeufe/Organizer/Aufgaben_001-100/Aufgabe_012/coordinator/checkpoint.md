Task: Fix custom Accept-Language handling for XHR requests.
Status: Complete.
Changes: custom_headers accepts fallback_accept_language; XHR requests disable the global fallback while domain-specific overrides still apply. Added shared-header and interceptor tests.
Validation: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py tests/unit/browser/webkit/network/test_networkmanager.py (26 passed). git diff --check passed.
Delegation: None.
