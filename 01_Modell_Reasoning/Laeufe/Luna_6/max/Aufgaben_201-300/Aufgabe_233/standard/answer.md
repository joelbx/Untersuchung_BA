Refactored directory traversal to use `fs.FS`, with `walkDirTree` returning results and error channels. `Scan` now mounts the media root with `os.DirFS` and calls the walker directly; `getRootFolderWalker` and `utils.IsDirReadable` were removed.

Added an in-memory filesystem traversal test. **Verification:** `go test ./scanner` passed, and `git diff --check` was clean. The build emitted a TagLib deprecation warning. Updated `.codex-role-output/checkpoint.md`.

Changed: [walk_dir_tree.go](/app/scanner/walk_dir_tree.go:29), [tag_scanner.go](/app/scanner/tag_scanner.go:83), and [walk_dir_tree_test.go](/app/scanner/walk_dir_tree_test.go:43).