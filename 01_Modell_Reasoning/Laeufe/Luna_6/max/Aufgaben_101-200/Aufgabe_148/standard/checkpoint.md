# Checkpoint

Task: Support inbound SSH connections prefixed with `Teleport-Proxy`, a JSON payload, and a null terminator. Classify these as SSH and expose a payload `ClientAddr` as the connection's remote address while preserving standard SSH behavior.

Findings: `lib/sshutils/server.go` already parses the prefixed JSON handshake, strips it before SSH negotiation, imports its `ClientAddr`, and exposes that address through `RemoteAddr()`. The multiplexer previously rejected the prefix before it reached the SSH server.

Change: `lib/multiplexer/multiplexer.go` now confirms the complete `Teleport-Proxy` signature and classifies the connection as `ProtoSSH`. The detection reader remains buffered and is passed through, preserving the handshake for existing metadata and tracing handling. Standard SSH detection is unchanged.

Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./lib/multiplexer` passed.
