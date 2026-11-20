Task: Preserve JavaScript-specified Accept-Language on XHR requests.
Status: Complete. XHR requests omit the global Accept-Language header unless a URL-specific setting matches. Other request types retain the existing fallback.
Verification: 29 focused unit tests passed; git diff --check passed.
