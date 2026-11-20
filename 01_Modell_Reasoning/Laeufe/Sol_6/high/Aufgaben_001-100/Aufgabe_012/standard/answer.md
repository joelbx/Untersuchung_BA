Updated `custom_headers` so XHR requests leave out the global Accept-Language value when a URL has no matching override. Domain-specific overrides still apply, and other request types retain the global fallback. The WebEngine interceptor now selects the XHR behavior.

Added regression coverage and updated the checkpoint. The relevant tests passed: **31 passed**.