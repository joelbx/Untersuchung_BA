VERDICT: FIX

**Code defect:** [archive.py](/app/openlibrary/coverstore/archive.py:112) treats a remote zip filename as proof that its contents match the local zip. If `archive()` later adds covers to that batch, finalization skips reupload, marks those covers `uploaded=true`, and deletes the local zip. Their remote URLs then point to missing images. Verify the remote zip contents or checksum before updating the database or deleting local files; prevent changes to a finalized batch.

**TEST_ENVIRONMENT_PROBLEM:** The existing database integration tests are skipped because they require a running PostgreSQL database and the `openlibrary` user. Run them in that environment. Their archive assertion in [test_webapp.py](/app/openlibrary/coverstore/tests/test_webapp.py:194) also expects the old tar format and needs updating for zip output.

Tests attempted:

- `python -m pytest -q openlibrary/coverstore/tests/test_archive_zip.py` — 3 passed.
- `python -m pytest -q openlibrary/coverstore/tests` — 21 passed, 7 skipped.
- `python -m pytest -q -rs openlibrary/coverstore/tests/test_webapp.py` — 1 passed, 7 skipped.

I made no project code or test changes during this independent review.