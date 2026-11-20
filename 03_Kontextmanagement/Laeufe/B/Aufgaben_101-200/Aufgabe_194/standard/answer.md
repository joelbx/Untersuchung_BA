`BlocklistDownloads` now inherits `QObject` and emits signals for individual downloads and batch completion. Both adblock consumers connect their handlers before starting downloads.

Verification: 38 relevant tests passed, 13 were skipped, and `git diff --check` passed.