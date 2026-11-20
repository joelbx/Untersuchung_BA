Issue: preserve JavaScript XHR Accept-Language headers against the global fallback.

Plan: inspect custom_headers and request interception, update their behavior, then run the focused existing tests.

Implemented `fallback_accept_language` in shared custom header selection. WebEngine passes false for XHR and true for other resource types. Added coverage for omitted global fallback, retained no-URL behavior, and domain override.

Verification: `python -m compileall` and `git diff --check` pass. Focused pytest was attempted but the process aborted during Qt `qapp` setup before executing tests (environmental Qt initialization failure).
