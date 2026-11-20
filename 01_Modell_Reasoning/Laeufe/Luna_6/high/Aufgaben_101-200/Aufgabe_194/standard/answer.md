Updated `BlocklistDownloads` to inherit from `QObject` and emit `single_download_finished` and `all_downloads_finished` signals. Both consumers now connect handlers before starting downloads, and empty URL lists emit a completion count of `0`.

The focused tests passed: **2 passed**. `git diff --check` passed.