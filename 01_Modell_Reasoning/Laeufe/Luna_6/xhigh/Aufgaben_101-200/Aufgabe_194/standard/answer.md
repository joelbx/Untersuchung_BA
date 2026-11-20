Implemented the Qt signal interface for `BlocklistDownloads`, including `all_downloads_finished(0)` for empty URL lists. Updated both blocker consumers to connect before initiation and migrated the existing unit test.

Validation: 37 passed, 13 skipped; `git diff --check` passed.

Changed [blockutils.py](/app/qutebrowser/components/utils/blockutils.py), [adblock.py](/app/qutebrowser/components/adblock.py), [braveadblock.py](/app/qutebrowser/components/braveadblock.py), and [test_blockutils.py](/app/tests/unit/components/test_blockutils.py).