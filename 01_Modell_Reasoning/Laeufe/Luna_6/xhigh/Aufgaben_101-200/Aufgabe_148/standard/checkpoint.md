# Checkpoint

Task: support inbound `Teleport-Proxy`-prefixed SSH connections, parse optional `ClientAddr`, and expose it through the accepted connection's remote address while preserving ordinary SSH behavior.

Implementation:
- `lib/multiplexer` recognizes the `Teleport-Proxy` signature as SSH, reads and parses the null-terminated JSON handshake, and exposes parsed `ClientAddr` via `Conn.RemoteAddr()`.
- The consumed prefix and payload are replayed so the SSH server can continue extracting tracing context.
- Ordinary SSH and existing PROXY-protocol remote-address behavior remain as before when no Teleport `ClientAddr` is supplied.

Verification:
- `go test ./lib/multiplexer` passed.
- `go test ./lib/sshutils` passed.
- The nested API tracing SSH package test could not run because its dependencies are unavailable with `GOPROXY=off`.
