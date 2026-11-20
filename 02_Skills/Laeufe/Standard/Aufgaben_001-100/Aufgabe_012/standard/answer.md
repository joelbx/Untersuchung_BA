Updated `custom_headers` to accept `fallback_accept_language=True`. For XHR requests, the interceptor now skips the global Accept-Language value while still applying a matching per-domain override. Other requests retain the global fallback.

Added coverage for those cases. **32 relevant tests passed** with Qt’s offscreen platform, and `git diff --check` passed.