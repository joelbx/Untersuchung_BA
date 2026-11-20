Implemented `override-validation=true` for `/import/api`. The flag now flows through `load()` to `validate_record()` and skips the requested publication year, independent publisher, and missing ISBN checks. Added case-insensitive `is_promise_item(rec)`.

The override defaults to `False`. Existing add-book and import API tests passed: **74 passed**. `compileall` and `git diff --check` also passed.

Checkpoint: [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md)