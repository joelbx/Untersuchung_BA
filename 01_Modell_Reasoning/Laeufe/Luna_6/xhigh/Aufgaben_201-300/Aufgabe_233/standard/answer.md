Refactored directory traversal to use `fs.FS`. `walkDirTree` now returns stats and error channels, and `loadDir` and `isDirEmpty` use the supplied filesystem. `Scan` starts the walker directly and maps its paths back to host paths.

Removed `getRootFolderWalker` and `utils.IsDirReadable`, and updated the walker tests.

Verification: `go test ./scanner` passed; `git diff --check` passed.