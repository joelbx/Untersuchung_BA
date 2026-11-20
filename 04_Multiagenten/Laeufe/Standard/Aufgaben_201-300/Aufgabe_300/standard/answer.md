Implemented `override-validation=true` for the import API. The flag passes through `load()` to `validate_record()`, where it skips the publication year, independently published, and missing ISBN checks. Required fields and the default validation behavior remain in place.

Added `is_promise_item(rec)` with case-insensitive `promise:` prefix matching. The relevant tests pass: **116 passed**.