Updated Booknotes work ID handling to check for an existing target first and leave the table unchanged on conflict. Conflicts return `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}`. Added a regression test; other models retain their existing behavior.

Verification: `python -m pytest openlibrary/tests/core/test_db.py -q` passed (3 tests), and `git diff --check` passed.