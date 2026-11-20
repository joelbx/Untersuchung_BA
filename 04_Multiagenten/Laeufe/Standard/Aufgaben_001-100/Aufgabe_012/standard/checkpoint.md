Task: Fix Accept-Language handling for XHR interception.
Status: Complete. custom_headers accepts fallback_accept_language=True, skips global fallback for URL-specific XHR lookups, and keeps domain overrides. interceptRequest disables fallback only for XHR requests. Added focused helper and interceptor tests.
Verification: QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py (29 passed); git diff --check passed.
Constraints observed: Used local repository and existing tests only; git history/index and harness configuration unchanged.
