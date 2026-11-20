Implemented the module-level `extra_suffixes_workaround` and updated `WebEnginePage.chooseFiles` to pass a deduplicated merged suffix list to `super().chooseFiles` in one call. Updated the unit tests to use the new helper and invoke `chooseFiles` with `None` for `self`.

Validation: **20 focused tests passed** with `QT_QPA_PLATFORM=offscreen`; compile and whitespace checks passed. The first test attempt aborted during Qt GUI initialization.

The required checkpoint is at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md). It is ignored by the repository’s `.git/info/exclude`.