# Checkpoint

Task: fix BatchEvaluate handling of disabled flags, preserve ordered per-flag responses and durations, and migrate protobuf empty/timestamp uses to google.golang.org/protobuf.

Status: implementation complete. Added ErrDisabled and batch handling that preserves ordered disabled entries with value "disabled", timestamps, and per-flag durations. Migrated server, storage, and RPC protobuf references to timestamppb/emptypb and modern protobuf interfaces. Preserved gRPC InvalidArgument mapping for single disabled evaluations.

Verification: `GOPROXY=off GOSUMDB=off GOFLAGS=-mod=readonly go test ./...` passed; `git diff --check` passed. The offline test run populated two existing dependency checksums in go.sum.
