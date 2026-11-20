# Checkpoint

Task: preserve internal collection symlinks in build and install, with safe path checks and tar member metadata.

Implemented in `lib/ansible/galaxy/collection.py`; updated and added regression tests in `test/units/galaxy/test_collection.py`.

TDD: focused new/changed tests failed before implementation (manifest expansion, regular tar members, non-symlink install, missing `_is_child_path`); then passed after implementation.

Verification: `PYTHONPATH=lib:test pytest -q test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py` passed, 103 tests. `git diff --check` passed.

Repository-wide check: `pytest -q` collected 3279 items with 17 collection errors. It was interrupted after 26.94 seconds as unrelated failures/errors accumulated: 8 failed, 67 passed, 62 errors, 159 rerun. Examples: `test/ansible_test/unit/test_diff.py` cannot import `ansible_test._internal`; integration module tests exit while parsing absent stdin JSON; `test/units/cli/test_galaxy.py` has TypeError errors. The full repository suite is therefore not verified green.
