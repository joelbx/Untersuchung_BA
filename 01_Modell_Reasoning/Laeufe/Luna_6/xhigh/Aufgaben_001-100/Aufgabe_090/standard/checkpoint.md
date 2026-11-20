# Checkpoint

Task: Resolve the `/lists/add` POST query/body conflict.

Completed:
- `ListRecord.from_input` now parses a nonempty URL-encoded body with `parse_qs`, takes the first value per field, and never combines it with query input.
- Body defaults are omitted when they would be ancestors of flattened body keys; empty-body requests use `web.input` defaults.
- Seed handling normalizes only nonempty strings and valid keyed objects, returning a list and skipping malformed entries.
- `utils.unflatten` now lets later assignments overwrite prior simple values and safely reconstructs nested values after scalar assignments.
- Added focused regression tests for the input selection and unflatten precedence behavior.

Verification: `pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py` passed (17 passed); `git diff --check` passed.
