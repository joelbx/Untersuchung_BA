Task: Add TELEPORT_KUBE_CLUSTER environment support in tsh while preserving CLI precedence. Verify TELEPORT_CLUSTER/TELEPORT_SITE and TELEPORT_HOME precedence.
Status: Complete. Added kube cluster environment fallback after CLI parsing, extended focused tests for Kubernetes cluster and home precedence. Existing site/cluster behavior already matched requirements.
Tests: go test ./tool/tsh -run 'Test(ReadClusterFlag|ReadKubeClusterFlag|ReadTeleportHome)$' -count=1 (passed); git diff --check (passed).
Delegation: None; solved directly.
