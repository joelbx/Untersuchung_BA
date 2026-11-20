Task: Fix module_common collection module_utils resolution, redirects, package imports, payload assembly, and diagnostics.
Status: Implemented queue-based dependency discovery with legacy and collection locators. Added redirect shims, metadata handling, real package initializer loading, missing initializer synthesis, relative import correction, six normalization, and clearer errors.
Verification: 59 module_common unit tests passed. collections_relative_imports playbook passed locally (3 tasks). git diff --check and py_compile passed.
Files changed: lib/ansible/executor/module_common.py; test/units/executor/module_common/test_recursive_finder.py; new test/units/executor/module_common/test_collection_module_utils.py.
Constraints honored: local code/tests only; no git history, index, or harness configuration changes.
