Resolved the Kubernetes session connection issue in [forwarder.go](/app/lib/kube/proxy/forwarder.go). Sessions now validate the cluster name, prefer local credentials, use the reverse tunnel for remote clusters, and record the selected kube_service endpoint.

Verification passed: `go test ./lib/kube/proxy -count=1` and `git diff --check`.