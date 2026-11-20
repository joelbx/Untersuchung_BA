`BlocklistDownloads` now inherits from `QObject` and emits `single_download_finished(object)` and `all_downloads_finished(int)`. The host and Brave adblock consumers connect their handlers before starting downloads, including for empty batches. Tests cover multiple listeners, empty batches, and QObject parenting.

Verification: 38 passed, 13 skipped in the affected component tests.