# Checkpoint

Task: preserve safe internal collection symlinks during build and install, and expose tar member metadata from extraction helpers.
Status: implemented in `lib/ansible/galaxy/collection.py`; updated collection unit tests for preserved symlinks and added extraction coverage. `python -m pytest -q test/units/galaxy/test_collection.py` passes (60 tests).
