The SSH multiplexer now routes `Teleport-Proxy` connections with null-terminated JSON as SSH. When the payload contains `ClientAddr`, the connection exposes it through `RemoteAddr()`. The prefix is replayed so the SSH server can read its metadata; standard SSH behavior remains covered by the existing tests.

Validation passed: `go test ./lib/multiplexer -count=1` and `git diff --check`.