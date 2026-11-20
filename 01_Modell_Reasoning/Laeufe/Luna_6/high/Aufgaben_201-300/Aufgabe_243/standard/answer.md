Updated [forwarder.go](/app/lib/kube/proxy/forwarder.go) to reject sessions without a selected Kubernetes cluster, prefer local credentials before service discovery, and route endpoint connections through `dialEndpoint`. Selected kube_service addresses are recorded on the session.

Updated the remote session test fixture to include a selected cluster.

Verification: `go test ./lib/kube/proxy` passed. `git diff --check` passed.