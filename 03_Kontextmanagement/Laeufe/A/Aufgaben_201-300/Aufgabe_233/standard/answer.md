Refactored directory traversal to use `fs.FS`. `walkDirTree` now accepts a filesystem and returns result and error channels; `loadDir`, `isDirEmpty`, and the walker’s filesystem checks use the same abstraction. `Scan` starts the walker directly, and `utils.IsDirReadable` was removed.

Added virtual filesystem and error coverage. `go test ./scanner ./utils` and `git diff --check` passed.