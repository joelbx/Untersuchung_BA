The SSH multiplexer now recognizes `Teleport-Proxy` connections, consumes their null-terminated JSON header, and exposes `ClientAddr` through `RemoteAddr()`. Standard SSH behavior remains unchanged.

The new [integration test](/app/lib/multiplexer/teleport_proxy_test.go) covers routing, address propagation, and plain SSH. The full `lib/multiplexer` test package passes.