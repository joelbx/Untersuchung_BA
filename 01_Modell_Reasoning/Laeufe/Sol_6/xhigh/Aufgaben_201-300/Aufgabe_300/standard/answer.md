Implemented `override-validation=true` for the import API. The flag passes through `load()` to `validate_record()`, bypassing the publication year, independent publisher, and missing ISBN checks. Required fields and default validation remain in place. Added the case-insensitive `is_promise_item()` utility.

Relevant tests: **142 passed, 1 expected failure**.