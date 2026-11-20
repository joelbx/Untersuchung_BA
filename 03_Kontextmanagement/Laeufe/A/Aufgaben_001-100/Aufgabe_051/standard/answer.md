`tsh` now reads `TELEPORT_KUBE_CLUSTER` into `KubernetesCluster` when no Kubernetes cluster was specified on the CLI. The existing `SiteName` precedence and `TELEPORT_HOME` override and path normalization already meet the requested behavior. I added tests for Kubernetes cluster precedence and the home override.

The focused `tsh` tests and `git diff --check` passed.