# Checkpoint

Task: support the requested `tsh` environment variables and precedence for `KubernetesCluster`, `SiteName`, and `HomePath`.

Progress: `tsh` reads site and home environment settings after CLI parsing. Site selection already honors CLI > `TELEPORT_CLUSTER` > `TELEPORT_SITE`; `TELEPORT_HOME` already overrides the CLI home and uses `path.Clean`. Added `TELEPORT_KUBE_CLUSTER`, applied only when the CLI did not provide a Kubernetes cluster. Verified with `go test ./tool/tsh` (passed).
