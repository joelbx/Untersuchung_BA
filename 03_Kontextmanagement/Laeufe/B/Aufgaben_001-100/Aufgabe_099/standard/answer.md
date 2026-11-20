Resolved the BatchEvaluate bug. Disabled flags now produce an ordered response entry with `match: false` and `value: "disabled"`; other flags continue evaluating. Each entry has its own timestamp and duration, and the batch has a total duration. Added `ErrDisabled` and migrated the protobuf timestamp and empty-result types.

`GOPROXY=off go test -mod=mod ./...` passed.