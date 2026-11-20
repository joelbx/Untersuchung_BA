Implemented the validation override through `/import/api`, `load()`, and `validate_record()`. When enabled, it bypasses publication year, “Independently Published,” and required ISBN checks. Added the case insensitive `is_promise_item()` utility.

Existing tests passed: add-book **48 passed**, import API **6 passed**. `git diff --check` is clean.