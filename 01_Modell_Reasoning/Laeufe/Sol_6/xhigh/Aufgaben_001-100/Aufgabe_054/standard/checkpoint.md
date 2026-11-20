Task: Add generic singleton.GetInstance[T](constructor func() T).
Status: Implemented GetInstance with a reflect.Type keyed sync.Map and per-type sync.Once. Added tests for value/pointer independence, reuse, and 20,000 concurrent callers.
Verification: `GOPROXY=off GOSUMDB=off go test ./utils/singleton` and `GOPROXY=off GOSUMDB=off go test -race ./utils/singleton` both pass; `git diff --check` passes.
