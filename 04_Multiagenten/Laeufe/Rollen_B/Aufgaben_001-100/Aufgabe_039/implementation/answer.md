Updated `Booknotes.update_work_id` so a populated target work ID leaves all booknotes unchanged and returns `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}`. The admin caller now preserves the dictionary response.

Added regression coverage for conflicts, successful updates, and dry-run rollback. All 5 tests in `openlibrary/tests/core/test_db.py` pass.