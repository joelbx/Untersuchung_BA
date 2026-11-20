# Checkpoint

Implemented `singleton.GetInstance[T]` using a mutex-protected shared cache keyed by the full reflected type name. This returns concrete values, caches one constructor result per `T`, supports independent value and pointer types, and serializes concurrent initialization. The existing `Get` API remains available for current callers.

Verification: `go test ./utils/singleton` passed.
