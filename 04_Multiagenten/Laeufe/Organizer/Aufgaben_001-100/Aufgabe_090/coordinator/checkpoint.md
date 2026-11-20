# Checkpoint

Resolved `/lists/add` form/query conflicts in `ListRecord.from_input` by parsing nonempty URL-encoded bodies with `parse_qs`, taking each key's first value, unflattening before filling absent defaults, and excluding query parameters. Empty bodies still use `web.input` defaults. Invalid or empty nested seed entries are ignored. Shared `unflatten` now lets the last assignment win, including parent/child collisions.

Validation: `pytest -q openlibrary/plugins/openlibrary/tests/test_lists.py openlibrary/plugins/upstream/tests/test_utils.py` passed (17 tests); `ruff check` and `git diff --check` passed.

No delegation used.
