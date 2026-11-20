# Checkpoint

Task: support Teleport-Proxy-prefixed inbound SSH connections and preserve ClientAddr as remote address.

Implemented in `lib/multiplexer/multiplexer.go` and `wrappers.go`: detect the shared Teleport proxy signature as SSH, consume and parse the null-terminated JSON header with a 64 KiB bound, and expose a valid client IP:port as `RemoteAddr()`. Standard SSH bytes remain buffered for the SSH server. Added focused parsing and listener-routing tests in `multiplexer_test.go`.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer -run TestTeleportProxySSHHeader -count=1` — passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer -count=1` — passed.
- `git diff --check` — passed.

Tooling note: `rg` is unavailable (`/bin/sh: rg: not found`); used local `find` and `grep`.
