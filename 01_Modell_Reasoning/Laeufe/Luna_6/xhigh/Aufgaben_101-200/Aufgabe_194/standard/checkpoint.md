# Checkpoint

## Objective
Replace `BlocklistDownloads` callback constructor arguments with Qt signals, migrate existing consumers, and run the relevant existing tests.

## Findings
- `BlocklistDownloads` is in `qutebrowser/components/utils/blockutils.py`.
- Production consumers are in `qutebrowser/components/adblock.py` and `qutebrowser/components/braveadblock.py`.
- The existing unit test is `tests/unit/components/test_blockutils.py` and currently uses callbacks.
- No `AGENTS.md` files were found.

## Next steps
Implemented `BlocklistDownloads` as a `QObject` with the two requested signals, updated host and Brave blocker connections, and migrated the existing blockutils test to connect slots. Empty URL batches emit `all_downloads_finished(0)`.

Existing unit tests for blockutils, host adblocking, and Brave adblocking completed: 37 passed, 13 skipped. Final diff and whitespace checks are complete.
