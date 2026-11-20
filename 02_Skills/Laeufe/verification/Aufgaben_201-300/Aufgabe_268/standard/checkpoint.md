# Checkpoint

Issue: GUIProcess startup errors omitted the command and error type.

Changed `qutebrowser/misc/guiprocess.py` so `_on_error` formats the capitalized process name, quoted command, specific QProcess error wording, and process error detail. On non-Windows, FailedToStart with `No such file or directory` or `Permission denied` adds the requested executable hint. Existing non-Windows crash notification remains handled by `_on_finished` to avoid a duplicate notification.

Updated `tests/unit/misc/test_guiprocess.py` to cover the real nonexistent-command case, all five requested error codes, and hint behavior across platform and error-detail cases.

Verification:
- `pytest -q --reruns 0 --tb=short tests/unit/misc/test_guiprocess.py`: exit 0, 32 passed.
- `git diff --check`: exit 0.

The first test run (`pytest -q tests/unit/misc/test_guiprocess.py`) failed in 11 new cases because expected error logs were not captured by the test fixture; the tests now capture those logs. `rg` is unavailable (`/bin/bash: rg: command not found`); local searches used `find` and `grep`.
