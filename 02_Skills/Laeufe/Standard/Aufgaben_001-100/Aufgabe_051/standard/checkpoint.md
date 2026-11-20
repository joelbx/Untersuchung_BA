# Checkpoint

Implemented `TELEPORT_KUBE_CLUSTER` in `tsh` CLI configuration. The environment value is applied only when no Kubernetes cluster was specified on the CLI. Existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` and `TELEPORT_HOME` behavior was verified and covered with additional home precedence cases.

Verification: `GOPROXY=off GOSUMDB=off go test ./tool/tsh -run '^(TestReadClusterFlag|TestReadKubeClusterFlag|TestReadTeleportHome)$' -count=1` passed. `git diff --check` passed.

Tooling note: `rg` is unavailable (`/bin/bash: rg: command not found`); repository inspection used `grep` and `find`.
