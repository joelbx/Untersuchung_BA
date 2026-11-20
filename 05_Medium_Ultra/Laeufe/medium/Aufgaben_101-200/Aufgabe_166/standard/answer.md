Updated `DataLoader.load_from_file` so `cache='none'` leaves the file cache untouched and `cache='vaulted'` reuses parsed vaulted files. Play `vars_files` now uses vaulted caching, avoiding repeated reads and decryption.

Added regression tests for both cache modes and repeated `vars_files` loading. All 44 relevant tests pass.