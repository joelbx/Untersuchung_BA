Implemented `override-validation=true` for `/api/import`. It flows through `load()` to `validate_record()` and skips the publication year, independent publisher, and missing ISBN checks. Required-field checks remain active. Added the case-insensitive `is_promise_item()` utility.

**Validation:** 69 relevant tests passed, and `git diff --check` passed.