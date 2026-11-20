Fixed `/lists/add` so a present POST body is parsed independently of the query string. Body fields override defaults, nested `seeds` fields no longer collide with the `seeds=[]` default, invalid seed entries are skipped, and repeated simple flattened assignments use the last value.

Added regression tests. All 17 relevant tests pass; Ruff and `git diff --check` pass.