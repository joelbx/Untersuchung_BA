Task: resolve module_common collection module_utils dependency resolution.
Status: implemented queue-based dependency collection, legacy/collection locators, redirect shims and metadata handling, relative package imports, synthesized package initializers, and clearer lookup errors.
Verification: PYTHONPATH=lib python -m pytest test/units/executor/module_common -q --disable-warnings --tb=short --maxfail=1 (51 passed); py_compile passed.
