# Checkpoint

Task: add local staged/pending import lookup in `openlibrary/core/imports.py`.

Initial inspection: `ImportItem` has `find_pending` and `find_by_identifier`; `Batch.dedupe_items` queries `import_item` using `ia_id IN $ia_ids`. `rg` is unavailable (`/bin/bash: rg: command not found`), so use local `find`/`grep` for discovery.

Next: inspect relevant tests and database query conventions, implement the method and constant, run relevant tests.

Implementation: added `STAGED_SOURCES` and `ImportItem.find_staged_or_pending`, then wired `Edition.from_isbn` to search both ISBN forms. Added a lookup test.

First verification: `pytest -q openlibrary/tests/core/test_imports.py` exited 1 because the new test asserted `web.db.ResultSet`, while SQLite returns `web.db.SqliteResultSet`. The query itself expanded the four expected source/identifier combinations. Adjusted the assertion; rerun pending.

The adjusted lookup test passed. Added a local ISBN-10 staged-record integration test and expanded matching rows. `pytest -q openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py` exited 0 with 17 passed. `ruff check openlibrary/core/imports.py openlibrary/core/models.py openlibrary/tests/core/test_imports.py` and `git diff --check` exited 0.

Optional formatter check unavailable: `ruff format --check openlibrary/core/imports.py openlibrary/core/models.py openlibrary/tests/core/test_imports.py` exited 2 with `error: unexpected argument '--check' found`. Local Ruff version does not support that option; formatting remains unverified by that command.

Final verification after the last source edit: `pytest -q openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py` exited 0 (17 passed); `ruff check openlibrary/core/imports.py openlibrary/core/models.py openlibrary/tests/core/test_imports.py && git diff --check` exited 0.
