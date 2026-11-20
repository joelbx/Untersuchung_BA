`BlocklistDownloads` now inherits `QObject` and emits `single_download_finished(object)` and `all_downloads_finished(int)`. Both consumers connect their handlers before starting downloads, including when the URL list is empty.

The relevant tests passed: **39 passed, 13 skipped**. `git diff --check` also passed.