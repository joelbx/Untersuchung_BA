# Checkpoint

Implemented `load_from_file` cache modes: `none` never stores parsed data, while `vaulted` caches encrypted files and reuses those results. Updated `vars_files` loading to request `vaulted` caching, retaining its no-cache behavior for ordinary files. Added focused unit coverage for cache avoidance and vaulted cache reuse.

Validation: `python -m pytest -q test/units/parsing/test_dataloader.py` passed (33 tests); `git diff --check` passed.
