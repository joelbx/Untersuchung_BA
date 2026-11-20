The SSH multiplexer now recognizes `Teleport-Proxy` JSON headers terminated by a null byte, routes those connections as SSH, and exposes `ClientAddr` through `RemoteAddr()`. It replays the header to the SSH server so the server can still read its metadata. Standard SSH behavior remains covered by the tests.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer -count=1` passed.