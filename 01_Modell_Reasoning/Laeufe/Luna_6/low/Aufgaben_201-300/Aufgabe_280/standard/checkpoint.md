Task: fix teleport-kube-agent Kubernetes backend environment variable handling.

Plan: locate backend constructor and its tests, define/use namespace and release environment constants, validate namespace and replica name, adjust environment test setup, then run the relevant existing tests.
