Updated `custom_headers` so XHR requests leave the global `Accept-Language` header unset, allowing JavaScript’s custom header to be sent. A matching domain override still applies; other requests keep the global fallback.

The relevant unit tests pass: **29 passed**.