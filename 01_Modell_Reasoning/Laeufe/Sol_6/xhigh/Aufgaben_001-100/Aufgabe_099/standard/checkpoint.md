Task: Resolve BatchEvaluate failures for disabled flags and migrate protobuf timestamp/empty use.
Status: Complete. Disabled flags now retain ordered non-matching entries with empty variant values, timestamps, and per-flag durations; only other errors abort. ErrDisabled is mapped to InvalidArgument for unary Evaluate. Protobuf and gRPC use timestamppb/emptypb; the pinned gateway runtime is bridged through an interface that includes modern proto.Message.
Verification: GOPROXY=off go test -mod=mod ./... passed; git diff --check passed.
Constraints: Edit checked-out files; preserve git history/index/harness; use local code and tests only.
