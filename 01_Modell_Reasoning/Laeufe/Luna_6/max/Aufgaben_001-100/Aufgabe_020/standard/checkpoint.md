# Checkpoint

Task: Add TLS trust configuration to the Redis cache backend and register the TLS cache integration suite.

Completed:
- Added `ca_cert_path`, `ca_cert_bytes`, and `insecure_skip_tls` to Redis cache config and both schemas; the skip flag defaults to false.
- Added the required CA input exclusivity validation message.
- Added `internal/cache/redis.NewClient` with TLS 1.2 minimum, custom CA file/bytes support, insecure verification control, and nil custom roots when system roots should be used.
- Routed gRPC Redis cache setup through the new constructor.
- Added the four requested YAML fixtures and config loading expectations.
- Added the TLS Redis integration suite and registered `api/cachetls` in the integration registry and GitHub Actions matrix.

Verification: `go test -short ./internal/config ./internal/cache/redis ./internal/cmd ./build/testing` passed. The Dagger integration service was compiled but not executed.
