Updated the [audit structures and constructors](/app/internal/server/audit/types.go) so rules and rollouts record single segment keys, comma-separated keys for multiple segments, and optional operator names. Added [tests](/app/internal/server/audit/types_test.go) for those cases and JSON omission.

`GOPROXY=off GOSUMDB=off go test ./internal/server/audit/...` passed.