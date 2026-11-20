Implemented `BlocklistDownloads` as a `QObject` with `single_download_finished(object)` and `all_downloads_finished(int)` signals. Updated both consumers to connect before initiating downloads, and added a test confirming an empty URL list emits `all_downloads_finished(0)`.

Verification: `pytest -q tests/unit/components/test_blockutils.py` — 2 passed.