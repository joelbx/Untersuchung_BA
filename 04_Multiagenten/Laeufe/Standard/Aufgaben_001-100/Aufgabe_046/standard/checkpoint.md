Task: Fix collection module_utils dependency resolution in module_common.
Status: complete.
Changes: queue-based finder; legacy and collection locators; redirect shims with deprecation/tombstone handling; package initializer relative imports; synthesized package files; clearer lookup errors; six normalization. Added focused locator and package synthesis tests.
Verification: PYTHONPATH=lib pytest -q test/units/executor/module_common (52 passed).
Constraints observed: local repository/tests only; no git history, index, or harness changes.
