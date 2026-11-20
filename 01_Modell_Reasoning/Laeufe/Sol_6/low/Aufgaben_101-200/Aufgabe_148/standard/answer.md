The SSH multiplexer now routes `Teleport-Proxy` connections as SSH, parses their null terminated JSON payload, and exposes `ClientAddr` through `RemoteAddr()`. It preserves the preamble for the SSH server, which also reads its tracing metadata. Standard SSH behavior remains covered by the package tests.

Verification: `go test ./lib/multiplexer` passed.