# Redis TLS cache work

Implemented Redis CA path, inline PEM, insecure verification toggle, TLS 1.2 minimum, config validation, YAML fixtures/tests, schema keys, and the public `redis.NewClient` constructor. The gRPC Redis startup uses `NewClient`. Added a TLS Redis integration case under `api/cachetls` and its GitHub Actions matrix entry.

Validation:
- `GOPROXY=off GOSUMDB=off go test ./internal/config ./internal/cache/redis ./internal/cmd -short -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./build/testing -run '^$' -count=1` passed (compile check; no test files).
- `git diff --check` passed.
- Full Dagger `api/cachetls` integration execution was not run locally; the case compiles but its TLS Redis service behavior remains to be confirmed in CI.

Tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used grep/find. An initial full short test run failed because `TestStructTags` rejected the new JSON tag; updated that tag and reran successfully.
