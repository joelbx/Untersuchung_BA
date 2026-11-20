# Debugging checkpoint

Task: restore efficient vaulted variable file loading while preserving uncached reads.

Status: investigating root cause and existing tests. `rg` is unavailable locally; using `find` and `grep`.

Root cause: `VariableManager.get_vars` loads every play `vars_files` entry with `cache=False`, which bypasses cache lookup and repeatedly decrypts vaulted files. `DataLoader.load_from_file` also stores parsed data unconditionally, even when caching was disabled. The loader's `_get_file_contents` returns `show_content=False` only for a vaulted file, which can select storage without another read. Existing `host_group_vars` uses `cache=True`, showing boolean caching remains an established pattern.

Hypothesis: add explicit `'none'` and `'vaulted'` policies in `load_from_file`, preserving boolean callers, then use `'vaulted'` for play `vars_files`. A cached vaulted file will skip `_get_file_contents` on repeat calls, while plain files and `'none'` calls remain uncached.

Reproduction: `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/test_dataloader.py -k 'cache_none or cache_vaulted'` failed before the patch: both the `'none'` vaulted read and `'vaulted'` plain read unexpectedly reused the cache (read count 1 vs expected 2).

Implementation: `DataLoader.load_from_file` now supports `'none'` and `'vaulted'` while retaining boolean behavior. `VariableManager` requests vaulted-only caching for play `vars_files`.

Verification: `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/test_dataloader.py test/units/vars/test_variable_manager.py` passed, 43 tests. Added a manager-level test confirming two variable resolutions read a vaulted file once.
