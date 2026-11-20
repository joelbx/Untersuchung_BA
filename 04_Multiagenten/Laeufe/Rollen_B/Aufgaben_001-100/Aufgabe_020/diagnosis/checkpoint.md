Progress: Fault localized without modifying project source or tests.
- `RedisCacheConfig` in internal/config/cache.go has `require_tls` but no CA or insecure fields. `CacheConfig.setDefaults` has no insecure default; `config.Default` sets RequireTLS false.
- `getCache` in internal/cmd/grpc.go creates go-redis client directly with TLS MinVersion 1.2 and no RootCAs/InsecureSkipVerify. A new `redis.NewClient(config.RedisCacheConfig) (*goredis.Client,error)` would centralize certificate loading and client options; getCache should propagate its error before Ping.
- `config.Load` registers validators for top-level fields only. Mutual-exclusion validation for nested Redis fields must be reached via `CacheConfig.validate`, with exact required error string. Git config has analogous fields/validation but different error wording.
- Existing config tests cover redis.yml only; existing Redis cache tests use plaintext container. Integration registry in build/testing/integration.go includes api/cache but no api/cachetls; workflow matrix likewise lacks api/cachetls.
- Existing config test run started; result pending.
- Verification: `go test ./internal/config -run '^TestLoad$' -count=1` passed against existing tests. No source or test edits made.
