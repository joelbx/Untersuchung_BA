Task: fix tctl auth sign Kubernetes kubeconfig server address selection.
Status: implemented and verified.
Changes: ProxyConfig.KubeAddr returns an HTTPS URL on the default Kubernetes proxy port, preferring Kube.PublicAddrs and validating the advertised host. tctl uses this for an enabled local Kubernetes proxy; otherwise it searches registered proxies, skips invalid addresses, and preserves explicit --proxy.
Tests: GOPROXY=off go test ./lib/service ./tool/tctl/common -run 'TestProxyConfigKubeAddr|TestAuthSignKubeconfig' -count=1 (passed). git diff --check (passed).
