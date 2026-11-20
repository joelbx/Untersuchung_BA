Implemented the module-level `make_date_string` and added `patron_check_ins.is_valid` to require a nonempty `id` and a `year` or `data` field. The existing `check_ins` method delegates to the new formatter.

Validation: `pytest -q openlibrary/plugins/upstream/tests/test_checkins.py` passed (5 tests), and `git diff --check` passed.