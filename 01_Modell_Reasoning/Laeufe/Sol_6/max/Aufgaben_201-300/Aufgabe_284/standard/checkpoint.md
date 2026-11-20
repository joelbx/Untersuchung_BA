# Checkpoint

- Task: replace the reverse tunnel server's local-site slice with one `localSite` and reuse the proxy's existing access point and clients.
- Repository state: clean at start. Changed `lib/reversetunnel/srv.go`, `localsite.go`, and their existing test files.
- Result: one `server.localSite` is constructed, its auth client and proxy access point are reused, and service connections validate the certificate cluster against the local cluster.
- Verification: `GOPROXY=off GOSUMDB=off go test ./lib/reversetunnel` passed.
