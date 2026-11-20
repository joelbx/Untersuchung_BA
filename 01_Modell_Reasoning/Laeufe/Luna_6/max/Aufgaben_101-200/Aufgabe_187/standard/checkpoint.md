# Checkpoint

Issue: Kubernetes `kubectl exec` failed when the streaming upload directory had not been initialized. Forwarder state and audit handling also needed to remain safe across client disconnects and disappearing remote clusters.

Implemented:
- Initialize the session uploader from Kubernetes service startup; make uploader initialization process-wide and idempotent.
- Rename forwarder dependencies to `Authz`, `AuthClient`, `CachingAuthClient`, `ReverseTunnelSrv`, and `ConnPingPeriod`; use those dependencies for authorization, auth reads, CSR requests, heartbeat announcements, and connection pings.
- Replace cached request-bound `clusterSession` values with a TTL cache for ephemeral TLS credentials, keyed by authenticated context and guarded by per-key CSR serialization. Certificates must have at least one minute of validity remaining.
- Route through an internal `httprouter.Router` with an explicit `ServeHTTP` method and catch-all `NotFound` handler.
- Emit exec, port-forward, and catch-all audit events using the service context. Ensure exec completion events run on error paths, including client disconnects, and log exec setup/response errors.

Validation: `go test ./lib/kube/proxy ./lib/service` passed. `git diff --check` passed.
