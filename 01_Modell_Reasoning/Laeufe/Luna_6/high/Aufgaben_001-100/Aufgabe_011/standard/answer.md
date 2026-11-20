Implemented the reported fixes across module error handling, YAML constructors, Templar overrides, lookup messages, deprecations, timeout evaluation, and early CLI errors.

The focused existing suites passed: **125 tests**. Compile checks and `git diff --check` also passed. `test_deprecate_warn.py` still reports 7 failures: its assertions read the module-side warning accumulator, while this run’s controller context delegates deprecation collection to `Display`.

The required checkpoint is at `.codex-role-output/checkpoint.md`.