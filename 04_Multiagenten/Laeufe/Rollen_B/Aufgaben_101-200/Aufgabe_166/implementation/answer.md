Updated `DataLoader.load_from_file` so `cache='none'` bypasses cache reads and writes, while `cache='vaulted'` caches parsed vaulted files for reuse. `vars_files` now uses vaulted caching, avoiding repeated reads and decryption. Existing boolean cache callers retain their behavior.

Added cache and vault regression tests. All 43 relevant parsing and variable manager tests pass.