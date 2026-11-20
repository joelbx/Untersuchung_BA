Implemented the Kubernetes session and `Forwarder` fixes.

- Kubernetes startup initializes the session uploader once per process, creating and servicing the streaming upload directory.
- `ForwarderConfig` now uses the requested responsibility specific field names. TLS heartbeats use `AuthClient`.
- `Forwarder` implements `ServeHTTP`, creates fresh request scoped sessions, and caches only ephemeral certificates with serialized CSR requests and expiry checks.
- Audit events use the forwarder service context. Exec stream errors are audited before the handler returns.

Verification passed: `go test ./lib/kube/proxy ./lib/service` and `git diff --check`.