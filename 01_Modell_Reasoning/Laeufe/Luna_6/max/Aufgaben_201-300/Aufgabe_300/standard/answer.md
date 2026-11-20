Implemented the `override-validation` query flag for `/import/api`. It bypasses the three requested checks while keeping required-field validation intact, and flows through `load()` to `validate_record()`.

Added case-insensitive `is_promise_item()` detection and tests for validation behavior, API forwarding, and promise records.

Verification passed: **114 focused tests**, **30 import API tests**, and `git diff --check`.