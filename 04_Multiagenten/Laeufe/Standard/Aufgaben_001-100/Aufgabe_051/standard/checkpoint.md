# Checkpoint

Task: implement tsh environment configuration precedence for Kubernetes cluster, site, and home.
Status: complete. Added TELEPORT_KUBE_CLUSTER handling after CLI parsing, preserving explicit CLI Kubernetes cluster. Existing TELEPORT_CLUSTER/TELEPORT_SITE precedence and TELEPORT_HOME override/normalization remain intact. Added tests for Kubernetes precedence and home override.
Verification: go test ./tool/tsh -run '^(TestReadClusterFlag|TestReadKubeClusterFlag|TestReadTeleportHome)$' -count=1 passed; git diff --check passed.
