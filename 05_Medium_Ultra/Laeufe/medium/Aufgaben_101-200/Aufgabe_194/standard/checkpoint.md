# Checkpoint

Task: Replace BlocklistDownloads constructor callbacks with Qt completion signals.

Completed:
- Made BlocklistDownloads a QObject with single_download_finished(object) and all_downloads_finished(int).
- Updated host and Brave adblock consumers to connect before initiate().
- Updated blockutils tests for signals, multiple listeners, empty batches, and QObject parenting.

Verification: pytest -q tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py — 38 passed, 13 skipped.
