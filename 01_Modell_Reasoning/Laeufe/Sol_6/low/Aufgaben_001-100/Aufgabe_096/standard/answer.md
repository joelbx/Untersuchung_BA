Updated `atomic_move()` so newly created files use `0600` under a `0022` umask. Modules that accept `mode` now warn when they omit it; a later explicit mode call clears the warning for that path.

Added focused tests and updated existing expectations for preserving an existing file’s mode. **45 relevant tests passed** with `PYTHONPATH=lib`.