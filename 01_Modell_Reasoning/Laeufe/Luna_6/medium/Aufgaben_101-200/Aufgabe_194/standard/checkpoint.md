# Checkpoint

Implemented QObject-based `BlocklistDownloads` with `single_download_finished(object)` and `all_downloads_finished(int)`. Migrated both production consumers and the unit test to connect to signals; added coverage for empty URL batches.

Verification: `pytest -q tests/unit/components/test_blockutils.py` passed (1 test) before adding the empty-list case. Re-running after that addition.
