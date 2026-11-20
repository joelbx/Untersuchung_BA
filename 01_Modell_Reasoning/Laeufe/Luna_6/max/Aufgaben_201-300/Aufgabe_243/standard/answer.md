Implemented the session routing changes in [forwarder.go](/app/lib/kube/proxy/forwarder.go):

- Missing cluster names now return `trace.NotFound`; matching local credentials take priority and supply their configured address and TLS settings.
- Remote sessions use the reverse tunnel endpoint through `dialEndpoint`.
- kube_service endpoints are discovered and one is selected per session. Its address is used for dialing, forwarding headers, and audit records. Missing endpoints return `trace.BadParameter`.
- Updated the remote session test to provide a cluster name.

Validation passed: `go test ./lib/kube/proxy` and `git diff --check`.