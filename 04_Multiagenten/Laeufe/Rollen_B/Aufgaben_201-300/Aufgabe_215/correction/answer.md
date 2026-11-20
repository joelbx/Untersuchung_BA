Added the missing TLS certificate and key fixtures at the required paths and updated the configuration test to load the specified advanced HTTPS setup.

`GOPROXY=off GOSUMDB=off go test ./cmd/flipt` and `git diff --check` both passed. No `TEST_ENVIRONMENT_PROBLEM`.