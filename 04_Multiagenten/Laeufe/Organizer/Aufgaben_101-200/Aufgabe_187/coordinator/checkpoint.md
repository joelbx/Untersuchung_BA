Task: repair Kubernetes forwarder interactive sessions, uploader startup, credential cache, routing, and audit behavior.
Status: implemented and verified. Kubernetes startup creates the streaming directory and starts the uploader for a standalone kube service. Forwarder caches only TLS credentials with expiry checks and serialized CSR requests; sessions remain request scoped. Audit writes use the forwarder context, exec status errors are logged without skipping final events, HTTP routing delegates through an internal router, and configuration fields were renamed by responsibility.
Tests: `go test -mod=vendor ./lib/kube/proxy ./lib/service` passed; `git diff --check` passed.
Delegation: none.
