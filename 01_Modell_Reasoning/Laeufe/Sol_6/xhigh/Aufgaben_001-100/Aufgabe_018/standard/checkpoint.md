# Config string slice decoding

- Task: restore whitespace splitting for scalar strings decoded into `[]string` in `internal/config/config.go`, including YAML and ENV values.
- Status: implementation complete. Scalar strings decode to `[]string` using Unicode whitespace and commas; empty strings produce an empty slice. Existing sequences and non-string values bypass the hook. The advanced fixture and focused load tests cover YAML and ENV paths.
- Verification: `GOPROXY=off GOSUMDB=off go test ./internal/config` passed; `git diff --check` passed.
