Updated `Booknotes.update_work_id` so an existing target work ID leaves every booknote unchanged and returns `{"rows_changed": 0, "rows_deleted": 0, "failed_deletes": 1}`. The update also rolls back if a collision occurs during the database operation. The admin redirect summary now uses the dictionary result.

Added tests for conflicts, successful updates, and dry runs. All 6 relevant tests pass.