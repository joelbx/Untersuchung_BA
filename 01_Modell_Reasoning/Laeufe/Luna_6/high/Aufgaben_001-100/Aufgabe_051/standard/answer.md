Implemented `TELEPORT_KUBE_CLUSTER` support in `tsh`. The environment value sets `KubernetesCluster` unless a CLI value is provided. Existing site and home environment handling already meets the requested precedence and normalization.

Added tests for Kubernetes precedence and `TELEPORT_HOME` overriding and normalizing the CLI path.

Validation passed: `go test ./tool/tsh` and `git diff --check`.