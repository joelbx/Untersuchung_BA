# Checkpoint

Task: Better handle HA database access.
Status: implemented and verified.

Changes:
- Database server string includes HostID; sorting uses name then HostID; display deduplication preserves first occurrence.
- Fake remote site can mark individual ServerIDs offline with connection problem errors.
- Proxy retains all matching database servers, shuffles candidate order (with an injectable hook), and tries each candidate on tunnel connectivity failures. It reports a connection problem if none can be reached.
- `tsh db ls` sorts and deduplicates before rendering.
- Added API type tests and an integration test for offline first tunnel and all tunnels offline.

Verification: `GOPROXY=off go test ./types` in api; `GOPROXY=off go test ./lib/reversetunnel ./lib/srv/db ./tool/tsh` in root; focused database access test and API type tests passed. Final tsh compile check passed.
