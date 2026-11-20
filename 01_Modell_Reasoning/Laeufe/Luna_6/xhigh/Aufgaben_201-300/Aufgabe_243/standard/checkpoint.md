# Checkpoint

Task: resolve inconsistent Kubernetes cluster session connection paths in `/app`.

Completed in `lib/kube/proxy/forwarder.go`:
- Added `kubeClusterEndpoint` carrying an endpoint address and server ID, plus the endpoint dialing method on `teleportClusterClient`.
- Made local session creation report a clear NotFound error for a missing cluster and prefer configured local credentials before kube_service discovery.
- Kept remote sessions on `reversetunnel.LocalKubernetes` and routed their connections through endpoint dialing with requested client credentials.
- Routed discovered kube_service endpoints through `clusterSession.dial`, recording the selected address and dialing with its server ID.
- Preserved the authenticated context, including kube users/groups and remote/local cluster fields, when creating sessions.

Verification: `go test ./lib/kube/proxy` passed; `git diff --check` passed. No external research was used.
