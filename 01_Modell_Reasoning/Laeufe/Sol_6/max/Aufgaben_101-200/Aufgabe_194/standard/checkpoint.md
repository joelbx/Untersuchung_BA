# BlocklistDownloads Qt signals

Implemented QObject inheritance and `single_download_finished(object)` / `all_downloads_finished(int)` signals. Host and Brave blockers now connect handlers before initiating downloads. Updated blockutils tests for multiple listeners, local file completion, empty lists, and QObject parent support.

Verification: `DISPLAY=:99 QT_QPA_PLATFORM=offscreen pytest -p no:xvfb -q -rs tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py -k 'not benchmark'` completed with 37 passed and 13 skipped (optional `adblock` package unavailable). `git diff --check` passed.
