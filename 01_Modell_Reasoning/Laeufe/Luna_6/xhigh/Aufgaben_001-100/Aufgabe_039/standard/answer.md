Implemented the booknotes conflict fix. `Booknotes.update_work_id` now rolls back the update on a uniqueness conflict, preserves every record, and returns `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}`. The admin report now keeps that dictionary result.

Added a regression test; the existing bookshelf collision behavior remains unchanged.

Verification: `pytest -q openlibrary/tests/core/test_db.py` — **3 passed**. `git diff --check` passed.

Changed: [booknotes.py](/app/openlibrary/core/booknotes.py:13), [admin/code.py](/app/openlibrary/plugins/admin/code.py:247), [test_db.py](/app/openlibrary/tests/core/test_db.py:82).