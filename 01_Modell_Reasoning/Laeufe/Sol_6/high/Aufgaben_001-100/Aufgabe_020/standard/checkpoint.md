# Redis TLS cache issue

Implemented Redis CA path/inline/insecure TLS settings, validation, a TLS 1.2 Redis client constructor, application wiring, YAML fixtures, schema entries, and `api/cachetls` integration setup.

Verified with `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cache/redis ./internal/cmd ./config -short`, `go test ./build/testing -run '^$'`, and `git diff --check`. All passed. The Dagger integration suite was compiled but not executed locally.
