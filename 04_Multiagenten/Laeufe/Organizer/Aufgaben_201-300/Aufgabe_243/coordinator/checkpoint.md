# Checkpoint

Task: resolve Kubernetes cluster session connection path consistency.
Status: implemented and verified.
Changes: validate kubeCluster; prioritize local credentials; use reverse tunnel for remote sessions; discover kube_service endpoints; dial selected endpoint and record kubeAddress.
Tests: GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -count=1 (passed); git diff --check (passed).
Delegation: none.
