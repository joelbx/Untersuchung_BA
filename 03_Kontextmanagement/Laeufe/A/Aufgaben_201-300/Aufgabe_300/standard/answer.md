Implemented `override-validation=true` for the import API. It flows through `load()` to `validate_record()` and bypasses the publication year, “Independently Published,” and missing ISBN checks. Required fields still apply, and the original checks remain in place when the flag is absent or false.

Added the case insensitive `is_promise_item()` utility. All 117 relevant tests pass.