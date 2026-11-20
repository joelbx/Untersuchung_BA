# Checkpoint

Task: import alternate-script names for MARC 100, 700, and 720 personal authors.

Plan: inspect local parser and tests; add failing behavioral tests; implement the smallest parser change; run relevant tests and project suite.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); use local `grep` and `find`.

Implemented: normalized author names and dates; resolved each personal author's MARC `$6` linkage against `880` fields for tags 100, 700, and 720; collected unique alternate names. Updated MARC fixture expectations and the downstream add-book name expectation to reflect required trailing-period removal.

Verification:
- RED: `pytest -q openlibrary/catalog/marc/tests/test_parse.py -k 'name_from_list_normalizes or linked_personal_author'` failed for the missing helper and linked names before implementation.
- GREEN: `pytest -q openlibrary/catalog/marc/tests --reruns 0` passed: 124 tests, 21 warnings.
- `pytest -q openlibrary --reruns 0 --tb=short` passed: 1344 passed, 17 skipped, 17 xfailed, 54 xpassed, 45 warnings.
- Full bare command `pytest -q --reruns 0` failed during collection with `ValueError: Plugin name already registered: /app/infogami/conftest.py`. The `infogami` symlink causes duplicate plugin registration. This leaves bare root collection unverified; the complete `openlibrary` tree was run instead.
