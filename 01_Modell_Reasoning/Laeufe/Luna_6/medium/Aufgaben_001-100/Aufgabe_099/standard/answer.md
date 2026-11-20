Implemented disabled flag handling for batch evaluation. Disabled flags now return `ErrDisabled`; batch evaluation recognizes that error, adds a `DISABLED` result with its own timestamp and duration, and continues in input order. The outer response still records total duration.

Updated generated protobuf and gRPC types, plus server RPC empty results, to use `google.golang.org/protobuf`. The required checkpoint is in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

`git diff --check` passed. The existing tests could not run because the checkout lacks `go.sum` entries for `google.golang.org/grpc`; I did not download dependencies or modify `go.sum`.