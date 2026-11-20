# Checkpoint

Task: replace BlocklistDownloads callbacks with QObject signals, update consumers and relevant tests.
Status: complete.
Changed: BlocklistDownloads now emits single_download_finished(object) and all_downloads_finished(int); host and Brave blockers connect before initiate; added tests for empty batches, QObject parent, and multiple listeners.
Verification: pytest -q tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py (39 passed, 13 skipped); git diff --check passed.
