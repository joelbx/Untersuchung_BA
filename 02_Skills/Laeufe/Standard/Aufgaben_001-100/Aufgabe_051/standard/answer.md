`tsh` now reads `TELEPORT_KUBE_CLUSTER` into `KubernetesCluster` when no Kubernetes cluster was specified on the CLI. I added tests for that precedence and for the existing `TELEPORT_HOME` override behavior. The existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` precedence tests also pass.

The focused `tool/tsh` tests and `git diff --check` passed.