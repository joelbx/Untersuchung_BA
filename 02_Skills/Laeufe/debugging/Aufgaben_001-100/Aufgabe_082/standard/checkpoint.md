# Checkpoint

Root cause: `initExternalLog` returned a `MultiLog` for multiple audit event URIs, but `MultiLog` lacked the `Emitter` interface required by auth initialization. The `stdout://` backend also constructed `WriterLog`, which lacked typed event emission.

Reproduction: `GOPROXY=off GOFLAGS=-mod=vendor go test ./lib/events -run '^TestMultiLogEmitterRegression$' -count=1` failed before the fix at the `Emitter` assertion.

Changes: Added `WriterEmitter` with JSON line emission and aggregated close errors; validated and embedded `MultiEmitter` in `MultiLog`; switched stdout initialization to `NewWriterEmitter`; added unit and service regression coverage. No git history, index baseline, or harness configuration changed.

Verification: `GOPROXY=off GOFLAGS=-mod=vendor go test ./lib/events -count=1` passed. `GOPROXY=off GOFLAGS=-mod=vendor go test -v ./lib/service -run '^TestConfig$' -check.f 'TestInitExternalLog' -check.v -count=1` passed, showing one check.v test executed. `git diff --check` passed. The service build emitted an existing sqlite3 C compiler warning; it did not fail.
