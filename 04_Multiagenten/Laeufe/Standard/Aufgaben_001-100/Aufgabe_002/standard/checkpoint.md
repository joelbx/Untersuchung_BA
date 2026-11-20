Task: Fix Kubernetes proxy address selection for `tctl auth sign --format=kubernetes`.
Status: Implemented `ProxyConfig.KubeAddr()` with HTTPS and port 3026, updated tctl signing to select a Kubernetes proxy address and skip invalid registered addresses, and added regression tests. `go test -vet=off ./lib/service ./tool/tctl/common -count=1` passes. `git diff --check` passes.
