Implemented Redis TLS support with custom CA path or inline certificate data, TLS 1.2 minimum, system CA fallback, and optional certificate verification skipping. Added the requested CA exclusivity validation, config fixtures, and the `api/cachetls` integration case and workflow matrix entry.

Verification passed: `go test -short ./internal/config ./internal/cache/redis ./internal/cmd ./build/testing`. The Dagger integration service was compiled but not launched.

Key changes: [Redis client](/app/internal/cache/redis/client.go:14), [cache config](/app/internal/config/cache.go:47), [integration suite](/app/build/testing/integration.go:342).