`tsh` now reads `TELEPORT_KUBE_CLUSTER` into `KubernetesCluster` after parsing CLI arguments, so a CLI cluster value takes precedence. I added tests for that behavior and for `TELEPORT_HOME` overriding a CLI home path. The existing tests cover `TELEPORT_CLUSTER` and `TELEPORT_SITE` precedence.

The focused `tsh` tests passed, and `git diff --check` found no issues.