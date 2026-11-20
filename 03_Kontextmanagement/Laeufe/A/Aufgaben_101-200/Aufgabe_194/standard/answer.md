`BlocklistDownloads` now inherits from `QObject` and emits `single_download_finished(object)` and `all_downloads_finished(int)`. Both ad blocker consumers connect their handlers before starting downloads. The tests also cover multiple listeners and empty URL lists.

Relevant tests: **38 passed, 13 skipped**. `git diff --check` passed.