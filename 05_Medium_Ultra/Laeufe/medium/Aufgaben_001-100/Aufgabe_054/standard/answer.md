Added `singleton.GetInstance[T](constructor func() T) T` in [singleton.go](/app/utils/singleton/singleton.go). It caches `T` and `*T` separately and runs each type’s constructor once, even under concurrent calls.

Added tests for reuse, type separation, and 20,000 simultaneous calls in [singleton_test.go](/app/utils/singleton/singleton_test.go). The singleton package passes `go test -race`.