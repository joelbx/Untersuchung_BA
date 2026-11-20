Task: Add override-validation support to /import/api and is_promise_item utility.
Status: completed.
Changes: POST reads override-validation=true and passes boolean to add_book.load; load forwards to validate_record; requested checks are skipped only with override; is_promise_item checks source_records case-insensitively.
Verification: 116 relevant tests passed; git diff --check passed.
