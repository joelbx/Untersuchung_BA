Updated `custom_headers` so XHR requests do not apply the global Accept-Language setting. A matching domain override still applies, and other requests retain the global fallback.

The shared-header and WebEngine interceptor tests passed: **28 passed**. `git diff --check` passed. Flake8 was unavailable in the environment.