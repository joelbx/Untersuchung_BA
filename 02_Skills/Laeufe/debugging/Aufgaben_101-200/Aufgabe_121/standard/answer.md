Implemented `flipt.is_auth_method(input, "token")` for both authorization engines. It supports all seven requested labels, maps `k8s` and `kubernetes` to the same protobuf method, and returns the specified errors for missing authentication and unsupported labels.

Verified with `GOPROXY=off GOSUMDB=off go test ./internal/server/authz/... -count=1`; all tests passed.