Fixed `Booknotes.update_work_id` so a target `work_id` conflict leaves every booknote unchanged. It now returns `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}` for a conflict. The admin redirect summary also preserves the returned dictionary.

Verification: all 7 tests in `openlibrary/tests/core/test_db.py` passed.