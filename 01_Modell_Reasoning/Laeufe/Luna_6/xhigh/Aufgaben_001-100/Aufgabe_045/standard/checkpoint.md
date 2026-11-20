# Checkpoint

Issue: Collection FQCN validation accepts Python reserved keywords.

Changes made:
- Added `is_python_identifier` beside collection reference validation and made `AnsibleCollectionRef.is_valid_collection_name` require two valid, non-keyword Python identifiers.
- Removed `_is_py_id`, `_is_fqcn`, their Python 2 fallback code, and routed dependency classification through `AnsibleCollectionRef.is_valid_collection_name`.

Verification:
- `test/units/utils/collection_loader/test_collection_loader.py`: 57 passed on Python 3.9.
- `test/units/galaxy/test_collection.py`: 43 passed on Python 3.9.
- Default Python matrix attempt could not start Python 3.8 tests because pytest and PyYAML are unavailable there.
