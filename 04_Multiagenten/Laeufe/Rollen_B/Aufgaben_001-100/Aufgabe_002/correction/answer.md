Fixed `ProxyConfig.KubeAddr()` to skip invalid public addresses and use the first valid one. Added regression cases for both Kubernetes-specific and generic proxy address lists.

Both reviewer test commands passed, and `git diff --check` passed. No test environment problem remains.