# Checkpoint

Task: restore efficient vaulted variable file loading through `DataLoader.load_from_file` cache modes.

Initial state: repository was clean; `load_from_file` took a boolean `cache` parameter and wrote to `_FILE_CACHE` even with `cache=False`.

Changes:
- `DataLoader.load_from_file` accepts `none` and `vaulted`; default is `vaulted`. Existing boolean values remain supported. `none` bypasses reads and writes to the cache; `vaulted` caches only decrypted vaulted files.
- Host/group vars and play `vars_files` request vaulted-only caching.
- Added regression tests for repeated vaulted loads, uncached loads, plain files, and boolean compatibility.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/test_dataloader.py test/units/vars/test_variable_manager.py` passed (43 tests). `git diff --check` passed.
