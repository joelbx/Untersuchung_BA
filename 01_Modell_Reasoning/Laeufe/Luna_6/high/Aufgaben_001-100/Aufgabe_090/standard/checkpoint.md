# Checkpoint

Issue: Fix `/lists/add` handling of POST form bodies that conflict with query parameters.

Completed:
- `ListRecord.from_input()` now parses a nonempty URL-encoded body with `parse_qs`, selects the first value per field, and excludes query parameters from that path.
- Body defaults are omitted for parent keys that have nested body fields; body fields then override remaining defaults.
- Seed normalization skips empty or malformed nested values and ensures the returned seeds collection is a list.
- `utils.unflatten()` now lets later assignments overwrite an existing simple key.

Validation: `pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py` passed (14 tests); `git diff --check` passed.
