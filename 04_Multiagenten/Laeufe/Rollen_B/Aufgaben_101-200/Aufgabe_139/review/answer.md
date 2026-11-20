VERDICT: FIX

**Code defect:** [promise_batch_imports.py](/app/scripts/promise_batch_imports.py:63) maps a missing ASIN to `identifiers.amazon = [None]`. For an incomplete item without ISBN-10, staging passes that value to [get_non_isbn_asin](/app/openlibrary/catalog/utils/__init__.py:400), which calls `None.startswith("B")`. I reproduced the resulting `AttributeError`; it occurs before the staging error handler and stops the batch. Omit absent ASINs when mapping, and make identifier selection skip empty or non-string values.

**TEST_ENVIRONMENT_PROBLEM:** The plain targeted pytest command could not collect the script tests because `_init_path` was not on `PYTHONPATH`. With the repository’s scripts directory included, the tests ran successfully:

- `python -m pytest -q openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/importapi/tests/test_import_validator.py scripts/tests/test_promise_batch_imports.py` — collection error: `ModuleNotFoundError: _init_path`; 24 other tests passed.
- `PYTHONPATH=/app/scripts:/app python -m pytest -q openlibrary/plugins/importapi/tests/test_code.py openlibrary/plugins/importapi/tests/test_import_validator.py scripts/tests/test_promise_batch_imports.py` — 31 passed.
- `PYTHONPATH=/app/scripts:/app python -m pytest -q openlibrary/catalog/add_book/tests/test_add_book.py` — 74 passed.

I reviewed the patch without changing project code or tests.