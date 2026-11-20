VERDICT: FIX

The affected tests pass, but the patch leaves three code defects:

- [validate.go](/app/internal/cue/validate.go:66) returns raw parse errors. Invalid YAML can therefore bypass the required multi-error unwrapping and file, line, and column format.
- [validate.go](/app/internal/cue/validate.go:155) checks flag rules but misses boolean rollout segment references. `flipt validate` can accept an unknown segment that import or snapshot creation later rejects.
- [snapshot.go](/app/internal/storage/fs/snapshot.go:96) calls the reference-only check, so snapshot creation skips CUE configuration validation.

**Tests:** `go test ./internal/cue ./internal/ext ./internal/storage/fs ./cmd/flipt` exited 0; the first three packages passed, and `cmd/flipt` has no test files. **TEST_ENVIRONMENT_PROBLEM:** none. No project code or tests were changed during this review.