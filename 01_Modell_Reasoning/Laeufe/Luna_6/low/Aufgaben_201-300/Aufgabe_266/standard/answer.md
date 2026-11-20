Implemented `find_staged_or_pending` with the fixed `('amazon', 'idb')` source tuple, and updated ISBN resolution to check matching staged or pending records locally using both ISBN forms. Added coverage for source and status filtering.

`pytest -q openlibrary/tests/core/test_imports.py` passed: 6 tests. `git diff --check` passed. Black wasn’t available in the environment.