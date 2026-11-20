Reverted directory scanning to native OS filesystem calls and added [utils.IsDirReadable](/app/utils/paths.go). Traversal now uses absolute paths while retaining audio detection, directory ignore rules, and error logging.

`go test ./scanner ./utils` and `git diff --check` passed.