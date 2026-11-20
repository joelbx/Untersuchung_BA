# Checkpoint

Task: migrate `BlocklistDownloads` from constructor callbacks to Qt signals.

Completed:
- `BlocklistDownloads` now inherits `QObject`, accepts `urls` plus optional `parent`, and exposes `single_download_finished(object)` and `all_downloads_finished(int)`.
- Successful file downloads emit the single-download signal; batch completion emits the count, including `0` for empty URL lists.
- Host blocker and Brave ad blocker consumers connect handlers with Qt's `connect()` before initiating downloads.
- Updated the existing blockutils tests to use signals and cover empty-list completion.

Verification: `python -m pytest tests/unit/components/test_blockutils.py` passed (2 tests); `git diff --check` passed.
