Added [GetInstance[T]](/app/utils/singleton/singleton.go:30), which returns the concrete type and uses a concurrency-safe cache. It creates each type once and keeps `T` and `*T` independent. Added [tests](/app/utils/singleton/singleton_test.go:20) for reuse, type separation, and 20,000 concurrent calls.

`go test ./utils/singleton` and `go test -race ./utils/singleton` both pass.