Reverted the scanner to native OS directory operations and absolute paths. Added [IsDirReadable](/app/utils/paths.go) for directory open checks, while preserving audio detection, ignored-directory handling, and traversal error logging.

Updated the scanner tests, including absolute-path and missing-root coverage. `go test ./scanner ./utils` and `git diff --check` pass.