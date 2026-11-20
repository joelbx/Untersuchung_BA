`BlocklistDownloads` now inherits from `QObject` and emits `single_download_finished(object)` and `all_downloads_finished(int)`. Both consumers connect their handlers before starting downloads, so local files and empty URL lists are handled correctly.

The focused test suite reported **38 passed, 13 skipped**; the updated signal tests passed on a final run. `git diff --check` is clean.