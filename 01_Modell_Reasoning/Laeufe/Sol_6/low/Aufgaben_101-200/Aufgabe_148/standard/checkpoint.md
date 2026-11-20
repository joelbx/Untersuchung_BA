Task: support Teleport-Proxy-prefixed SSH connections.
Status: implemented SSH detection, bounded JSON preamble parsing, remote address override, and preamble replay for the SSH server.
Verification: go test ./lib/multiplexer passed.
