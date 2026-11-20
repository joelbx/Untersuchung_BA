# Checkpoint

Task: fix custom Accept-Language handling for XHR requests.

Findings: `Config.get(..., url=url, fallback=False)` returns only matching URL-scoped values and yields `usertypes.UNSET` when there is no override.

Changes: `custom_headers` now accepts keyword-only `fallback_accept_language=True`, omits the global value for a URL lookup when false, and retains matching scoped overrides. WebEngine passes false only for XHR requests.

Verification: `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` passed (22 tests). The default display-backed attempt aborted during Qt application setup; the offscreen run completed successfully. `git diff --check` is clean.

No external research or downloads.
