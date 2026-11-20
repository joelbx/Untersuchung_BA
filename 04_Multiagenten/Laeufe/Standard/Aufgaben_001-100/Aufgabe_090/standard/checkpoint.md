Task: Fix /lists/add POST handling for conflicting query/body parameters and unflatten overwrite behavior.
Status: Complete. Body form values are parsed separately with parse_qs first-value semantics, unflattened, and applied over defaults. Empty-body requests use web.input defaults. Indexed seeds ignore invalid entries. Later simple-key assignments overwrite earlier values in unflatten.
Verification: python -m pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py (17 passed); git diff --check passed.
Files changed: openlibrary/plugins/openlibrary/lists.py, openlibrary/plugins/upstream/utils.py, and corresponding existing test files.
