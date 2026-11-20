Restored directory scanning to native OS filesystem operations with absolute paths, symlink traversal, audio and image detection, ignored-directory handling, and recursive error logging. Added `utils.IsDirReadable` and updated the scanner call site and traversal tests.

`go test ./scanner ./utils` and `git diff --check` pass. The build shows an existing TagLib deprecation warning.