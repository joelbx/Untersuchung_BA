Fixed XHR Accept-Language handling. `custom_headers` now accepts `fallback_accept_language=True`; XHR requests pass `False`, so the global setting no longer overrides a JavaScript supplied header. A domain-specific setting still applies, and other requests retain the global fallback.

The relevant tests passed: **26 passed** with Qt offscreen. No delegation was used.