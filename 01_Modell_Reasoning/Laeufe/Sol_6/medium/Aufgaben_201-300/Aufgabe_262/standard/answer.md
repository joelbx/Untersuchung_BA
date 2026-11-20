Book imports now validate cover URLs against `ALLOWED_COVER_HOSTS` in both new and matched edition paths. The new `process_cover_url` function accepts HTTP and HTTPS, compares hosts without regard to case, and removes `cover` from the edition dictionary whether the URL is accepted or ignored.

Verification: 151 import tests passed, 1 was already marked as an expected failure, and Ruff passed.