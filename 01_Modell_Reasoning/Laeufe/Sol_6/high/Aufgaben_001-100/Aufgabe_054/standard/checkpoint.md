Task: Implement generic singleton.GetInstance[T](constructor func() T) in /app.
Status: Implemented GetInstance with exact-type caching and sync.Once. Added tests for reuse, value/pointer separation, and 20,000 concurrent callers.
Verification: `go test ./utils/singleton`, `go test -race ./utils/singleton`, and `git diff --check` passed. The race test was rerun after the final assertion change.
