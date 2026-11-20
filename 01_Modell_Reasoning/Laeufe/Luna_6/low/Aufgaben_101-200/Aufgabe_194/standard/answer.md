Updated `BlocklistDownloads` to inherit from `QObject` and emit `single_download_finished(object)` and `all_downloads_finished(int)`. Both consumers and the existing test now connect through Qt signals, and the test covers an empty URL list emitting a count of zero.

Verification: `pytest -q tests/unit/components/test_blockutils.py` passed (2 tests), and `git diff --check` passed.