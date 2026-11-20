Fixed `Booknotes.update_work_id` so a target `work_id` conflict preserves every booknote and returns `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}`. Added regression tests for collisions, a successful update, and dry run behavior.

Verification: all 6 tests in [test_db.py](/app/openlibrary/tests/core/test_db.py) passed; `git diff --check` passed.