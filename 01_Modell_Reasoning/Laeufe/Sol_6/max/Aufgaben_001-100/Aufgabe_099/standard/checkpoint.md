# Checkpoint

Task: make BatchEvaluate preserve one ordered result per requested flag, including disabled flags, while migrating protobuf empty and timestamp types.

Initial state: repository at `/app`; working tree status showed no tracked edits. `rg` is unavailable, so local inspection will use `find` and `grep`.

Next: inspect evaluator, error types, generated RPC code, and existing tests; edit implementation and run relevant existing Go tests.

Progress: added typed `ErrDisabled`, ordered batch results with per-flag duration and an explicit `disabled` field, and migrated timestamp/empty types in server, storage, and protobuf/gRPC generated code. Updated the generated protobuf descriptor locally to include the field. Added regression tests for mixed enabled/disabled batches, error propagation, serialization, and disabled error mapping. Formatting is complete; relevant tests are next.

Final: all repository Go tests passed with `GOPROXY=off GOSUMDB=off go test -mod=mod ./...`; the focused server suite passed again after increasing the timing test delay. `git diff --check` passed. The old protobuf imports are gone from repository Go source. `go.sum` gained two hashes for existing declared dependencies during the offline test run.
