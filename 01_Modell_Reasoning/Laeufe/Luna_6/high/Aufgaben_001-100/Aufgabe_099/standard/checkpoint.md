# Checkpoint

Task: Fix BatchEvaluate handling of disabled feature flags in `/app`.

Implemented:
- Added the `ErrDisabled` string error type and `ErrDisabledf` constructor.
- `evaluate` returns `ErrDisabled`; batch evaluation uses `errors.As`, continues on disabled flags, emits `Value: "DISABLED"`, and preserves request order.
- Batch entries have their own duration and timestamp; the outer response duration measures the full batch call.
- Switched generated RPC timestamps and empty messages plus server/database timestamp handling to `timestamppb` and `emptypb`.

Verification: `gofmt` and `git diff --check` passed; `go test ./errors` passed. `go test ./server ./storage/db/... ./errors ./rpc` could not set up because go.sum lacks entries for required gRPC/lib/pq modules. No dependency downloads were attempted.
