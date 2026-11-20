# Checkpoint

Completed: Replaced scanner tree traversal with native OS path operations, absolute roots, native directory entries, symlink resolution, ignore handling (including Windows system folders), and OS-based readability checks. Added `utils.IsDirReadable` and updated the scanner call site and traversal tests.

Validation: `go test ./scanner ./utils` passes. `git diff --check` passes. The build emits an existing TagLib deprecation warning for `AudioProperties::length()`.
