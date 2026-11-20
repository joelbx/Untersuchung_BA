Fixed `Booknotes.update_work_id` so a destination conflict leaves every booknote unchanged and returns `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}`. The [admin caller](/app/openlibrary/plugins/admin/code.py) now preserves that dictionary.

Added regression tests in [test_db.py](/app/openlibrary/tests/core/test_db.py). All 6 relevant tests pass.