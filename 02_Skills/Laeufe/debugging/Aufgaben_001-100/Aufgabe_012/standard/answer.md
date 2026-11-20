Fixed the XHR Accept-Language override. `custom_headers` now omits the global value for URL-bearing XHR requests when no domain-specific value is configured, allowing the JavaScript header to be preserved. Other requests retain the global fallback.

Regression tests cover the fallback and domain override behavior. The relevant test modules pass: **28 tests passed**.