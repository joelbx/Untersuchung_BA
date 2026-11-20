# Checkpoint

Task: Resolve the Kubernetes `kubectl exec` session uploader initialization and related Forwarder requirements from the issue.

Completed:
- Renamed Forwarder auth, cache, reverse tunnel, and connection ping config fields to reflect their responsibilities and updated service construction.
- Kept only reusable short lived Kubernetes certificates in the TTL cache; each request rebuilds its cluster session and closes request scoped idle transports.
- Added serialized CSR processing and a one minute certificate freshness check.
- Detached audit event contexts from client cancellation for exec, port forwarding, and catch all requests; exec failures are logged and still produce completion audit events.
- Initialized the uploader in Kubernetes only processes and wired the TLS heartbeat announcer to AuthClient.
- Added explicit `Forwarder.ServeHTTP` delegation to its router.

Verification:
- `go test ./lib/kube/proxy ./lib/service ./lib/events/filesessions` passed.
- `git diff --check` passed.

Constraints: No external research or downloads; git history, index baseline, and harness configuration were not changed.
