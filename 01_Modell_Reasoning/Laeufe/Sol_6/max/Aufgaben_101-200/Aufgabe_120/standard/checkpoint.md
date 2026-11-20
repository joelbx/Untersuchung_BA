# Coverstore archival checkpoint

Task: update cover archival to use deterministic zip batches, verify uploads, reconcile database paths and status, and prevent overlapping archival runs.

Initial state: repository is clean. Located `openlibrary/coverstore/archive.py`, `schema.sql`, and `schema.py`. `rg` is unavailable, so searches use `find` and `grep`.

Implemented: deterministic 10-digit cover IDs, 4-digit items, 2-digit batches; uncompressed zip staging; exact IA upload checks; locked batch processing; transactionally reconciled remote URLs; schema flags/indexes; server redirect from verified DB URLs; operator documentation. Added an SQLite-backed end-to-end archival test and focused retry, boundary, and lock tests.

Verification: `python -m pytest openlibrary/coverstore/tests -q --reruns 0` passed (25 passed, 7 skipped). `ruff check` passed. `git diff --check` passed.

Final review: staged covers stay locally readable; completion requires a closed batch, complete local zip inventory, valid CRCs, and exact remote filenames. Source cleanup has a retry manifest. The server redirects from verified database URLs and retries lookup if a local read races completion.
