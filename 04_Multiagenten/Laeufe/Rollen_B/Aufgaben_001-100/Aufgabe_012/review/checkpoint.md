VERDICT: ACCEPT
Reviewed qutebrowser/browser/shared.py and qutebrowser/browser/webengine/interceptor.py against the issue. The fallback flag is disabled only for XHR; URL-specific accept-language settings remain available, and no URL preserves the global value. No code defect found.
Test: QT_QPA_PLATFORM=offscreen python -m pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py — 29 passed.
Check: git diff --check — passed.
