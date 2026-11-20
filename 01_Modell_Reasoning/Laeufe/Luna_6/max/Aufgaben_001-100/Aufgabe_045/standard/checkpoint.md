# Checkpoint

Task: Fix FQCN collection-name validation so Python keywords are rejected and both segments are valid Python identifiers.

Completed: Removed `_is_py_id`, `_is_fqcn`, and their identifier-specific Python 2/3 fallback from `dataclasses.py`. Dependency resolution now uses `AnsibleCollectionRef.is_valid_collection_name`. Added `is_python_identifier`; the validator checks exactly two identifier segments, rejects keywords in either segment, and returns `False` for conversion failures.

Verification: `ansible-test units --local --python 3.9 --no-pip-check test/units/utils/collection_loader/test_collection_loader.py test/units/galaxy/test_collection_install.py` passed (87 tests). Manual validation covered valid names, `def`, `return`, `assert`, `import`, malformed segments, extra segments, and a trailing newline. `py_compile` and `git diff --check` passed.
