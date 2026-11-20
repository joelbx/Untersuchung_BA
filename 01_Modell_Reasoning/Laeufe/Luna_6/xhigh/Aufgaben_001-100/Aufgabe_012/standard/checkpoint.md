# Checkpoint

Task: Fix global Accept-Language fallback behavior for XHR requests.

Implemented:
- `custom_headers` now accepts `fallback_accept_language=True` and only omits Accept-Language when a URL is present, fallback is disabled, and no matching per-domain setting exists.
- The WebEngine interceptor disables that fallback only for XHR requests.
- Added shared header behavior tests and interceptor routing tests.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` passed (25 tests).
