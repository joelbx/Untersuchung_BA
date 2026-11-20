Refactored `walkDirTree`, `loadDir`, and `isDirEmpty` to use a supplied `fs.FS`. The walker now returns result and error channels, and `Scan` sets it up directly. Removed `utils.IsDirReadable` and added a virtual filesystem test.

`go test ./scanner ./utils` and `git diff --check` passed. No delegation was used.