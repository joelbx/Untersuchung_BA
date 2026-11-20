VERDICT: FIX

**Code defect:** [forwarder.go](/app/lib/kube/proxy/forwarder.go:1554) selects one `kube_service` endpoint per session, and [clusterSession.dial](/app/lib/kube/proxy/forwarder.go:1401) returns immediately if that endpoint fails. With one unavailable service and one healthy service, connections can fail depending on which is selected. Restore attempts across the discovered endpoints, recording the address and `serverID` of the endpoint that succeeds.

**Tests:** `go test ./lib/kube/proxy -run 'Test(NewClusterSession|DialWithEndpoints)$' -count=1` passed; `go test ./lib/kube/proxy -count=1` passed. The existing tests do not cover one failed endpoint among multiple services.

**TEST_ENVIRONMENT_PROBLEM:** None.