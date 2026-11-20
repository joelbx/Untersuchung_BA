# Checkpoint

Implemented `override-validation=true` for the import API, forwarded through `add_book.load` to `validate_record`. The override bypasses publication year, independently published, and source ISBN checks while preserving required-field checks. Added `is_promise_item` with case-insensitive prefix matching and focused tests.

Verification:
- `python -m pytest -q openlibrary/catalog/add_book/tests openlibrary/plugins/importapi/tests openlibrary/tests/catalog/test_utils.py`: 147 passed, 1 xfailed.
- `python -m ruff check --ignore UP035 openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/utils/__init__.py openlibrary/plugins/importapi/code.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/tests/catalog/test_utils.py`: passed.
- `git diff --check`: passed.
- Plain `python -m ruff check` on the same files reports UP035 on the pre-existing `from typing import cast, Mapping` line in `openlibrary/catalog/utils/__init__.py`; confirmed the line exists in HEAD.
- `python -m black --check openlibrary/catalog/add_book/__init__.py openlibrary/catalog/add_book/tests/test_add_book.py openlibrary/catalog/utils/__init__.py openlibrary/plugins/importapi/code.py openlibrary/plugins/importapi/tests/test_code.py openlibrary/tests/catalog/test_utils.py` could not run: `/usr/local/bin/python: No module named black`. Formatting uncertainty remains for that check; no dependency was downloaded.
