Refactored directory traversal to use `fs.FS` for loading, directory checks, ignore markers, and readability checks. `Scan` now creates the filesystem adapter and consumes the traversal channels directly; `getRootFolderWalker` and `utils.IsDirReadable` were removed.

Updated the existing walker tests. `go test ./scanner` passed. The build emitted a deprecation warning from TagLib’s C++ wrapper.