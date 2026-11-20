# Checkpoint

Task: support Teleport-Proxy-prefixed SSH connections and expose ClientAddr as RemoteAddr.

Implemented in `lib/multiplexer/multiplexer.go` and `lib/multiplexer/wrappers.go`: detect the prefix as SSH, consume a bounded null-terminated JSON metadata header, preserve the SSH stream, and prefer a parsed ClientAddr for RemoteAddr. Standard SSH remains unchanged. Added routing, address, banner, and malformed-header tests in `lib/multiplexer/multiplexer_test.go`.

Verification: `GOPROXY=off GOSUMDB=off go test ./lib/multiplexer` passed. `git diff --check` passed.

Local tooling note: `rg` is unavailable (`/bin/sh: rg: not found`); used local `find`/`grep` for repository inspection. No external research or downloads.
