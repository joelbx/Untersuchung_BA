# Checkpoint

Task: Restore native OS filesystem directory scanning and add `utils.IsDirReadable`.

Implemented:
- Scanner traversal, stat, open, symlink resolution, ignore file checks, and audio discovery now use OS paths and operations. The walker converts roots to absolute paths.
- Added `utils.IsDirReadable` using `os.Open` and an immediate close; close errors are logged.
- Preserved sorted reads, entry error logging, directory skip rules, and Windows `$Recycle.Bin` skip behavior.
- Buffered the single walker error so callers can drain results before reading the error without deadlocking.
- Updated scanner tests for path-based signatures; added relative-root, missing-root, and utility tests.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./scanner ./utils`: passed (TagLib emitted an existing C++ deprecation warning).
- `git diff --check`: passed.
- `rg` unavailable (`/bin/bash: rg: command not found`); used local `grep` and `find`.
- An earlier run of the same Go test command was interrupted after the new missing-root test exposed the unbuffered error-channel deadlock. The buffer fix was applied and the command subsequently passed.
