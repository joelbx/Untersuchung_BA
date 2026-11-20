# Checkpoint

Resolved the vars file cache regression in the checked-out repository.

- `DataLoader.load_from_file` now accepts `cache='none'` and `cache='vaulted'` while preserving existing boolean calls. `none` bypasses the cache without writing it. `vaulted` stores and reuses parsed whole-file vault contents, leaving plain files uncached.
- Play `vars_files` loading now uses `cache='vaulted'` so repeated vaulted files are read and decrypted once per loader.
- Added unit coverage for cache behavior and the vars manager call.

Validation: `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/test_dataloader.py test/units/vars/test_variable_manager.py test/units/plugins/inventory test/units/inventory` — 100 passed, 1 unrelated `crypt` deprecation warning. `git diff --check` passed. `rg` was unavailable; local `grep`/`find` were used instead.
