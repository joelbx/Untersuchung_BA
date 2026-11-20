The `walkDirTree` refactor is complete. Traversal, directory loading, and emptiness checks now use `fs.FS`; `Scan` starts the walker directly. I removed `getRootFolderWalker` and `utils.IsDirReadable` and added a virtual filesystem test.

`go test -count=1 ./scanner`, `go test ./scanner ./utils`, and `git diff --check` passed.