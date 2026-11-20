# Checkpoint

Task: support Teleport-Proxy-prefixed SSH connections.
Status: investigating mux detection and address propagation.
Tooling: rg unavailable; using grep/find.

Root cause: detectProto only recognizes SSH bytes at the start of a connection. Teleport senders emit `Teleport-Proxy` + JSON + NUL before SSH bytes, so detection rejects the connection before routing. Conn.RemoteAddr currently only supports HAProxy source addresses. Existing sender format and HandshakePayload are in api/utils/sshutils/ssh.go and lib/srv/regular/proxy.go.
Hypothesis: classify the exact Teleport signature as SSH, consume and decode its bounded payload during detection, and override Conn.RemoteAddr with a parsed TCP address. A new integration test verifies routing, address override, prefix removal, and plain SSH behavior.
Pre-fix reproduction: `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer -run '^TestTeleportProxySSH$' -count=1 -timeout=90s` exited 1: both prefixed cases timed out waiting for SSH routing; plain SSH passed.

Implemented: detect the exact Teleport-Proxy signature as SSH; consume a bounded, NUL-terminated JSON HandshakePayload; parse ClientAddr into a TCP address; expose it through Conn.RemoteAddr. The header is removed before forwarding SSH bytes. Plain SSH and absent ClientAddr retain the original socket address.
Verification: `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer -run '^TestTeleportProxySSH$' -count=1 -timeout=90s` passed after the fix. `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer -count=1 -timeout=180s` passed. `git diff --check` passed.
