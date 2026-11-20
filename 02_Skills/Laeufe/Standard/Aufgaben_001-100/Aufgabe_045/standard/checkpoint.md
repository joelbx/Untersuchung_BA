# Checkpoint

Task: Reject Python keywords in collection names and replace legacy identifier helpers.
Status: Implemented and verified.

Changes:
- Collection-name validation checks both segments with Python identifier and keyword rules and returns a boolean.
- Dependency resolution uses the shared validator; removed `_is_py_id`, `_is_fqcn`, and the related Python 2/3 compatibility block from `dataclasses.py`.
- Added validator and dependency-resolution regression cases for keywords and malformed identifiers.

Checks:
- `PYTHONPATH=lib:test pytest -q --tb=short test/units/utils/collection_loader/test_collection_loader.py` — 82 passed.
- `PYTHONPATH=lib:test pytest -q --tb=short test/units/galaxy/test_collection_install.py` — 37 passed.
- `git diff --check` — passed.
- Initial combined command `PYTHONPATH=lib:test pytest -q test/units/utils/collection_loader/test_collection_loader.py test/units/galaxy/test_collection_install.py` — failed with 1 failure and 14 setup errors in galaxy tests because the collection-loader suite reset the global finder before the galaxy suite. Running each suite in a separate process passes. No code behavior is left unverified by these suites.
