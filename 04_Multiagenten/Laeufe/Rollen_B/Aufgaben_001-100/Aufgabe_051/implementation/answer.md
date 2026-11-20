`tsh` now uses `TELEPORT_KUBE_CLUSTER` when no Kubernetes cluster was specified on the CLI. The CLI value takes precedence. I added tests for unset, environment, and CLI values, plus a test confirming that `TELEPORT_HOME` overrides a supplied path and removes its trailing slash.

The focused tests passed, and `git diff --check` found no issues.