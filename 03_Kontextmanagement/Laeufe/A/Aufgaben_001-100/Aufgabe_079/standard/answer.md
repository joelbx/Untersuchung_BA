Restored native OS filesystem operations for directory traversal and audio file discovery. The walker now uses absolute paths and calls the new [IsDirReadable](/app/utils/paths.go) helper. Directory ignore behavior, audio detection, and traversal error logging are preserved.

Verification: `go test ./scanner ./utils` and `git diff --check` passed.