# Checkpoint

Task: Fix `DataLoader.load_from_file` cache behavior for `cache='none'` and `cache='vaulted'`.

Completed:
- Added string cache modes while preserving the legacy boolean behavior.
- `cache='none'` always reads and parses without reading from or writing to `_FILE_CACHE`.
- `cache='vaulted'` reuses cache hits and stores parsed data only when file loading identified decrypted vault data.
- Updated play `vars_files` loading to use vaulted-only caching.
- Added unit coverage for no-cache and vaulted-only caching behavior.

Verification:
- `PYTHONPATH=lib:test/lib python -m pytest -q -o addopts='' test/units/parsing/test_dataloader.py` — 33 passed.
- `PYTHONPATH=lib:test/lib python -m pytest -q -o addopts='' test/units/vars/test_variable_manager.py` — 8 passed.
- `git diff --check` — passed.
- `ansible-test units` could not run because `pytest-xdist` is unavailable (`-n auto` is unrecognized).
