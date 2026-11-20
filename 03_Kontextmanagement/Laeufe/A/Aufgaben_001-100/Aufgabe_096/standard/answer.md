Updated `atomic_move()` so newly created files receive `0600` permissions with umask `0022`. Modules that accept `mode` now warn for each created path when it is omitted; a later `set_mode_if_different()` call clears that path’s warning.

The relevant existing tests and added coverage pass: **66 passed**.