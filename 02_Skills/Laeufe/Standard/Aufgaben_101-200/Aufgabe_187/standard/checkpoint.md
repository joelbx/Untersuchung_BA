# Checkpoint

Resolved the Kubernetes interactive session failure in the checked-out repository.

- Kubernetes service initializes the uploader during startup, creating the streaming upload directory.
- Forwarder uses explicit auth, cached auth, tunnel, and connection ping configuration fields and delegates ServeHTTP to its internal router.
- Request-specific cluster sessions are rebuilt for each request; only short-lived user TLS credentials are cached. Concurrent CSRs for the same key are serialized, and cached certificates are reused only while more than one minute remains before expiry.
- Exec, port forwarding, and catch-all audit events use the forwarder lifetime context so client cancellation does not suppress them. Exec logs response status errors and emits failure events after stream errors.
- Kubernetes TLS heartbeat announcer uses AuthClient.

Checks run successfully: `go test ./lib/kube/proxy ./lib/service`; `git diff --check`. The go test build printed an upstream sqlite3 C compiler warning but exited successfully.
