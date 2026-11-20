Fixed the vars file cache regression. `load_from_file` now supports `cache='none'` without writing to the cache and `cache='vaulted'` to reuse parsed vaulted files. Play `vars_files` now uses the vaulted mode.

Validation passed: **43 relevant unit tests** and `git diff --check`.