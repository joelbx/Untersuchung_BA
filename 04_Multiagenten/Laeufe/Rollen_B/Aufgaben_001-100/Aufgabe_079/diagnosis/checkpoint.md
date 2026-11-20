# Fault localization progress

Located the scanner's fs.FS path through `TagScanner.Scan` (`os.DirFS`, `isDirEmpty`, and `walkDirTree`) into `walkFolder`/`loadDir`/directory helpers in `scanner/walk_dir_tree.go`. No project source or tests changed.

Likely fix: pass the absolute media path directly; use OS `Stat`/`Open`/directory reads and OS symlink target lookup; check `.ndignore` via OS stat; add `utils.IsDirReadable(path) (bool, error)` implemented with `os.Open` and immediate close, logging close failures. Retain sorted directory entries, error-loop handling, postorder stats emission, audio/playlist/image counts, skipped unreadable or ignored directories, and error channel/log behavior.

Existing tests in `scanner/walk_dir_tree_test.go` use `os.DirFS` and a fake `fs.ReadDirFile`, so signature changes require corresponding test updates by the implementing role. The Windows-only test expects `$Recycle.Bin` ignored and has signatures inconsistent with current implementation. Test fixtures referenced at `scanner/tests/fixtures` are absent in this checkout. No tests run in this fault-localization pass.
