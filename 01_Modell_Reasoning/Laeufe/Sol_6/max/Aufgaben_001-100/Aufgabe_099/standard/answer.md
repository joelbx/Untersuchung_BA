Fixed `BatchEvaluate` so disabled flags produce ordered response entries with `disabled=true`, timestamps, and their own durations. Other errors still stop the batch. Added `ErrDisabled` and migrated the repository’s protobuf timestamp and empty result types.

The full Go test suite passes: `GOPROXY=off GOSUMDB=off go test -mod=mod ./...`.