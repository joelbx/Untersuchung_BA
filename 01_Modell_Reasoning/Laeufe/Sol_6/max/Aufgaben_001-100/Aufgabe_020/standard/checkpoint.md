# Redis cache TLS support

Implemented the Redis CA path, inline CA, and insecure TLS config fields with conflict validation and schema updates. Added `redis.NewClient` with TLS 1.2, connected it to gRPC cache setup, added YAML fixtures and TLS trust tests, and registered `api/cachetls` in the integration runner and GitHub Actions matrix.

Verification: `GOPROXY=off GOSUMDB=off go test -short ./internal/config ./internal/cache/redis ./config ./internal/cmd` passed; `GOPROXY=off GOSUMDB=off go test -short ./build/testing -run '^$'` passed; `git diff --check` passed. The Dagger integration case was not executed locally because it requires container images.
