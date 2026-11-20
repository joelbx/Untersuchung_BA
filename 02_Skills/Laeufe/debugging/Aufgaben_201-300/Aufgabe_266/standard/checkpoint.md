# Checkpoint

Task: Add local staged or pending import lookup by source and identifier.

Status: Investigating repository patterns and tests. `rg` is unavailable (`/bin/bash: rg: command not found`); using `grep` and `find`.

Investigation: `Edition.from_isbn` in `openlibrary/core/models.py` already queries `import_item` for staged/pending records, but hardcodes amazon/idb and only the ISBN-13 form. `ImportItem` has no reusable lookup. `db.query` returns web.db.ResultSet; existing `Batch.dedupe_items` uses `IN $ia_ids` with bound vars. Hypothesis: moving the existing query into `ImportItem.find_staged_or_pending` with the Cartesian source/identifier IDs, then calling it from `from_isbn` with ISBN-13 and ISBN-10, provides the requested local resolution path.

Implemented: Added `STAGED_SOURCES`, `ImportItem.find_staged_or_pending` using bound source/identifier combinations and status filtering, and wired `Edition.from_isbn` to search both ISBN-13 and ISBN-10. The method returns the DB query result directly. Empty source/identifier input uses a false SQL predicate to retain a result-set return without invalid PostgreSQL `IN ()` syntax.

Test progression: Baseline `python -m pytest openlibrary/tests/core/test_imports.py -q` passed (5). New test initially failed on missing `STAGED_SOURCES`, as expected. First implementation revealed SQLite returns `SqliteResultSet`, a sibling of production `ResultSet` under `BaseResultSet`; test now asserts the common base and validates rows. Final `python -m pytest openlibrary/tests/core/test_imports.py openlibrary/tests/core/test_models.py -q` passed (16). `ruff check openlibrary/core/imports.py openlibrary/core/models.py openlibrary/tests/core/test_imports.py` passed. `git diff --check` passed.

Tooling note: `ruff format --check openlibrary/core/imports.py openlibrary/core/models.py openlibrary/tests/core/test_imports.py` failed with `error: unexpected argument '--check' found`; this installed Ruff does not support that option. No formatter result is claimed. Earlier `rg` was unavailable; local `grep` and `find` were used instead.
