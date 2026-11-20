Fixed the Kubernetes interactive session path. Standalone Kubernetes service startup now initializes the session uploader, which creates the directory needed for async recordings.

The forwarder now caches only short lived CSR credentials and builds fresh cluster session state for each request. Audit events use the service context so a client disconnect does not cancel them, and exec stream and response errors are logged and included in the final audit event. I also renamed the forwarder config fields by responsibility, added `ServeHTTP` delegation to its internal router, and switched the TLS heartbeat announcer to `AuthClient`.

Validation passed: `go test ./lib/kube/proxy ./lib/service -run Test -count=1` and `git diff --check`.