# Checkpoint

Task: replace `BlocklistDownloads` completion callbacks with Qt signals and update consumers.

Initial state: clean working tree. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use `grep`.

Changed `BlocklistDownloads` to inherit `QObject` and emit `single_download_finished(object)` and `all_downloads_finished(int)`. Updated both production callers and the blockutils tests to connect signals before initiation. Added coverage for multiple listeners, QObject parent, and an empty URL list.

Final verification after all code edits: `pytest -q tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py` exited 0: 38 passed, 13 skipped. `git diff --check` exited 0.
