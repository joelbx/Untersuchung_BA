Added `flipt.is_auth_method(input, name)` to both authorization backends. It accepts the seven requested identifiers, maps `k8s` and `kubernetes` to the same protocol buffer code, returns a boolean for matches, and reports the specified errors.

All authorization engine tests passed with `GOPROXY=off go test ./internal/server/authz/engine/...`.