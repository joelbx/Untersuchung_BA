Implemented generic `GetInstance[T]` in [singleton.go](/app/utils/singleton/singleton.go). It returns `T` directly, constructs each type once under concurrency, and keeps `T` and `*T` in separate cache entries.

Added tests covering reuse and 20,000 concurrent calls. The singleton tests and race detector both pass.