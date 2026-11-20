# Checkpoint

Task: Preserve a JavaScript XHR Accept-Language header when no domain override is configured.

Status: Investigating root cause before edits.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using local grep/find.

Root cause: `shared.custom_headers` calls `config.instance.get` for Accept-Language with the default `fallback=True`. `RequestInterceptor.interceptRequest` passes its result to `setHttpHeader` for XHR as well as other resource types, overwriting any JS header. The config lookup supports `fallback=False` for URL-scoped values and returns `usertypes.UNSET` when none matches. A URL-less call must retain global behavior.

Pattern: The same config API is used for per-URL fallbacks elsewhere; XHR handling already exists in the interceptor for the Accept header. Hypothesis: use `fallback=False` only for URL-bearing XHR Accept-Language lookup and omit `UNSET`; preserve all other calls.

Initial reproduction command: `pytest -q tests/unit/browser/test_shared.py::test_custom_headers_accept_language_fallback tests/unit/browser/webengine/test_webengineinterceptor.py::test_accept_language_fallback_for_resource_type` exited 134 before executing assertions: Qt aborted while creating pytest-qt's qapp (no display). Retrying with `QT_QPA_PLATFORM=offscreen`.

Reproduction with display workaround: `QT_QPA_PLATFORM=offscreen pytest -q tests/unit/browser/test_shared.py::test_custom_headers_accept_language_fallback tests/unit/browser/webengine/test_webengineinterceptor.py::test_accept_language_fallback_for_resource_type` exited 1 with six expected failures: `custom_headers` rejected `fallback_accept_language`, and the interceptor did not pass it.

Fix: `custom_headers` takes `fallback_accept_language=True`, disables config fallback only for URL-bearing requests when false, and ignores the config `UNSET` sentinel. `interceptRequest` passes false for XHR and true for other requests.

Verification: `QT_QPA_PLATFORM=offscreen pytest -q --reruns 0 tests/unit/browser/test_shared.py tests/unit/browser/webengine/test_webengineinterceptor.py` exited 0; 28 passed. Initial no-display test command remains an environment-only failure. `git diff --check` exited 0 before the final formatting edit.
