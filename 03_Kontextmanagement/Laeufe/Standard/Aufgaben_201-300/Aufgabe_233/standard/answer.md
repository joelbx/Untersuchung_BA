Refactored directory traversal to use `fs.FS`, including directory loading, symlink checks, ignore markers, and readability checks. `Scan` now starts the walker directly, and the unused `utils.IsDirReadable` helper is removed. Added virtual filesystem tests.

`go test ./scanner ./utils` and `git diff --check` passed.