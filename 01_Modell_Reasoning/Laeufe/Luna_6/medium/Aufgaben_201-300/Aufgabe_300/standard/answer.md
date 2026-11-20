Implemented the import validation override and `is_promise_item(rec)`.

The `/import/api` endpoint reads `override-validation=true` and passes it through `load()` to `validate_record()`. When enabled, it skips publication year, independent publisher, and required ISBN checks. The promise item utility checks `source_records` case insensitively.

Focused tests passed: **54 passed**. `git diff --check` passed.