Fixed kubeconfig address selection. `ProxyConfig.KubeAddr()` now returns an HTTPS URL using the Kubernetes public host, or the proxy public host as a fallback, on port 3026. `tctl auth sign --format=kubernetes` uses that address, skips invalid registered proxy addresses, and preserves an explicit `--proxy` value.

The focused service and `tctl` tests pass.