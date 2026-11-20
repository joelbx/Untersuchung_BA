Task: Replace BlocklistDownloads constructor callbacks with QObject signals.
Status: Complete. BlocklistDownloads now emits single_download_finished(object) and all_downloads_finished(int). Both consumers connect before initiate(); tests cover local files and empty lists with QObject parent.
Verification: pytest -q tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py (38 passed, 13 skipped); git diff --check passed.
