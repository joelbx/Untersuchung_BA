Refactored [walkDirTree](/app/scanner/walk_dir_tree.go) and its helpers to use `fs.FS` and return result and error channels. [Scan](/app/scanner/tag_scanner.go) now sets up the filesystem and walker directly. Removed `utils.IsDirReadable` and added virtual filesystem test coverage.

Verification passed: `go test ./scanner ./utils` and `git diff --check`.