# Checkpoint

Implemented collection symlink preservation in tar builds and safe restoration during artifact install. The manifest walker records internal directory links without descending into them. Extract helpers now expose `(TarInfo, stream)` and path validation checks destination and link targets. Updated existing assertions and added build/install round trip and escaping-link coverage.

Verification: `PYTHONPATH=lib:test pytest -q test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py --reruns 0` passed (102 tests). `git diff --check` passed.
