BatchEvaluate now keeps disabled flags in the response, preserves input order, and continues evaluating the remaining flags. Disabled entries have `match=false`, an empty value, a timestamp, and their own duration; the outer response retains the total duration. `ErrDisabled` is distinct, while single-flag evaluation still maps it to `InvalidArgument`.

Protobuf message types and empty-result RPCs now use `timestamppb` and `emptypb`. The grpc-gateway v1 adapter retains its legacy `proto.Message` import because its runtime requires that interface.

The full offline test suite and `git diff --check` passed.