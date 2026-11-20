Migrated `get_ia.py` to `requests`, including status validation, response content and text handling, UTF-8 fallback, and Range headers. Updated its callers in `marc_subject.py` and the existing tests.

Verification: all 47 tests in `test_get_ia.py` pass, and `git diff --check` passes.