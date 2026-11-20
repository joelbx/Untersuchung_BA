Restored directory scanning to native OS filesystem operations with absolute paths. Added [utils/paths.go](/app/utils/paths.go) with `IsDirReadable`, and updated the tag scanner and traversal tests.

`go test ./scanner ./utils` passes, and `git diff --check` is clean. The build emitted an existing TagLib deprecation warning.