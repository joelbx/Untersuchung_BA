# Checkpoint

Task: implement generic singleton.GetInstance with type-specific, concurrency-safe caching.
Status: complete.
Implementation: `GetInstance[T any](func() T) T` caches by exact reflect.Type, with one sync.Once per type. Existing `Get` remains compatible.
Verification:
- `GOPROXY=off go test ./utils/singleton` — passed.
- `GOPROXY=off go test -race ./utils/singleton` — passed.
- `git diff --check` — passed.
- New test starts 20,000 callers simultaneously and checks one constructor call and identical returned pointers.
Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
