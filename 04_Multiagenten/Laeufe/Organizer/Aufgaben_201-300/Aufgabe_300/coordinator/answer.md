Implemented `override-validation=true` for the import POST endpoint. The flag passes through `load()` to `validate_record()` and bypasses publication year, “Independently Published,” and missing ISBN checks. Required fields remain enforced. I also added the case-insensitive `is_promise_item()` utility.

The relevant test suites passed: **102 passed, 1 expected failure**. No delegation was used.