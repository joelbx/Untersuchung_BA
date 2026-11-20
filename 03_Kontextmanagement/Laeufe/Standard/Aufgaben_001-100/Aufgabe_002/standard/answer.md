Fixed kubeconfig address selection for `tctl auth sign --format=kubernetes`. `ProxyConfig.KubeAddr()` now returns an HTTPS URL on port 3026. The command uses it for an enabled local Kubernetes proxy; otherwise, it checks registered proxies, skipping invalid addresses. An explicit `--proxy` value still takes precedence.

The focused service and `tctl` tests passed, as did `git diff --check`.