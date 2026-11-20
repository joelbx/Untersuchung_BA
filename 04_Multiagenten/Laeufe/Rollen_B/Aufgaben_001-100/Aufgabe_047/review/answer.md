VERDICT: FIX

**Code defect:** [hasher.go](/app/utils/hasher/hasher.go:34) creates a random `maphash` seed for every `Hasher`. As a result, setting the same ID and explicit seed in a fresh instance or process does not reliably reproduce the same hash. The added [tests](/app/utils/hasher/hasher_test.go:19) check restoration only within one instance. Use a deterministic hash based on the supplied seed and input, and verify reproduction across instances.

**Tests:** `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./utils/hasher`, `go test -race ./utils/hasher`, and `go test ./db ./persistence` all passed with the same offline environment variables. `git diff --check` passed. TEST_ENVIRONMENT_PROBLEM: none.