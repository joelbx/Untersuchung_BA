The SSH multiplexer now routes `Teleport-Proxy`-prefixed connections as SSH. It reads the null-terminated JSON, exposes `ClientAddr` through `RemoteAddr()`, and replays the original hello so the SSH server can still read tracing metadata. Standard SSH behavior remains unchanged.

Added routing and payload tests. `go test ./lib/multiplexer -count=1` and `git diff --check` passed.