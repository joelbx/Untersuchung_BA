The SSH multiplexer now recognizes `Teleport-Proxy` headers, consumes the null-terminated JSON payload, routes the connection as SSH, and exposes a valid `ClientAddr` through `RemoteAddr()`. Standard SSH connections retain their existing behavior.

Verification passed: `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer -count=1` and `git diff --check`.