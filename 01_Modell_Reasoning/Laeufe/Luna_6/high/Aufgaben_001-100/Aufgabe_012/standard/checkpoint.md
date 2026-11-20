# Checkpoint

Task: fix custom `Accept-Language` handling for XHR requests.

Implemented:
- `custom_headers` now accepts keyword-only `fallback_accept_language` (default `True`). With a URL and the flag false, config lookup skips the global fallback while retaining URL pattern overrides. Without a URL, the global fallback remains enabled.
- WebEngine request interception disables that fallback for XHR requests only.
- Added shared-header coverage for the fallback cases and a per-domain override.

Verification:
- `git diff --check` passed.
- `QT_QPA_PLATFORM=offscreen QTWEBENGINE_DISABLE_SANDBOX=1 pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` passed (23 tests).
- Plain and `xvfb-run` pytest attempts aborted during Qt app initialization in this headless environment; offscreen mode resolved it.
