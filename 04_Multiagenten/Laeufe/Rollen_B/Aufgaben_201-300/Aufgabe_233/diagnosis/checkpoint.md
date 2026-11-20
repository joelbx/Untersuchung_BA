# Fault localization result

- `scanner/walk_dir_tree.go`: `walkDirTree` accepts a caller-owned channel and returns an error; `walkFolder`/`loadDir` use paths without an `fs.FS` parameter. `loadDir` directly calls `os.Stat`/`os.Open`; symlink and ignore checks directly call `os.Stat`; readability calls `utils.IsDirReadable` (another `os.Open`). `fullReadDir` already accepts `fs.ReadDirFile` but types its entries as `os.DirEntry`.
- `scanner/tag_scanner.go`: `Scan` calls `isDirEmpty(ctx, s.rootFolder)` and `getRootFolderWalker`; the latter owns channel construction, goroutine and logging. `isDirEmpty` calls `loadDir`.
- `utils/paths.go`: sole `IsDirReadable` definition; the walker is its only Go caller.
- Preserve relative slash paths required by `fs.FS` while keeping scanner paths compatible with current DB and media processing. OS fixture tests expect a symlink to a directory to be visited; virtual FS symlink behavior is uncertain and needs explicit coverage. Preserve child-first ordering, sorted entries, ignore marker behavior, and error/close semantics.
- Existing `fullReadDir` tests use `fstest.MapFS` with injected read errors. Focused baseline command `GOPROXY=off GOTOOLCHAIN=local go test -mod=readonly ./scanner -run '^TestScanner$' -ginkgo.focus='walk_dir_tree' -count=1` passed.

No project source or tests changed.
