# Checkpoint

Task complete: Kubernetes exec sessions no longer require manual upload-directory creation. A Kubernetes-only process initializes the uploader; combined processes use the uploader owned by another enabled service.

Forwarder changes: explicit Authz/AuthClient/CachingAuthClient/ReverseTunnelSrv/ConnPingPeriod fields; internal httprouter with ServeHTTP; audit events and recorder close use the forwarder lifetime context; exec response failures are logged and final audit events are emitted; request-specific sessions are rebuilt each time; only short-lived CSR certificates are cached with per-key request serialization and at least one minute of remaining validity. Idle forwarding connections close after each request. Kubernetes TLS heartbeat uses AuthClient.

Verification: gofmt and git diff --check completed. go test ./lib/kube/proxy ./lib/service passed. Regression tests cover router NotFound delegation, certificate reuse with fresh session state, concurrent CSR sharing, and rejection of short-lived certificates.
