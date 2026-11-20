Fixed the reviewed PyOpenSSL fallback defect: client certificate and Unix socket HTTPS connections now use the configured cipher context. Added regression tests for both paths.

The reviewer’s exact test command passed: **136 passed, 4 warnings**. `git diff --check` is clean.

**TEST_ENVIRONMENT_PROBLEM:** `OpenSSL` is unavailable locally, so the real PyOpenSSL fallback could not be exercised; the new tests use a mocked context.