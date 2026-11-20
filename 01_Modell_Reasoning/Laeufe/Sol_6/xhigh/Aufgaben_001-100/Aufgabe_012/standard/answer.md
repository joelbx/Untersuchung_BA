Updated `custom_headers` so XHR requests use a domain-specific `Accept-Language` setting when one matches, but do not apply the global setting. Other requests retain the global fallback. Added regression tests for both paths.

Validation: 30 relevant tests passed with Qt in offscreen mode; `git diff --check` passed.