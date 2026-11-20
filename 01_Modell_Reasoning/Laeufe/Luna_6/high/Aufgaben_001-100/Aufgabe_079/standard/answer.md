Restored directory scanning to native OS operations with absolute paths, including recursive traversal, symlink handling, audio detection, ignore rules, and existing error reporting. Added `utils.IsDirReadable` and updated scanner tests for the new path based API.

Validation passed: `go test ./scanner ./utils` and `git diff --check`.