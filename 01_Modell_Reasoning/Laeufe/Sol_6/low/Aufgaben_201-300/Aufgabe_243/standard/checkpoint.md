# Checkpoint
Implemented session endpoint selection in lib/kube/proxy/forwarder.go; local credentials are preferred, selected address is recorded, and endpoint dialing uses dialEndpoint.
Verification: go test ./lib/kube/proxy -count=1 passed.
