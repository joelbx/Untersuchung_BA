# Checkpoint

Task: restore efficient vaulted variable file loading in `DataLoader.load_from_file` while preserving an uncached mode.

Status: implemented and verified. Repository has no `AGENTS.md`; working tree was clean at start.

Changes: `load_from_file` now supports `cache='none'` and `cache='vaulted'`, only inserts entries when the selected mode permits it, and recognizes vaulted entries when cache modes are mixed. `VariableManager` now uses vaulted-only caching for play `vars_files`. Added focused tests for uncached reads, vaulted reuse, and the call site.

Verification: `python -m pytest -q test/units/parsing test/units/vars test/units/plugins/inventory` passed (369 tests; two unrelated warnings). `git diff --check` passed.
