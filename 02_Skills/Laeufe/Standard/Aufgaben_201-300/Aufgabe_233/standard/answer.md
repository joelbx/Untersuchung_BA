Refactored directory traversal to use `fs.FS` throughout, moved walker startup into `Scan`, and removed `utils.IsDirReadable`. Added virtual filesystem and error channel tests.

`GOPROXY=off GOSUMDB=off go test ./scanner ./utils` and `git diff --check` passed.