Fixed `BatchEvaluate` so disabled flags produce ordered response entries instead of aborting the batch. Each entry includes its own timestamp and duration, and an explicit `disabled` field identifies disabled flags. The outer response retains the total duration.

Added `ErrDisabled` and `ErrDisabledf`, migrated protobuf timestamps and empty RPC responses to `google.golang.org/protobuf`, and added regression coverage. I delegated the evaluator, protobuf, and test changes, then integrated and reviewed them.

**Verification:** `GOPROXY=off GOSUMDB=off go test ./... -count=1` passed.