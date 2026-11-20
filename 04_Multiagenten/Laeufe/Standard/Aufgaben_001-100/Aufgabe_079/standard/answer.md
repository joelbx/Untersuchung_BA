Reverted directory scanning to native OS paths and filesystem calls, while preserving audio detection, ignore rules, symlink handling, and traversal error reporting. Added [IsDirReadable](/app/utils/paths.go) and updated the scanner tests.

`GOPROXY=off go test ./scanner ./utils` and `git diff --check` passed.