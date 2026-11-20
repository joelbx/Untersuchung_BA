Restored directory scanning to native OS operations with absolute paths, while preserving audio detection, ignore rules, symlink handling, and directory read error logging. Added `utils.IsDirReadable` and restored the Windows `$Recycle.Bin` skip.

Updated scanner call sites and tests. See [walk_dir_tree.go](/app/scanner/walk_dir_tree.go:30), [tag_scanner.go](/app/scanner/tag_scanner.go:79), and [paths.go](/app/utils/paths.go:10).

`go test ./scanner ./utils` passes. The build emitted a TagLib C++ deprecation warning.