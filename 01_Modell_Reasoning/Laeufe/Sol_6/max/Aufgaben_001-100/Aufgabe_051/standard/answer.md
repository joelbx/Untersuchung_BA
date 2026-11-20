`tsh` now reads `TELEPORT_KUBE_CLUSTER` into `KubernetesCluster` after CLI parsing, so a CLI-selected cluster takes precedence. I updated the CLI reference and added precedence tests; the existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` tests and expanded `TELEPORT_HOME` tests also pass.

Verification: targeted `tool/tsh` tests passed, and `git diff --check` found no issues.