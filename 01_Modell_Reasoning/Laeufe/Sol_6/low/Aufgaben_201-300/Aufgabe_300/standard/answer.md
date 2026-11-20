Implemented `override-validation=true` for `POST /import/api`. The flag now passes through `load()` to `validate_record()` and skips the publication year, independent publisher, and missing ISBN checks. Required fields and the default validation behavior remain in place. Added the case-insensitive `is_promise_item()` utility.

Relevant tests passed: **62 passed**.