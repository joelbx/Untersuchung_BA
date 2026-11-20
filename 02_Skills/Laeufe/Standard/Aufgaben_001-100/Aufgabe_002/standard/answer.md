Fixed `tctl auth sign --format=kubernetes` so generated kubeconfigs use an HTTPS Kubernetes proxy address on port 3026. Added `ProxyConfig.KubeAddr()`, kept an explicit `--proxy` override, and made registered-proxy lookup skip malformed public addresses.

The focused auth and service tests passed, including the existing kubeconfig test. `git diff --check` passed.