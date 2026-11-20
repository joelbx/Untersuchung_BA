VERDICT: FIX

Review complete. The new lookup generates source-prefixed IDs and filters staged/pending rows correctly, but `Edition.from_isbn` still passes a matching row to `do_import`, which calls `ol.import_data` or `ol.import_ocaid` over the import API. Thus staged data is not imported through a local path, contrary to the issue's expected behavior. Correct by consuming staged `item.data` locally in ISBN resolution (and only use a remote import path when local data is unavailable); cover that path with an existing or focused integration test.

Tests executed: `python -m pytest -q openlibrary/tests/core/test_imports.py` (6 passed); `python -m pytest -q openlibrary/tests/core/test_models.py` (10 passed). `git diff --check` passed. TEST_ENVIRONMENT_PROBLEM: none.
