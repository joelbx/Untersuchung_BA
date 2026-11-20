Implemented generic `GetInstance[T]` in [singleton.go](/app/utils/singleton/singleton.go). It caches by exact type, runs each type’s constructor once under concurrency, and keeps value and pointer singletons independent.

Added tests in [singleton_test.go](/app/utils/singleton/singleton_test.go), including 20,000 concurrent calls and nil interface results.

Validation passed: `go test ./utils/singleton`, `go test -race ./utils/singleton`, and the packages using legacy `Get`. The `db` tests passed with a compiler warning from sqlite3.