Anonymous telemetry now reports `flipt.audit.sinks` with `"log"`, `"webhook"`, or both when those audit sinks are enabled. It omits `audit` when neither is enabled and uses telemetry version `1.3`.

The new sink cases failed before the change and passed afterward. `go test ./internal/config ./internal/telemetry -count=1` and `git diff --check` passed.