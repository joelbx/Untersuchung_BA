# Checkpoint

Task: add tracing sampling ratio and propagator configuration in `/app`.

Assigned process: systematic debugging. Investigating existing config types, defaults, loading, validation, and tests before editing implementation. `rg` is unavailable (`/bin/bash: rg: command not found`), so local searches use `grep`/`find`.

Root cause: `TracingConfig` has no sampling ratio or propagator fields, its Viper defaults omit them, and it does not implement `validator`. `Default()` also omits them. The runtime hardcodes `AlwaysSample()` and tracecontext plus baggage. Existing config sections use `setDefaults` and `validate`, and `Load` calls both around unmarshalling. Hypothesis: adding the two fields and their defaults/validation through this existing path will preserve configured values and reject invalid input. A focused failing config test will verify this before the patch.

The focused config test failed before implementation with undefined fields/types. After adding config fields, defaults, and validation it passes; `GOPROXY=off GOSUMDB=off go test ./internal/config -count=1` passes. Runtime hypothesis: passing the ratio into `NewProvider` and selecting propagators from the validated list removes the remaining fixed behavior. Local module cache contains the OpenTelemetry contrib propagator modules, so runtime support can be implemented offline.

The focused runtime test initially failed with the old provider signature and absent propagator factory. After implementation, its first run exposed a test assumption: B3's `Fields()` reports both header formats. The test now checks actual injection for b3 and b3multi. `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing ./internal/cmd -count=1` passes. The existing schema tests initially failed because both schemas rejected the new fields; after updating them, `GOPROXY=off GOSUMDB=off go test ./config -run 'Test_CUE|Test_JSONSchema' -count=1` passes.

One attempted command, `GOPROXY=off GOSUMDB=off go test -mod=mod ./internal/tracing -run 'TestNewProviderSamplingRatio|TestNewPropagator' -count=1`, failed because workspace mode only permits readonly or vendor `-mod`. Retrying without `-mod=mod` succeeded using local cached modules. No dependency download was used.

Final verification: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/tracing ./internal/cmd ./config -count=1` passed for all four packages. `git diff --check` passed. Added the local cached module checksums to `go.sum`; no harness settings or git history/index were changed.
