# Singleton task checkpoint

Implemented generic `GetInstance` in `utils/singleton` with a cache keyed by exact `reflect.Type` and per-type `sync.Once`. Added tests for reuse, independent value and pointer instances, and 20,000 concurrent calls. Existing `Get` behavior remains intact.

Verification: `GOPROXY=off go test ./utils/singleton` and `GOPROXY=off go test -race ./utils/singleton` passed; `git diff --check` passed.
