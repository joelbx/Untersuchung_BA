# Checkpoint

Task: Fix the `DataLoader.load_from_file` cache behavior for `cache='none'` and `cache='vaulted'` and verify with the repository's existing relevant tests.

Initial state: Repository at `/app`; no tracked working-tree changes reported before edits. `rg` is unavailable in this environment, so use `find`/`grep` for repository discovery.

Findings:
- `load_from_file` currently only uses `cache` to guard lookup; insertion is unconditional, so `cache=False` still grows `_FILE_CACHE` but never reuses it.
- `VariableManager` intentionally calls this with `cache=False` for `vars_files`; cache only vaulted files there to avoid repeated decryptions while preserving uncached reads for regular vars files.
- Other callers use boolean `True`/`False`, so preserve their behavior while adding string policies `none` and `vaulted` (and `all` for the existing general-cache behavior).

Implementation:
- Added `cache='none'`, `cache='vaulted'`, and `cache='all'` policies while preserving boolean cache arguments.
- Cache insertion now follows the selected policy; vaulted files are identified from the existing `show_content` signal and tracked so vaulted-only lookups reuse only vaulted entries.
- Changed vars-file loading to use `cache='vaulted'`.

Verification:
- `PYTHONPATH=lib:test python -m pytest -q test/units/parsing/test_dataloader.py` — 31 passed.
- `PYTHONPATH=lib:test python -m pytest -q test/units/vars/test_variable_manager.py` — 8 passed.
- `ansible-test units test/units/parsing/test_dataloader.py` could not launch pytest because pytest does not recognize the runner's `-n` option in this environment; the same module passed via direct pytest.
- `git diff --check` passed. Working tree contains the two intended source edits.
