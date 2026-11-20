Updated [module_common.py](/app/lib/ansible/executor/module_common.py) to resolve `module_utils` dependencies through a queue and separate legacy and collection locators. The payload now handles collection redirects, package initializer imports, missing intermediate `__init__.py` files, and clearer missing import errors. Added focused coverage in [test_recursive_finder.py](/app/test/units/executor/module_common/test_recursive_finder.py).

Verification: **57 tests passed** in `test/units/executor/module_common`; `git diff --check` passed.

I adopted agent-1’s implementation patch, then manually corrected its locator interfaces, collection error handling, diagnostics, and tests.