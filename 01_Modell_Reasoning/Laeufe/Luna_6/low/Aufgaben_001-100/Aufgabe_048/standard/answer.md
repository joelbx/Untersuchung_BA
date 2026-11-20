Implemented structured plugin resolution metadata, context-carrying plugin errors, tombstone handling, centralized deprecation formatting, and updates to the task executor, action loader, and Jinja plugin lookup.

Validation: compilation and `git diff --check` passed. The focused suite passed (68 tests). A broader run had 69 passes and 2 failures in template JSON conversion and display warning output; those failures were unrelated to the modified code.

The checkpoint is recorded in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).