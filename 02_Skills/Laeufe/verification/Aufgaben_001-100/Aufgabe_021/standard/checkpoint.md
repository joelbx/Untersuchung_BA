# List model typing task

- Started inspection of `openlibrary/core/lists/model.py` and `openlibrary/plugins/openlibrary/lists.py`.
- `rg` is unavailable (`/bin/bash: rg: command not found`); using local `grep`/`find` for inspection.
- Implemented `SeedDict`, typed seed inputs and returns, normalized key comparison, subject key helpers, and type-filtered export output. Added focused tests.
- Final `pytest -q openlibrary/tests/core/lists/test_model.py openlibrary/tests/core/test_lists_model.py openlibrary/tests/core/test_lists_engine.py openlibrary/plugins/openlibrary/tests/test_lists.py`: 20 passed.
- Final `ruff check openlibrary/core/lists/model.py openlibrary/plugins/openlibrary/lists.py openlibrary/core/helpers.py openlibrary/core/models.py`: exit 0.
- Final `git diff --check`: exit 0.
- `python -m compileall -q openlibrary/core/lists/model.py openlibrary/plugins/openlibrary/lists.py openlibrary/core/helpers.py openlibrary/core/models.py`: exit 0.
- Broader legacy check `pytest -q openlibrary/tests/core/lists/test_model.py openlibrary/tests/core/test_lists_model.py openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/openlibrary/tests/test_listapi.py` could not collect `test_listapi.py`: `ModuleNotFoundError: No module named 'cookielib'`. That module's tests remain unverified in this environment.
