Implemented the XHR `Accept-Language` fallback behavior. `custom_headers` now accepts `fallback_accept_language=True`; the interceptor disables it for XHR only. Matching per-domain settings still apply, and calls without a URL retain the global header.

Added coverage for fallback behavior and interceptor routing in [test_shared.py](/app/tests/unit/browser/test_shared.py) and [test_webengineinterceptor.py](/app/tests/unit/browser/webengine/test_webengineinterceptor.py).

Verification passed: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` — 25 tests.