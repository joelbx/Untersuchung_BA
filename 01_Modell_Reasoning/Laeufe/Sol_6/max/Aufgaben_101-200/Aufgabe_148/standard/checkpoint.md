# Checkpoint

Task: Support `Teleport-Proxy` JSON prefixes on inbound SSH multiplexer connections, including client address forwarding.

Status: Implemented and verified. The multiplexer recognizes and parses null terminated `Teleport-Proxy` JSON headers, forwards the connection as SSH, and exposes `ClientAddr` through `RemoteAddr()`. It preserves the header for the SSH server to read tracing metadata; the server handles headers up to 16 KiB, including payloads longer than its initial read.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer ./lib/sshutils -count=1` passed. `git diff --check` passed. No external research or downloads were used.
