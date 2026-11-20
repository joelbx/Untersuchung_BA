Task: preserve safe internal collection symlinks in build/install; expose TarInfo with extraction streams.
Status: implementation complete. Manifest walk records directory links without recursion; tar build preserves internal links with relative targets and copies external file targets. Install validates destination and link targets and restores safe links. Extraction helpers return member and stream.
Tests: PYTHONPATH=lib:test pytest -q test/units/galaxy/test_collection.py test/units/galaxy/test_collection_install.py -> 102 passed. git diff --check passed.
Delegation: none.
