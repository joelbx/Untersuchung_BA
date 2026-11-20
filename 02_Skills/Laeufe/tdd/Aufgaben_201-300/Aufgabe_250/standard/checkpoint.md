# Checkpoint

Task: add `luqum_replace_child` in `openlibrary/solr/query_utils.py` using test-first development.

Status: implementation and regression tests complete. `rg` was unavailable (`/bin/bash: rg: command not found`); used local fallback search.

Changes: added `luqum_replace_child` for `BaseOperation`, `Group`, and `Unary`, preserving the existing children sequence type and order, replacing every equal direct child, and leaving children untouched when there is no match. Added tests for these cases and the unsupported-parent error.

Verification:
- `pytest -q openlibrary/tests/solr/test_query_utils.py -k replace_child`: observed five expected `AttributeError` failures before implementation; passed after implementation.
- `pytest -q openlibrary/tests/solr/test_query_utils.py`: 11 passed, two pre-existing dependency/deprecation warnings.
- `pytest -q`: collection error `ValueError: Plugin name already registered: /app/infogami/conftest.py`; no tests collected.
- `make test-py`: 1328 passed, 17 skipped, 17 xfailed, 54 xpassed; one unrelated failure in `scripts/solr_builder/tests/test_fn_to_cli.py::TestFnToCLI::test_full_flow` (`ValueError: Unsupported type: str | None`), and one collection error in `scripts/tests/test_partner_batch_imports.py` from a blocked proxy request to a remote schema (`ProxyError: Tunnel connection failed: 403 Forbidden`). The full suite cannot be claimed green; the remote schema case remains unverified in this offline environment.
