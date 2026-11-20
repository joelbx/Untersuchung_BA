Updated `atomic_move()` so new files receive `_DEFAULT_PERM = 0600` masked by the current umask. Modules that accept `mode` now warn for each new path when the argument is omitted; a later `set_mode_if_different()` call clears that path’s warning.

The relevant tests passed: **47 passed**. `git diff --check` also passed.