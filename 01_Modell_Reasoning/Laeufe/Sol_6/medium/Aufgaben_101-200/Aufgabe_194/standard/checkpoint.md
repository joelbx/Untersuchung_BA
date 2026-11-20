Task: Replace BlocklistDownloads constructor callbacks with QObject signals for individual and batch completion.
Status: complete.
Changes: BlocklistDownloads now inherits QObject, accepts an optional parent, emits single_download_finished(object) and all_downloads_finished(int). Host and Brave adblock consumers connect their handlers before initiate(). Unit tests cover multiple listeners, parent, and empty lists.
Verification: pytest -q tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py (38 passed, 13 skipped); git diff --check passed.
Constraints observed: local repository and existing tests only; no git history, index baseline, or harness changes.
