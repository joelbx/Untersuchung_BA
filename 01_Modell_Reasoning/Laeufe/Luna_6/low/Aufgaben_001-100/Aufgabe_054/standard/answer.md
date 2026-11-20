Implemented `GetInstance[T]` in [singleton.go](/app/utils/singleton/singleton.go). It returns the concrete type, caches one instance per type (with `T` and `*T` kept separate), and synchronizes initialization so concurrent calls reuse the same instance. The existing `Get` API remains available.

`go test ./utils/singleton` passed.