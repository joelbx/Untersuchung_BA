Task: repair Kubernetes exec sessions and forwarder lifecycle in the checked-out repository.
Status: implementation complete. Kubernetes startup creates the streaming directory and starts the uploader for a standalone kube service. Forwarder now caches only short-lived TLS credentials, rebuilds request sessions, retains audit events after disconnects, and uses the renamed configuration fields and internal router.
Verification: go test ./lib/kube/proxy -count=1 passed; go test ./lib/service -run '^$' passed; git diff --check passed.
