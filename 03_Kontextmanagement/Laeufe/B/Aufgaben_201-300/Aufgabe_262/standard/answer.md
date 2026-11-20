Book imports now check cover URLs against `ALLOWED_COVER_HOSTS` before upload. The new `process_cover_url` function accepts HTTP and HTTPS, compares hosts without case sensitivity, and removes the `cover` key whether the URL is allowed or rejected. Both new and matched edition imports use it.

Verification: all 89 add-book tests passed, and Ruff passed.