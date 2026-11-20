Refactored `walkDirTree`, `loadDir`, and `isDirEmpty` to use a supplied `fs.FS`. The walker now returns result and error channels. `Scan` creates the media filesystem directly; `getRootFolderWalker` and `utils.IsDirReadable` were removed.

Added in-memory filesystem and error-channel coverage. `go test ./scanner ./utils` and `git diff --check` pass.