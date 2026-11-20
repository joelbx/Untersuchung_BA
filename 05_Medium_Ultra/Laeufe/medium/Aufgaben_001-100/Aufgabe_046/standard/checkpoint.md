Task: resolve module_common collection module_utils dependency resolution bug.
Status: implemented iterative dependency queue, legacy and collection locators, redirect shims and metadata handling, package synthesis, package relative import handling, clearer lookup errors, and six normalization.
Validation: python -m pytest -q --reruns 0 test/units/executor/module_common (51 passed).
Constraints observed: local code/tests only; git history, index baseline, and harness configuration unchanged.
