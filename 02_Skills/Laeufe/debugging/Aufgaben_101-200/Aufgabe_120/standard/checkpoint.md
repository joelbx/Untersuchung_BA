# Coverstore archival checkpoint

## Root cause and pattern

Existing `archive()` wrote `.tar` plus `.index`, set `archived=true` and replaced database paths before upload, then removed originals. `code.py` redirected a fixed 8,000,000–8,809,999 interval to tar URLs regardless of the database row. Upload audit checked for a tar/index pair but did not reconcile cover rows. No batch lock existed. The working cover ID convention is 10 digits: four item digits, two batch digits, four entry digits.

## Changes

- Added deterministic `Cover`, `Batch`, `ZipManager`, `Uploader`, and `CoverDB` helpers in `archive.py`.
- Staging writes uncompressed, deduplicated ZIPs and keeps source files and database paths until all four ZIPs are verified on archive.org and checked for expected entries.
- Finalization updates all cover filenames to remote URLs with `uploaded=true` in a database transaction, then removes local files. Batch locks reject overlapping staging/finalization.
- Added `failed` and `uploaded` columns/indexes, removed hardcoded tar ID redirect in favor of row status, and documented schema and runbook.

## Checks

- Initial regression command: `python -m pytest -q openlibrary/coverstore/tests/test_archive.py` failed as expected because `Cover` and `ZipManager` did not exist.
- Final `python -m pytest -q -o reruns=0 openlibrary/coverstore/tests`: 23 passed, 7 skipped (database-backed webapp tests require a configured PostgreSQL environment).
- Final `python -m ruff check openlibrary/coverstore/archive.py openlibrary/coverstore/code.py openlibrary/coverstore/db.py openlibrary/coverstore/schema.py openlibrary/coverstore/tests/test_archive.py`: passed.
- Final `git diff --check`: passed.
- Live `ia` upload/list was not run: external archive.org research and operations are unavailable for this task. The uploader and verification behavior is covered locally with a fake uploader; actual remote item behavior remains unverified.
