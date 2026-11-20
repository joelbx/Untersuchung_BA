Fixed `tctl auth sign --format=kubernetes` so generated kubeconfigs use an HTTPS Kubernetes proxy URL on port 3026, unless `--proxy` is explicitly set. Added `ProxyConfig.KubeAddr()` and a registered-proxy fallback that skips invalid public addresses.

Regression tests cover address selection and the generated kubeconfig. `go test ./lib/service ./tool/tctl/common -count=1` passed.