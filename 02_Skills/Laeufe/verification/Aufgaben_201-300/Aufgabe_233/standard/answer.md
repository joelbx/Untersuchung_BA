Refactored `walkDirTree`, `loadDir`, and `isDirEmpty` to use `fs.FS`. `Scan` now starts the walk directly, and `utils.IsDirReadable` was removed. Added a test that walks an in-memory filesystem.

Verification: `go test -count=1 ./scanner ./utils` passed, and `git diff --check` found no whitespace errors.