Task: Fix BatchEvaluate disabled flags and migrate timestamp/empty protobuf types.
Status: Complete.
Implemented: ErrDisabled/ErrDisabledf; batch continues for disabled entries in order with per-entry timestamp, unmatched/empty value, and individual duration; outer duration retained. Other errors still abort. Server and generated RPC timestamp/empty types use timestamppb/emptypb; storage timestamp conversion migrated; disabled single-evaluation errors retain InvalidArgument status.
Verification: GOPROXY=off GOSUMDB=off go test -mod=mod ./... passed; git diff --check passed.
Compatibility: grpc-gateway v1 generated gateway retains its legacy proto.Message import for forwarding API compatibility.
