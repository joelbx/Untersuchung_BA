Updated the SSH multiplexer to route `Teleport-Proxy` connections as SSH and expose a JSON `ClientAddr` through `RemoteAddr()`. The prefix remains available to the SSH server for its existing tracing parser. Standard SSH behavior is unchanged.

Added listener tests for prefixed and standard SSH. `go test ./lib/multiplexer -count=1` passed.