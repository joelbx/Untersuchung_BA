Fixed the vars file caching regression. `DataLoader.load_from_file` now supports `cache='none'` without storing a result and `cache='vaulted'` to reuse parsed vaulted files. Play `vars_files` now uses the vaulted mode, avoiding repeated reads and decryption.

Validation: 100 relevant tests passed, and `git diff --check` passed.