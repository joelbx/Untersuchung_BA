# Checkpoint

Task: support `override-validation=true` on the import API and add `is_promise_item`.
Status: implementation and regression tests complete; final suite running.

Test-first evidence:
- `pytest -q --reruns 0 openlibrary/plugins/importapi/tests/test_code.py -k 'promise_item or overrides_validation'` failed on missing `is_promise_item` and explicit true not being forwarded.
- `pytest -q --reruns 0 openlibrary/plugins/importapi/tests/test_code.py -k reads_override_from_url_query` failed because POST/form input could mask the URL query.
- Add-book regression tests failed on the missing `override_validation` argument.

Verification and offline limits:
- `pytest -q --reruns 0 openlibrary/catalog/add_book/tests openlibrary/plugins/importapi/tests`: 100 passed, 1 xfailed (before final URL-only refinement).
- `pytest -q --reruns 0`: collection failed with `ValueError: Plugin name already registered: /app/infogami/conftest.py` because the bare command collects incompatible test trees.
- `pytest -q --reruns 0 . --ignore=tests/integration --ignore=infogami --ignore=vendor --ignore=node_modules`: 1541 passed, 17 skipped, 17 xfailed, 54 xpassed, but collection errored in `scripts/tests/test_partner_batch_imports.py`; its import requests a schema from raw.githubusercontent.com and the proxy returned `403 Forbidden`. No dependencies were downloaded. That single file's behavior remains unverified offline.
- Same project suite with `--ignore=scripts/tests/test_partner_batch_imports.py`: 1541 passed, 17 skipped, 17 xfailed, 54 xpassed before final URL-only refinement; rerun pending.
- `python -m black --check ...`: unavailable (`No module named black`).
- `python -m ruff check ...`: existing `UP035` in `openlibrary/catalog/utils/__init__.py` line 4 (`Mapping` import).

Final verification:
- `pytest -q --reruns 0 . --ignore=tests/integration --ignore=infogami --ignore=vendor --ignore=node_modules --ignore=scripts/tests/test_partner_batch_imports.py`: 1542 passed, 17 skipped, 17 xfailed, 54 xpassed, 1 existing `cgi` deprecation warning.
- `python -m ruff check --ignore UP035` on all five changed files: passed. `UP035` was ignored solely for the pre-existing import noted above.
- `git diff --check`: passed.
