VERDICT: FIX

The new lookup in [imports.py](/app/openlibrary/core/imports.py:113) meets the specified source and status filtering requirements. But [Edition.from_isbn](/app/openlibrary/core/models.py:407) still passes a local match to `do_import`, which calls `/api/import` or `/api/import/ia` through [manage_imports.py](/app/scripts/manage_imports.py:32). A staged record therefore still depends on an import endpoint. Consume the staged data through a local import path to satisfy the expected behavior.

Relevant tests executed: `python -m pytest -q openlibrary/tests/core/test_imports.py` — 6 passed; `python -m pytest -q openlibrary/tests/core/test_models.py` — 10 passed. `git diff --check` passed. **TEST_ENVIRONMENT_PROBLEM:** none.