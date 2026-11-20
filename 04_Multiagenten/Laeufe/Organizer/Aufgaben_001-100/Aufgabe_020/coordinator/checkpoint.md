Task: Add Redis cache TLS trust configuration and integration matrix entry.
Status: implemented; local verification complete.
Changes: RedisCacheConfig fields/validation/default, NewClient TLS construction, grpc wiring, CUE/JSON schema, YAML fixtures, client tests, api/cachetls Dagger integration case and workflow matrix.
Verification: GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cache/redis -short -count=1 passed; targeted tests/build for internal/cmd and build/testing passed; git diff --check passed. Dagger integration case compiled but was not executed locally.
Delegation: none.
