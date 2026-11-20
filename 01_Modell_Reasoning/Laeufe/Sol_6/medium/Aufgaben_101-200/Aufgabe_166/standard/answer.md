Updated `DataLoader.load_from_file` to support `cache='none'` and `cache='vaulted'`. The vault-only mode caches parsed vaulted files for later reads while leaving plain files uncached. The `vars_files` loader now uses that mode, avoiding repeated vault decryption.

Added regression tests and ran the relevant loader and variable manager tests: **41 passed**.