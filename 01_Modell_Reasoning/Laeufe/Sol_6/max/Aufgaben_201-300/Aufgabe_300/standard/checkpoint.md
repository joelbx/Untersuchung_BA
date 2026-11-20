# Import API validation override

- Task: add `override-validation=true` handling through the import API and validation path; add `is_promise_item` catalog utility.
- Status: implementation and focused tests complete.
- Verification: `pytest -q openlibrary/plugins/importapi/tests openlibrary/catalog/add_book/tests openlibrary/tests/catalog/test_utils.py` passed (149 passed, 1 expected failure); `git diff --check` passed; Ruff passed with pre-existing `UP035` warning excluded. The same `UP035` warning occurs on the baseline version of `openlibrary/catalog/utils/__init__.py`.
