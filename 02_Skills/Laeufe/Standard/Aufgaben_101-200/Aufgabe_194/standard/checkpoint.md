# Checkpoint

Task: Replace `BlocklistDownloads` constructor callbacks with Qt signals and update consumers/tests.

Initial inspection: `BlocklistDownloads` lives in `qutebrowser/components/utils/blockutils.py`; callers are `adblock.py`, `braveadblock.py`, and `tests/unit/components/test_blockutils.py`. `rg` is unavailable (`/bin/bash: rg: command not found`), so repository searches use `grep`/`find`.

Implemented: `BlocklistDownloads` now inherits `QObject`, takes an optional QObject parent, emits `single_download_finished(object)` and `all_downloads_finished(int)`, and the host/Brave callers connect their handlers before initiation. Tests cover multiple listeners, completion counts, file closure, empty input, and QObject parenting.

Verification: `pytest -q tests/unit/components/test_blockutils.py tests/unit/components/test_adblock.py tests/unit/components/test_braveadblock.py` passed (38 passed, 13 skipped). `python -m compileall -q qutebrowser/components/utils/blockutils.py qutebrowser/components/adblock.py qutebrowser/components/braveadblock.py tests/unit/components/test_blockutils.py` and `git diff --check` passed.
