Fixed the reviewed `db.port` defect. Configuration loading now rejects nonnumeric and fractional ports with a field-qualified error instead of silently using the default port. Added regression tests for valid, malformed, and out-of-range values.

Both exact reviewer test commands passed: `go test ./config ./storage/db` and `go test ./cmd/flipt`, with `GOPROXY=off GOSUMDB=off`.