Added generic `GetInstance[T]` in [singleton.go](/app/utils/singleton/singleton.go). It caches each exact type separately and runs its constructor once, including under concurrent calls.

Added tests for value and pointer types, reuse, and 20,000 concurrent calls. The singleton package passes with the race detector.