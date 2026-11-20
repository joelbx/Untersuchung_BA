Updated `atomic_move()` so newly created files use `_DEFAULT_PERM = 0o0600` masked by the current umask. When a module accepts `mode` but omits it, the created path is tracked and `_return_formatted()` emits the required warning. A later `set_mode_if_different()` call removes that path from tracking.

Updated the relevant tests. All 67 focused tests pass, and `git diff --check` passes.