Refactored directory traversal to use `fs.FS`, including `walkDirTree`, `loadDir`, and `isDirEmpty`. `walkDirTree` now returns a results channel and an error channel. I moved walker setup into `Scan` and removed `getRootFolderWalker` and `utils.IsDirReadable`.

A new `fstest.MapFS` regression test passes. `go test ./scanner ./utils -count=1` and `git diff --check` also pass.