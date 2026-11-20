# Checkpoint

Task: fix Kubernetes `kubectl exec` interactive session initialization and Forwarder behavior per issue requirements.

Initial inspection: repository is a Go project; `rg` is unavailable, so use `find` and standard text search tools. Next locate Kubernetes forwarder/service code and relevant existing tests.
