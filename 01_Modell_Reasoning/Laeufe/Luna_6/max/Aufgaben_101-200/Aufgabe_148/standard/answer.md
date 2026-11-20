Updated [multiplexer.go](/app/lib/multiplexer/multiplexer.go:416) to recognize the full `Teleport-Proxy` signature as SSH and preserve the buffered handshake for the SSH server. Its existing parser exposes `ClientAddr` through `RemoteAddr()`.

`GOTOOLCHAIN=local GOPROXY=off go test ./lib/multiplexer` passed.