Replaced the scanner’s `fs.FS` reads with OS filesystem operations and absolute paths. Directory traversal, audio discovery, ignore rules, and error logging remain in place. Added [IsDirReadable](/app/utils/paths.go) and buffered traversal errors so recursive failures reach the caller without blocking.

`go test ./scanner ./utils` and `git diff --check` passed. No delegation was used.