# Checkpoint

Task: Correct Kubernetes proxy address selection for `tctl auth sign --format=kubernetes` and add `ProxyConfig.KubeAddr()`.

Status: Implemented. `KubeAddr()` requires Kubernetes proxy support and builds an HTTPS URL on port 3026 from the first Kubernetes public address, or the first general public address. The auth command uses that method for a local Kubernetes proxy; otherwise it searches registered proxies, skipping malformed public addresses. An explicit `--proxy` takes precedence.

Validation: `GOPROXY=off GOSUMDB=off go test ./tool/tctl/common ./lib/service -run 'TestAuthSign|TestProxyConfigKubeAddr' -count=1` passed. `git diff --check` passed. The compiler emitted a preexisting vendored SQLite C warning during tests. `rg` was unavailable (`/bin/bash: rg: command not found`), so inspection used grep/find.
