# Checkpoint

Implemented the disabled flag batch behavior and protobuf API updates in `/app`.

- Added `errors.ErrDisabled` and `ErrDisabledf`.
- `evaluate` now returns `ErrDisabled` for disabled flags.
- `batchEvaluate` detects wrapped disabled errors with `errors.As`, appends a `DISABLED` result in request order, and continues; each entry receives its own timestamp and duration. `BatchEvaluate` continues to populate total duration.
- Switched generated message and gRPC empty/timestamp types, plus server RPC empty return types, to `google.golang.org/protobuf`.

Verification attempted: `go test ./server ./rpc ./errors` could not compile because required `google.golang.org/grpc` module checksums are absent from `go.sum`. No dependency downloads or go.sum edits were performed.
