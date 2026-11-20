# Checkpoint

Task: Resolve collection FQCN validation accepting Python keywords.

Completed: Removed `_is_py_id`, `_is_fqcn`, and the Python 2 identifier fallback from `dataclasses.py`. Added `is_python_identifier` and tightened `AnsibleCollectionRef.is_valid_collection_name` to require exactly two valid, non-keyword Python identifiers. Dependency resolution now uses that validator.

Verification: `test/units/utils/collection_loader/test_collection_loader.py` passed (57 tests). The targeted validation check rejected `def.collection`, `return.module`, `assert.test`, and `import.utils`, accepted valid names, and confirmed boolean results. `test/units/cli/test_galaxy.py` and `test/units/galaxy/test_collection_install.py` had 136 passing and 4 failures, all in existing install tests asserting warning counts. `git diff --check` passed.
