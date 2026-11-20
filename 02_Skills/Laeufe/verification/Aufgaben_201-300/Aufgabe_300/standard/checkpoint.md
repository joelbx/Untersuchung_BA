# Import API validation override checkpoint

Implemented:
- `/api/import` POST reads the URL query parameter `override-validation`; exactly `true` enables the override.
- `add_book.load()` forwards `override_validation` to `validate_record()`. The override bypasses publication year, independently published publisher, and source ISBN checks while keeping required-field checks.
- Added case-insensitive `is_promise_item(rec)` for `promise:` source records.
- Added tests for validation, propagation, query parsing, and the utility.

Verification (after final code edit):
- `python -m pytest -q openlibrary/plugins/importapi/tests openlibrary/catalog/add_book/tests openlibrary/tests/catalog/test_utils.py`: exit 0, 142 passed, 1 xfailed, 1 warning.
- `python -m ruff check --ignore UP035 openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/utils/__init__.py openlibrary/plugins/importapi/code.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/tests/catalog/test_utils.py`: exit 0.
- `git diff --check`: exit 0.

Local tooling limitations:
- `rg` unavailable (`/bin/bash: rg: command not found`); used grep/find for inspection.
- `python -m black --check openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/utils/__init__.py openlibrary/plugins/importapi/code.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/tests/catalog/test_utils.py`: exit 1, `/usr/local/bin/python: No module named black`. Black formatting remains unchecked.
- `python -m ruff format --check openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/utils/__init__.py openlibrary/plugins/importapi/code.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/tests/catalog/test_utils.py`: exit 2, `error: unexpected argument '--check' found`; installed Ruff version does not support this check.
- Ruff without `--ignore UP035` reports an existing `Mapping` import warning at `openlibrary/catalog/utils/__init__.py:4`.
