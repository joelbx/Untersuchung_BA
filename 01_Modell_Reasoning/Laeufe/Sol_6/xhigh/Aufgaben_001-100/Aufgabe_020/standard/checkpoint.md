# Redis cache TLS checkpoint

- Added `ca_cert_path`, `ca_cert_bytes`, and `insecure_skip_tls` to Redis cache configuration, with exclusive CA validation and schema support.
- Added `redis.NewClient` to configure TLS 1.2, custom CA trust, system trust fallback, and optional certificate verification bypass; wired it into cache startup.
- Added YAML fixtures/config tests and Redis client tests for CA bytes/path, default trust, insecure TLS, and invalid inputs.
- Registered `api/cachetls` in the integration runner and GitHub Actions matrix. The case starts TLS-only Redis with an ephemeral certificate trusted by Flipt.
- Verified: `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cache/redis ./internal/cmd -short` passed; `GOPROXY=off GOSUMDB=off go test ./build/testing -run '^$'` passed; `git diff --check` passed.
- Container integration suite not executed locally because Docker and Dagger are unavailable.
