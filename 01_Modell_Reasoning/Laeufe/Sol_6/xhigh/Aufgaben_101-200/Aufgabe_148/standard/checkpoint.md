# Checkpoint

Task: support Teleport-Proxy-prefixed SSH connections in the multiplexer and expose ClientAddr through RemoteAddr.

Completed: the multiplexer recognizes the Teleport-Proxy signature as SSH, inspects the null-terminated JSON payload, and forwards ClientAddr as the connection's remote address. The header remains buffered so the SSH server's existing parser still receives tracing metadata. Tests cover prefixed routing, ClientAddr, tracing-only payloads, ordinary SSH, and a complete SSH handshake that checks RemoteAddr during authentication.

Validation: `go test ./lib/multiplexer` passed; `git diff --check` passed.
