Task: Support Teleport-Proxy-prefixed SSH connections in the SSH multiplexer.
Status: Implemented and verified.
Changes: Detect full Teleport-Proxy signature as SSH; inspect bounded null-terminated JSON without consuming it; expose ClientAddr through multiplexer Conn.RemoteAddr while retaining payload for SSH server tracing. Added listener-level tests for prefixed and standard SSH.
Verification: GOPROXY=off go test ./lib/multiplexer -count=1 passed; git diff --check passed.
