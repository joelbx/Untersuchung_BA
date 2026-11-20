Implemented Teleport-Proxy-prefixed SSH support in the multiplexer. It validates the null-terminated JSON payload, routes the connection to SSH, exposes `ClientAddr` via `RemoteAddr()`, and replays the preamble so the SSH server can process tracing metadata.

Added a regression test for SSH classification, address propagation, and preamble replay.

Verification passed: `go test ./lib/multiplexer` and `git diff --check`.