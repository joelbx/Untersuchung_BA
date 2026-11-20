Task: Fix Direct Dial SSH node heartbeat addresses that advertise wildcard hosts.

Plan: Trace inventory stream creation and heartbeat handling, pass the peer address through pipe options, rewrite non-routable heartbeat hosts while retaining the node port, and run relevant existing tests.

Status: Implemented PeerAddr for gRPC and pipe streams, added ICSPipePeerAddr, and corrected non-routable SSH heartbeat addresses before UpsertNode. Added regression tests for IPv4/IPv6 wildcard, loopback, routable, and absent peer cases. `go test ./lib/inventory` passed with GOPROXY=off. The API module's direct test cannot start because github.com/gogo/protobuf is unavailable locally with downloads disabled; the inventory test compiled the changed API package. `git diff --check` passed.
