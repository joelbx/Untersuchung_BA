# Checkpoint

- Goal: Resolve `/lists/add` POST handling when request body fields conflict with query parameters.
- Constraints: Used checked-out repository code and existing tests only; did not inspect credentials or evaluator artifacts.
- Initial state: Working tree was clean; no `AGENTS.md` was found in the repository ancestry scan.
- Changes made: `ListRecord.from_input` parses a nonempty body with `parse_qs`, uses the first value for each field, excludes query values, applies defaults only when their key and nested descendants are absent, and safely filters malformed seeds. `utils.unflatten` now honors later assignments and resolves scalar/nested collisions according to write order.
- Verification: `pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py` passed (14 tests); `git diff --check` passed.
