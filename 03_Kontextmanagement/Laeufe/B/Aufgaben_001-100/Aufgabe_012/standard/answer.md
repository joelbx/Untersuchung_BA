Fixed the Accept-Language override in the checked-out repository. XHR requests now preserve a header set by JavaScript unless a URL-specific setting applies; other requests retain the global fallback.

The relevant tests passed: **25 passed** using Qt’s offscreen platform.