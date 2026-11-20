Task: Fix Kubernetes proxy address selection in tctl auth sign kubeconfig generation.
Status: complete.
Changes: Added ProxyConfig.KubeAddr using HTTPS and default Kubernetes port 3026; tctl prefers local Kubernetes proxy address and scans registered proxies when needed, skipping invalid addresses; explicit --proxy remains authoritative. Added focused tests.
Verification: go test ./lib/service ./tool/tctl/common passed; git diff --check passed.
Delegation: none.
