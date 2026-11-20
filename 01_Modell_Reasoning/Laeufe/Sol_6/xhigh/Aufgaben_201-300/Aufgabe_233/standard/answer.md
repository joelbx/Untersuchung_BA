Refactored the directory walker to use `fs.FS` throughout and return result and error channels. `Scan` now starts the walker directly, and `utils.IsDirReadable` has been removed. Added virtual filesystem and error-channel coverage in [walk_dir_tree_test.go](/app/scanner/walk_dir_tree_test.go).

Verification passed: `go test ./scanner ./utils -count=1` and `git diff --check`.