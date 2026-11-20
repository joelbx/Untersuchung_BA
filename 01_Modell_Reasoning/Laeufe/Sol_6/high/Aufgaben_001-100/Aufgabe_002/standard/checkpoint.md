Task: Fix Kubernetes proxy address selection for `tctl auth sign --format=kubernetes`.

Plan: inspect ProxyConfig and signing flow; implement HTTPS Kubernetes address selection with port 3026 and invalid-address fallback; run relevant existing tests.

Status: implemented and verified. ProxyConfig.KubeAddr selects the Kubernetes public host (or proxy public host), validates it, and returns HTTPS on port 3026. tctl uses it for a local Kubernetes proxy or for registered proxies, skipping invalid registered addresses. An explicit --proxy remains authoritative.

Verification: `go test ./lib/service -run '^TestProxyConfigKubeAddr$' -count=1` and `go test ./tool/tctl/common -run '^TestAuthSignKubeconfig' -count=1` both pass.
