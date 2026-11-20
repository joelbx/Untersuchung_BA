Updated `DataLoader.load_from_file` so `cache='none'` bypasses the file cache and `cache='vaulted'` caches parsed vaulted files for reuse. The `vars_files` loader now uses vaulted caching, avoiding repeated reads and decryption. Existing boolean cache behavior remains supported.

Added focused cache tests. All 43 relevant tests pass, and `git diff --check` is clean.