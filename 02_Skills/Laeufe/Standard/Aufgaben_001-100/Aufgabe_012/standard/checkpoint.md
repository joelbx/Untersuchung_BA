# Checkpoint

Task: Preserve custom XHR Accept-Language headers while keeping global fallback for other requests.
Status: Inspecting implementation and tests. `rg` is unavailable; using `grep` and `find`.

Test environment: `pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` exited 134 with `Fatal Python error: Aborted` in `pytestqt/plugin.py` qapp fixture, before test execution. Retrying with Qt offscreen platform.

Status: Implemented `fallback_accept_language` in shared.custom_headers and disabled global fallback for WebEngine XHR requests only. Added tests for URL overrides, missing overrides, no URL, default behavior, and interceptor request types.
Verification: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py tests/unit/browser/webkit/network/test_networkmanager.py` passed (32 tests). `git diff --check` passed. No remaining test uncertainty after offscreen retry.
