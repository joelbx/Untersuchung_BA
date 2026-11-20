The SSH multiplexer now recognizes null terminated `Teleport-Proxy` JSON headers as SSH, removes the header before forwarding the SSH stream, and exposes `ClientAddr` through `RemoteAddr()`. Standard SSH behavior remains unchanged.

The new routing, address, and malformed header tests passed with `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer`.