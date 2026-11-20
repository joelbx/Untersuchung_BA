# Cover archival checkpoint

Task: implement consistent zip batch archival, upload validation, database state updates, and schema changes.

Status: inspecting current implementation and tests. Assigned TDD workflow in use; no production edits yet.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); using `find` and `grep`.

Verification: `pytest -q openlibrary/coverstore/tests --reruns 0 --disable-warnings` passed (24 passed, 7 skipped, 2 warnings). Bare `pytest -q --reruns 0 --disable-warnings` failed during collection with `ValueError: Plugin name already registered: /app/infogami/conftest.py`; no tests ran. Will use the repository Makefile's exclusions for the full suite.

Final implementation: ZIP batches use fixed-width item/batch/cover IDs and stored entries; upload verification gates DB URL updates and deletion. Local per-batch locks serialize staging and finalization. Missing source images set `failed=true`. Retrieval uses stored remote URLs and supports legacy remote tar references.

Final checks:
- `pytest -q openlibrary/coverstore/tests --reruns 0 --disable-warnings`: 30 passed, 7 skipped, 2 warnings.
- `pytest . --ignore=tests/integration --ignore=infogami --ignore=vendor --ignore=node_modules --ignore=scripts/tests/test_partner_batch_imports.py --reruns 0 --disable-warnings -q`: 1556 passed, 10 skipped, 17 xfailed, 54 xpassed, 2 warnings.
- `python -m ruff check openlibrary/coverstore/archive.py openlibrary/coverstore/code.py openlibrary/coverstore/schema.py openlibrary/coverstore/tests/test_archive.py`: passed.
- `git diff --check`: passed.

Offline tooling limits: The repository Makefile test scope without the additional ignore failed while collecting `scripts/tests/test_partner_batch_imports.py`: `requests.exceptions.ProxyError` for `https://raw.githubusercontent.com/internetarchive/openlibrary-client/master/olclient/schemata/import.schema.json` (proxy tunnel 403). That test remains unverified. `python -m black --check openlibrary/coverstore/archive.py openlibrary/coverstore/code.py openlibrary/coverstore/schema.py openlibrary/coverstore/tests/test_archive.py` could not run: `/usr/local/bin/python: No module named black`. Ruff formatting and linting ran instead. No downloads were attempted.
