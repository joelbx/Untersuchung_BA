Migrated `get_ia.py` to `requests`, including response handling, HTTP errors, UTF-8 fallback, and range requests. Updated two deprecated callers for the Response interface and added focused tests.

Verification: **47 tests passed** in `test_get_ia.py`; `git diff --check` passed.