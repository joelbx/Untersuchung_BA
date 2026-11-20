Refactored directory scanning to use `fs.FS`. `Scan` now creates the filesystem and starts `walkDirTree` directly; `loadDir` and `isDirEmpty` accept the filesystem, and `getRootFolderWalker` and `utils.IsDirReadable` were removed. Updated the existing walker tests for the new API.

Verification: `go test ./scanner ./utils` passed. The C++ build emitted a TagLib deprecation warning.