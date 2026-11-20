# Checkpoint

Task: consolidate list model functionality and registration.

Initial search command `rg` unavailable (`/bin/bash: rg: command not found`); using local grep/find fallback.

Status: inspecting repository.

Implemented: moved list methods into `core.models.List`, removed `ListMixin`, and added `core.lists.model.register_models()` for list document and changeset registration. Updated the list export annotation and added owner/registration tests.

Verification notes:
- `python -m pytest -q openlibrary/tests/core/test_models.py openlibrary/tests/core/test_lists_model.py openlibrary/tests/core/test_lists_engine.py openlibrary/plugins/upstream/tests/test_models.py openlibrary/plugins/openlibrary/tests/test_listapi.py openlibrary/plugins/openlibrary/tests/test_lists.py` failed: `test_listapi.py` cannot import `cookielib` (`ModuleNotFoundError`), and `test_lists.py::TestListRecord::test_from_input_with_data` fails because `web.ctx.env` is missing (`AttributeError`). These leave the full nearby test set unverified.
- `python -m pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py::TestListRecord::test_from_input_with_data` reproduces the missing `web.ctx.env` failure in isolation.
- `python -m black --check openlibrary/core/models.py openlibrary/core/lists/model.py openlibrary/plugins/upstream/models.py openlibrary/plugins/openlibrary/lists.py openlibrary/tests/core/test_models.py openlibrary/tests/core/test_lists_model.py` could not run: `/usr/local/bin/python: No module named black`. Formatting remains unverified by Black.
- Final focused verification: `python -m pytest -q openlibrary/tests/core/test_models.py openlibrary/tests/core/test_lists_model.py openlibrary/tests/core/test_lists_engine.py openlibrary/plugins/upstream/tests/test_models.py` — 20 passed, 0 failed.
- `python -m ruff check openlibrary/core/models.py openlibrary/core/lists/model.py openlibrary/plugins/upstream/models.py openlibrary/plugins/openlibrary/lists.py openlibrary/tests/core/test_models.py openlibrary/tests/core/test_lists_model.py` — exit 0, no findings.
- `git diff --check` — exit 0, no whitespace errors.
