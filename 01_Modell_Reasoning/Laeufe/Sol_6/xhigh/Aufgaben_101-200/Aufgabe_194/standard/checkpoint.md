# Checkpoint

- Task: replace `BlocklistDownloads` constructor callbacks with Qt signals.
- Found implementation in `qutebrowser/components/utils/blockutils.py`, consumers in `adblock.py` and `braveadblock.py`, and unit tests in `tests/unit/components/test_blockutils.py`.
- Implemented `QObject` inheritance, `single_download_finished(object)`, and `all_downloads_finished(int)`; connected both consumers before `initiate()`.
- Updated unit coverage for multiple listeners, file lifetime, batch count, empty URL lists, and QObject parenting.
- Verification: `pytest -q tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py` completed with 38 passed and 13 skipped (optional Brave adblock dependency unavailable). `git diff --check` passed.
