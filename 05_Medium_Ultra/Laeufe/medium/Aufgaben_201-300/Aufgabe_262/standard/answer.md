Book imports now check cover URL hosts against `ALLOWED_COVER_HOSTS` in both the new and matched edition paths. The new `process_cover_url` function accepts HTTP and HTTPS URLs, compares hostnames without regard to case, and removes the `cover` key whether the URL is accepted or ignored.

Verification: 88 add-book tests passed, Ruff passed, and `git diff --check` passed.