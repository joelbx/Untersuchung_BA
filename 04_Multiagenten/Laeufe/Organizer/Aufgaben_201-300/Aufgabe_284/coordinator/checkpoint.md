# Checkpoint

Task: replace the reversetunnel server local site slice with one localSite and reuse the proxy cache.
Status: implemented; full lib/reversetunnel tests pass.
Validation: go test ./lib/reversetunnel -count=1; git diff --check.
Delegation: none.
