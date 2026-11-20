# Checkpoint

Task: fix BatchEvaluate disabled flags, per-entry timing, and protobuf migration.
Status: implemented and verified.

- Added ErrDisabled/ErrDisabledf; evaluate returns it for disabled flags.
- BatchEvaluate uses errors.As, keeps ordered disabled entries, and measures each entry independently. Regression tests observed failing before the corresponding implementation and now pass.
- Migrated generated protobuf and gRPC types, server empty RPC signatures, and storage timestamps to timestamppb/emptypb.
- Full suite passed: `GOPROXY=off go test -mod=mod ./... -count=1`.
- `git diff --check` passed.
- Initial `GOPROXY=off go test ./server -run '^TestBatchEvaluate_DisabledFlagKeepsOrderedResults$' -count=1` failed during setup because go.sum lacked cached google.golang.org/grpc package checksums. Retried offline with `-mod=mod`; go.sum gained the required cached grpc and lib/pq checksums.
- Gateway v1 generated code (`rpc/flipt.pb.gw.go`) still imports the legacy proto interface required by its runtime v1 API. Migrating that file requires a gateway runtime upgrade, unavailable under the no-download constraint; generated protobuf messages and gRPC signatures use the modern packages.
