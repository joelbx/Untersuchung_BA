The SSH multiplexer now recognizes `Teleport-Proxy` headers as SSH, extracts `ClientAddr` for `RemoteAddr()`, and passes the header through to the SSH server for its existing metadata handling. Standard SSH behavior remains covered by tests.

Validation passed: `go test ./lib/multiplexer -count=1` and `git diff --check`.