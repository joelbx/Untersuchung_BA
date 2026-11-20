# Checkpoint

Task: implement generic singleton.GetInstance with per-type, concurrency-safe caching.
Status: complete.
Changes: exact reflect.Type key, sync.Map and sync.Once; tests for value/pointer separation, constructor reuse, and 20,000 concurrent callers.
Verification: GOPROXY=off go test ./utils/singleton; GOPROXY=off go test -race ./utils/singleton; git diff --check all passed.
Delegation: none.
