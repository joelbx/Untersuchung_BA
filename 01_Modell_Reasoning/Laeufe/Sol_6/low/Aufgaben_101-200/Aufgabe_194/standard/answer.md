`BlocklistDownloads` now inherits from `QObject` and emits `single_download_finished(object)` and `all_downloads_finished(int)`. Both consumers connect their handlers before starting downloads, including for synchronously completed local files. The empty URL case emits the batch completion signal with a count of zero.

Verification: 38 relevant tests passed, 13 skipped; `git diff --check` passed.