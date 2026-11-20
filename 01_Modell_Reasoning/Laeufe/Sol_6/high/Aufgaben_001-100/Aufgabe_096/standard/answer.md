Fixed `atomic_move()` so newly created files receive `0600` under umask `0022`. Modules that accept `mode` now emit the specified warning for each new path when `mode` is omitted; a later `set_mode_if_different()` call removes that path from warning tracking.

Updated the relevant tests. The `module_utils/basic` suite passed: **299 passed, 14 skipped**.