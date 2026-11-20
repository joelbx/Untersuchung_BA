Migrated `get_ia.py` to `requests`, including status checks, retries, UTF-8 fallback, Range headers, and response content handling. Updated its deprecated callers and added focused tests.

Verification: 167 catalog and MARC tests passed; `git diff --check` passed.