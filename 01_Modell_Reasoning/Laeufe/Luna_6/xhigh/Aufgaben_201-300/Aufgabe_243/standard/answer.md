Updated [forwarder.go](/app/lib/kube/proxy/forwarder.go) to prefer configured local credentials, validate missing local cluster names, and route remote and kube_service connections through endpoint dialing with the selected address and server ID.

Verification passed: `go test ./lib/kube/proxy` and `git diff --check`.