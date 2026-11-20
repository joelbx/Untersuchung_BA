Implemented `GetInstance[T](constructor func() T) T` in [singleton.go](/app/utils/singleton/singleton.go). It caches each exact type separately, so `T` and `*T` have independent instances. Concurrent first calls run the constructor once.

Added a test with 20,000 simultaneous callers. `go test` and `go test -race` both pass for `./utils/singleton`.