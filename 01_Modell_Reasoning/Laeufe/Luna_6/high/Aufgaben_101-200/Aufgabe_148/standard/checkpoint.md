# Checkpoint

Task: support Teleport-Proxy-prefixed SSH connections in the SSH multiplexer.

Implemented in `lib/multiplexer`: the detector recognizes the Teleport proxy preamble, validates and parses its null-terminated JSON payload, routes the stream to SSH, exposes `ClientAddr` through `RemoteAddr()`, and replays the preamble for the SSH server's existing tracing metadata handler. Standard unprefixed SSH behavior remains covered by the package's existing tests.

Added a focused regression test covering SSH classification, remote address propagation, and preamble replay.

Verification: `go test ./lib/multiplexer` passed; `git diff --check` passed.
