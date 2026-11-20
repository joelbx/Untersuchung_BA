# Checkpoint

Task: Resolve BatchEvaluate behavior for disabled flags in `/app`.

Completed:
- Added the `ErrDisabled` string error and `ErrDisabledf` constructor; disabled evaluations return this typed error and a `value` of `disabled`.
- Batch evaluation uses `errors.As` to tolerate disabled flags, keeps their responses in input order, and assigns each response its own timestamp and duration. The public batch method records total duration.
- Migrated protobuf timestamp and empty message types and RPC signatures to `timestamppb` and `emptypb`; moved the legacy grpc-gateway v1 compatibility interface to protobuf's `protoiface.MessageV1`.
- Marked `github.com/golang/protobuf` as indirect because grpc-gateway v1 still depends on it.

Verification:
- `GOPROXY=off go test -mod=mod -modfile=/tmp/flipt-codex-test.mod ./...` passed. A temporary modfile was used because the repository's go.sum lacks entries required by the cached dependencies; repository dependency sums were left unchanged.
- `git diff --check` passed.

Constraints followed: local code and existing tests only; no downloads, history/index baseline changes, or harness changes.
