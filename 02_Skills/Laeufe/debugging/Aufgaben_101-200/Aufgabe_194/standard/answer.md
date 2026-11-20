`BlocklistDownloads` now inherits from `QObject` and emits `single_download_finished(object)` and `all_downloads_finished(int)`. Both adblock consumers connect their handlers before starting downloads. Regression tests cover multiple listeners, a QObject parent, and empty URL lists.

The affected test suite passed: **38 passed, 13 skipped**. The Brave tests were skipped by the local environment.