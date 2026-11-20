VERDICT: FIX
Code defect: lib/kube/proxy/forwarder.go:1554 selects one kube_service endpoint for the session, and :1412 returns immediately if dialing it fails. The previous implementation tried other discovered endpoints. With one unavailable service and one healthy service, connection success is now random; preserve retry/failover while updating the session address and serverID to the endpoint that succeeds.
Tests executed: `go test ./lib/kube/proxy -run 'Test(NewClusterSession|DialWithEndpoints)$' -count=1` => PASS; `go test ./lib/kube/proxy -count=1` => PASS. Existing tests do not cover a failed endpoint among multiple kube_services.
TEST_ENVIRONMENT_PROBLEM: none.
