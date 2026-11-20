# Coverstore archival checkpoint

Implemented zip staging, zero-padded cover/item/batch paths and URLs, upload verification and batch finalization, per-batch local locks, uploaded/failed schema fields, and database-directed retrieval. Updated operational documentation and added focused tests.

Local tooling note: `rg` was unavailable (`/bin/bash: rg: command not found`); repository inspection used `find` and `grep`. No download was requested.

Verification evidence:
- `pytest -q openlibrary/coverstore/tests/test_archive.py`: 5 passed.
- `pytest -q openlibrary/coverstore/tests`: 23 passed, 7 skipped (exit 0).
- `ruff check openlibrary/coverstore/archive.py openlibrary/coverstore/code.py openlibrary/coverstore/coverlib.py openlibrary/coverstore/schema.py openlibrary/coverstore/tests/test_archive.py`: passed (exit 0).
- `git diff --check`: passed (exit 0).

The webapp suite skips seven integration tests in this environment. Actual Internet Archive upload was not performed; the uploader and finalization behavior are covered with local fakes.
