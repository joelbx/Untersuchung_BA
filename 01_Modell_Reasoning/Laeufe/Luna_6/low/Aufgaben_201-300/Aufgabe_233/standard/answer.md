Refactored scanner directory traversal to use `fs.FS` for directory reads, stats, ignore markers, symlink checks, and readability. `Scan` now creates the filesystem and starts the walker directly; `isDirEmpty` and `loadDir` accept `fs.FS`. Removed `getRootFolderWalker` and `utils.IsDirReadable`.

Verification: `go test ./scanner ./utils/...` passed. `git diff --check` passed.