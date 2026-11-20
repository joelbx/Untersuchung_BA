Updated the SSH multiplexer to recognize `Teleport-Proxy` JSON headers terminated by a null byte, route those connections as SSH, and expose `ClientAddr` through `RemoteAddr()`. Standard SSH behavior remains unchanged.

Added connection tests. `go test ./lib/multiplexer -count=1` passes.