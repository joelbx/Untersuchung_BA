Updated `custom_headers` so XHR requests use a domain-specific `Accept-Language` setting when present, but do not apply the global setting. Other requests retain the global fallback.

Added tests for the fallback behavior and request-type handling. The relevant test suites passed: **29 tests**.