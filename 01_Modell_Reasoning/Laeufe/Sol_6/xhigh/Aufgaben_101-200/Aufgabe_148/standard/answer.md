The SSH multiplexer now recognizes null-terminated `Teleport-Proxy` JSON headers as SSH traffic and exposes `ClientAddr` through `RemoteAddr()`. It keeps the header available for the SSH server’s existing metadata parser. Standard SSH behavior remains unchanged.

The listener tests and an end-to-end SSH authentication test pass. Validation: `go test ./lib/multiplexer` and `git diff --check`.