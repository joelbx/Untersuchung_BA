Task: Resolve coverstore archive consistency in /app.
Status: Implemented ZIP staging, ID/path/URL helpers, batch locking, upload verification, database completion, remote redirects, schema flags/indexes, and documentation. Added focused archive tests.
Verification: pytest -q openlibrary/coverstore/tests: 22 passed, 7 skipped. Ruff check and git diff --check passed.
Limit: Legacy tar records remain supported for retrieval; converting an already remote tar batch to ZIP requires its source images and is rejected by ZIP membership validation if incomplete.
