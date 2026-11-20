Task: Add TELEPORT_KUBE_CLUSTER handling in tsh CLI config.
Implemented: tsh reads TELEPORT_KUBE_CLUSTER into KubernetesCluster after CLI parsing when no CLI kube cluster was specified. Added tests for empty, environment, CLI, and precedence cases. Existing TELEPORT_CLUSTER/TELEPORT_SITE precedence and TELEPORT_HOME override/normalization were checked, with additional home tests.
Verification: gofmt; git diff --check; GOTOOLCHAIN=local GOPROXY=off go test ./tool/tsh -run 'TestRead(ClusterFlag|KubeClusterFlag|TeleportHome)$' -count=1 (passed).
