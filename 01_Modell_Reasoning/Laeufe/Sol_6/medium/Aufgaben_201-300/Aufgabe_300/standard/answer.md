Implemented `override-validation=true` for the import API. The flag passes through `load()` to `validate_record()` and skips the publication year, independently published, and required ISBN checks. Without the flag, the existing checks still apply. Added the case-insensitive `is_promise_item()` utility.

Verification: 99 tests passed, 1 expected failure; `git diff --check` passed.