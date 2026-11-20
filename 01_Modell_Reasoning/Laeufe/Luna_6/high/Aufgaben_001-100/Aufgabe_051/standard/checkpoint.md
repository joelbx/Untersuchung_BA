# Checkpoint

Task: Support environment defaults and requested precedence for `tsh` Kubernetes cluster, Teleport cluster, and home path configuration.

Implemented:
- Added `TELEPORT_KUBE_CLUSTER` handling after command-line parsing. It fills `CLIConf.KubernetesCluster` only when no CLI value is present.
- Confirmed `readClusterFlag` already gives CLI `SiteName` priority and otherwise prefers `TELEPORT_CLUSTER` to `TELEPORT_SITE`.
- Confirmed `readTeleportHome` already lets `TELEPORT_HOME` override CLI `HomePath` and normalizes with `path.Clean`.
- Added coverage for Kubernetes environment/default/CLI precedence and home override/trailing slash normalization.

Validation: `go test ./tool/tsh` passed; `git diff --check` passed.
