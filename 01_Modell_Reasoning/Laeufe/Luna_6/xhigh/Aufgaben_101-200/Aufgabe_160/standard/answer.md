Implemented peer address reporting for gRPC and in-memory inventory streams. SSH heartbeats now replace wildcard or localhost hosts with the stream peer host while preserving the heartbeat port.

Added coverage for IPv4 and IPv6 wildcards, routable addresses, and an empty peer address. The checkpoint is at [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).

**Verification:** `go test ./lib/inventory`, focused inventory pipe tests, and `git diff --check` passed. The standalone API module test could not resolve an uncached dependency with downloads disabled; the focused API client tests passed through the root module.