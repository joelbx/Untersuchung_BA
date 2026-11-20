`tsh` now reads `TELEPORT_KUBE_CLUSTER` after parsing CLI arguments. It uses the environment value when no Kubernetes cluster was specified on the CLI. Existing `TELEPORT_CLUSTER`/`TELEPORT_SITE` precedence and `TELEPORT_HOME` override and path normalization remain in place.

Added precedence tests, and the full `tool/tsh` test suite passes: `go test ./tool/tsh -count=1`.