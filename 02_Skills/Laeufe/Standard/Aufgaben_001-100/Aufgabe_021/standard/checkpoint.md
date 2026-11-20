# Checkpoint

Task: annotate List and Seed, normalize subject and entity seeds, and keep export output typed and complete.

Changes: added SeedDict and SeedSubjectString types, subject conversion and type guard, normalized duplicate checks, mixed-seed loading, type-filtered export with all three categories, utility return annotations, and focused tests.

Verification passed:
- `pytest -q openlibrary/tests/core/lists/test_model.py openlibrary/tests/core/test_lists_model.py openlibrary/tests/core/test_lists_engine.py openlibrary/plugins/openlibrary/tests/test_lists.py` — 15 passed.
- `mypy --follow-imports=silent openlibrary/core/lists/model.py openlibrary/plugins/openlibrary/lists.py` — no issues.
- `ruff check openlibrary/core/lists/model.py openlibrary/plugins/openlibrary/lists.py openlibrary/core/helpers.py openlibrary/core/models.py openlibrary/tests/core/lists/test_model.py openlibrary/plugins/openlibrary/tests/test_lists.py` — passed.
- `git diff --check` — passed.

Unavailable check: `pytest -q openlibrary/tests/core/lists/test_model.py openlibrary/tests/core/test_lists_model.py openlibrary/tests/core/test_lists_engine.py openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/openlibrary/tests/test_listapi.py` collected 15 passing tests but failed collecting `test_listapi.py`: `ModuleNotFoundError: No module named 'cookielib'`. That legacy API test remains unverified in this Python 3 environment. No dependency was downloaded.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and `grep`.
