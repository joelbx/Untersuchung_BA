The SSH multiplexer now recognizes `Teleport-Proxy` headers as SSH, parses the JSON payload through its null terminator, and exposes `ClientAddr` through `RemoteAddr()`. It replays the header so the SSH server can still read tracing metadata. Ordinary SSH behavior is unchanged.

`go test ./lib/multiplexer ./lib/sshutils` and `git diff --check` passed. No delegation was used.