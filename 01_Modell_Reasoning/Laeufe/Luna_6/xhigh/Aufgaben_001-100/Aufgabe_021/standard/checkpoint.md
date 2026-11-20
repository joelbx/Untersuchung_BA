# Checkpoint

Task: Improve typing and seed handling in the List model and related list plugin helpers.

Initial state: Repository inspection started. No files changed yet except this checkpoint.

Plan: Read repository guidance, inspect List/Seed implementation and relevant tests, make narrowly scoped typing/normalization fixes, then run the existing list tests.

Findings:
- `SeedDict` currently lives in the plugin module, while `List` accepts untyped seeds and compares dicts directly.
- Subject path normalization is duplicated in `ListRecord`, the JSON seed processor, and `get_seed_info`.
- `get_export_list()` currently returns only populated categories and can treat subject strings as entity objects.
- `get_seeds()` passes dict references through as if they were loaded documents.
- Existing related tests are in `openlibrary/tests/core/test_lists_model.py`, `openlibrary/tests/core/lists/test_model.py`, and `openlibrary/plugins/openlibrary/tests/test_lists.py`.

Implementation complete:
- Added `SeedDict`, `SeedSubjectString`, the subject string type guard, and shared subject normalization.
- Typed List and Seed APIs; normalized seed add/remove/lookup behavior and loaded object references for seed wrappers.
- Made export output always include authors, works, and editions, with loaded records filtered by entity type.
- Added helper return annotations for `urlsafe()` and `_get_ol_base_url()`.

Verification:
- Existing list tests: 11 passed.
- Ruff, `git diff --check`, and Python compilation passed.
- Mypy on the two changed list modules with imports skipped passed. Full mypy traversal reports unavailable third-party stubs (requests, yaml, and others).
