Task: Make collection manifest configuration accept minimal values and preserve default file selection behavior.
Status: Implemented Sentinel for absent manifest metadata, explicit handling of empty and null manifests, and exclusion of external file symlinks. Updated unit tests for routing, ignore patterns, and symlinks.
Verification: PYTHONPATH=lib python -m pytest -q test/units/galaxy/test_collection.py (67 passed); git diff --check passed.
