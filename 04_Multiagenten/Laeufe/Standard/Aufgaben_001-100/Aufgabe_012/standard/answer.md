Fixed XHR header handling. `custom_headers` now accepts `fallback_accept_language=True`; for XHR requests, the interceptor disables the global Accept-Language fallback while preserving domain-specific overrides. Other requests retain the global setting.

The focused tests passed: **29 passed**.