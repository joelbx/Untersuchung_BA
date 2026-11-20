Updated `custom_headers` so XHR requests use a domain-specific Accept-Language override when one exists, but do not apply the global value otherwise. Other requests retain the global fallback, leaving an XHR’s JavaScript-supplied header intact.

The relevant tests passed: **28 passed**.