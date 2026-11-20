# Checkpoint

Implemented support for `Teleport-Proxy` metadata frames in `lib/multiplexer`: the detector consumes the prefix, JSON payload, and null terminator before classifying the buffered connection; valid SSH traffic routes normally. Optional `ClientAddr` overrides `Conn.RemoteAddr()` while missing values preserve the socket address. Added coverage for both address-present and address-absent cases, including preservation of the initial SSH identification line.

Verification: `go test ./lib/multiplexer` passes.
