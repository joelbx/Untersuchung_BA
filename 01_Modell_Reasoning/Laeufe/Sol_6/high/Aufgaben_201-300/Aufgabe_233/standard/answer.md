Refactored `walkDirTree`, `loadDir`, and `isDirEmpty` to use `fs.FS`. `walkDirTree` now returns result and error channels. I moved the walker setup into `Scan` and removed `utils.IsDirReadable`.

Verification passed: `go test ./scanner ./utils` and `git diff --check`.