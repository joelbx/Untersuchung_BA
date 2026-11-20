# Checkpoint

- Task: support exact `${VARIABLE_NAME}` substitution in YAML configuration through the existing decode hooks.
- Status: implemented an exact-match environment reference decode hook as the first `DecodeHooks` entry. Added integration tests for multiple references, integer and duration conversion, override precedence, unchanged values, missing variables, and empty variables.
- Red checks: the new integer-port test failed on `${CONFIG_TEST_GRPC_PORT}`; the edge-case test failed on unresolved references with the hook disabled; moving the hook behind the duration hook failed on `cache.ttl`.
- Green check: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./internal/config -count=1` passed.
- Full check: `GOTOOLCHAIN=local GOPROXY=off GOSUMDB=off go test ./...` exited 1. `internal/cache/redis` TestSet, TestGet, and TestDelete failed because Docker daemon is unavailable at `/var/run/docker.sock`; `internal/gitfs` Test_FS_Submodule failed because its remote git request returned Forbidden. Other listed packages, including `internal/config`, passed. Full-suite status remains uncertain until those external dependencies are available.
- Constraints: local sources only, test first, run relevant and full repository tests without downloads.
