Fixed the vars file caching regression. `DataLoader.load_from_file` now supports `cache='none'` without adding a cache entry and `cache='vaulted'` to cache decrypted vault files. The variable manager uses vaulted caching for play vars files, avoiding repeated reads and decryption.

Added regression tests for both modes and cache reuse. All 42 relevant tests pass, and `git diff --check` passes.