# Checkpoint

Implemented Teleport-Proxy-prefixed SSH detection and bounded, NUL-terminated JSON header parsing in the multiplexer. ClientAddr overrides the SSH connection's RemoteAddr; ordinary SSH retains its existing address and stream behavior. Added an integration test for prefixed connections with and without ClientAddr and for standard SSH.

Verification: `go test ./lib/multiplexer -count=1` passed; `git diff --check` passed.
