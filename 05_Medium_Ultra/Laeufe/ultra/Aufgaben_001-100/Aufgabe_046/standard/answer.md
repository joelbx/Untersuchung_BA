Resolved collection `module_utils` resolution in [module_common.py](/app/lib/ansible/executor/module_common.py:688). Dependency discovery now uses a queue and separate legacy and collection locators. Redirects generate shims, package imports retain their relative import behavior, missing package initializers are synthesized, and unresolved imports report the paths tried.

Added regression coverage in [test_collection_module_utils.py](/app/test/units/executor/module_common/test_collection_module_utils.py:1) and updated existing payload expectations. **126 affected tests passed**; `git diff --check` and Python compilation passed.

I delegated test additions and read-only loader and code reviews, then integrated and verified the final patch.