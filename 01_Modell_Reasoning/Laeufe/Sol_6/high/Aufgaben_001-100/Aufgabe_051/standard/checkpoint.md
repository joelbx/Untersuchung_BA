Task: Add TELEPORT_KUBE_CLUSTER support in tsh CLI configuration and verify environment precedence.

Findings: tool/tsh/tsh.go already reads TELEPORT_CLUSTER, TELEPORT_SITE, and TELEPORT_HOME through small helpers. Existing cluster precedence matches the requested behavior. Added TELEPORT_KUBE_CLUSTER after CLI parsing with CLI precedence, tested the new cases, and expanded the home override test.

Verification: go test ./tool/tsh -run 'Test(ReadClusterFlag|ReadKubeClusterFlag|ReadTeleportHome)$' -count=1 passed.
