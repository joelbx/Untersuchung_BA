Fixed the cache regression. `cache='vaulted'` now reuses a cached result only when that entry came from a vaulted file, so an earlier plain-file load cannot leave `vars_files` stale. Added a regression test for that sequence.

The reviewer’s exact test command passed: **44 passed**. `git diff --check` also passed.