# Checkpoint

Objective: Restore selective file caching in `DataLoader.load_from_file` so `cache='none'` skips the internal cache and `cache='vaulted'` caches parsed vaulted files and reuses cached results.

Progress: Implemented cache mode handling with boolean compatibility, switched play `vars_files` to vaulted-only caching, and added loader tests for disabled caching, vaulted cache reuse, and plain-file behavior. Validation passed: 42 tests across `test_dataloader.py` and `test_variable_manager.py` using local pytest. `ansible-test` could not start because pytest-xdist is unavailable in the environment.
