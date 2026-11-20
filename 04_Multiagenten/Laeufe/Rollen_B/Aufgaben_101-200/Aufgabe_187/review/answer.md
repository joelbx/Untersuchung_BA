VERDICT: FIX

**Code defect:** [forwarder.go](/app/lib/kube/proxy/forwarder.go:1316) returns and caches a newly issued CSR certificate without checking that its `NotAfter` is at least one minute away. That check runs only on a later cache lookup. Apply the same expiry check before caching or returning the new certificate.

**Tests executed:** `GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -count=1` and `GOPROXY=off GOSUMDB=off go test ./lib/service -count=1` both passed. The focused proxy commands (`-run 'Test(Authenticate|Forwarder)'` and `-run '^Test$'`, each with `-count=1`) also passed. The focused service command (`-run 'Test.*(Kube|Kubernetes|Uploader)' -count=1`) passed with **no tests matched**. `git diff --check` passed. **TEST_ENVIRONMENT_PROBLEM:** none.

I recorded the review in [checkpoint.md](/app/.codex-role-output/checkpoint.md). No project code or tests were changed.