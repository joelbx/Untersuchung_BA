Implemented predictable no-log sanitization:

- `remove_values` now redacts string values only, preserves mapping keys and scalar values, and traverses deep containers iteratively.
- Added `sanitize_keys` for nested mapping keys, including exact-key sentinel replacement, ignore keys, and `_ansible` exemptions.
- URI response keys are sanitized only when `no_log_values` is present, using `NO_MODIFY_KEYS`.
- Date values remain unchanged during redaction; JSON serialization handles their ISO format.

The focused redaction, output, and text converter tests passed: **425 passed**. The broader `test/units/module_utils/basic` run reported 22 failures involving warning and deprecation output accumulated across tests; the focused output tests pass. `py_compile` and `git diff --check` passed.

Checkpoint: `.codex-role-output/checkpoint.md`.