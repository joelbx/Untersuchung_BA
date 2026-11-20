Refactored the directory walker to use `fs.FS` for traversal and directory checks. `Scan` now creates the filesystem and consumes the walker’s results and error channels directly. I removed `getRootFolderWalker` and `utils.IsDirReadable`, and added an in-memory filesystem test for child-first traversal and output paths.

The scanner and utils tests pass offline, and `git diff --check` is clean.