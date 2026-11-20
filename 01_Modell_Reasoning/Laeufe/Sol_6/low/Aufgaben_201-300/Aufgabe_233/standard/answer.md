Refactored `walkDirTree`, `loadDir`, and `isDirEmpty` to use `fs.FS`. `Scan` now starts the walker directly, and the unused `utils.IsDirReadable` method is removed. Added a virtual filesystem traversal test.

`go test ./scanner ./utils` passed.