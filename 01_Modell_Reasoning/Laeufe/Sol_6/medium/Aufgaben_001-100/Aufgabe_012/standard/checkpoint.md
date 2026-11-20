Task: Preserve custom Accept-Language on XHR requests while retaining global fallback for other requests and domain overrides.
Status: Complete. custom_headers now accepts fallback_accept_language (default True), suppresses the global Accept-Language when False and a URL is provided, and preserves per-domain overrides. WebEngine interception passes False for XHR and True for other request types.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py (29 passed). git diff --check passed.
