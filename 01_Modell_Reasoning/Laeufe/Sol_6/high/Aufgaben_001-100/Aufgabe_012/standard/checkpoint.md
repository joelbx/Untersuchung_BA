# Checkpoint

Task: Preserve explicit XHR Accept-Language headers while retaining global and domain-specific defaults where appropriate.

Status: Complete. `custom_headers` now uses URL-specific Accept-Language values without a global fallback when requested, and the WebEngine interceptor requests that behavior for XHR. Added unit coverage for XHR, normal requests, URL overrides, unmatched overrides, and no URL.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py tests/unit/browser/webkit/network/test_networkmanager.py` — 31 passed.
