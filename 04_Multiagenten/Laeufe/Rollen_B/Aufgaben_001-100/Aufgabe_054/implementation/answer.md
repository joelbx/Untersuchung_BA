Added `GetInstance[T]` in [singleton.go](/app/utils/singleton/singleton.go). It returns `T` directly, caches by exact type so `T` and `*T` remain separate, and runs each type’s constructor once under concurrent calls. The existing `Get` behavior is unchanged.

Added tests for reuse, value and pointer separation, and 20,000 simultaneous calls. The package tests and targeted race test passed.