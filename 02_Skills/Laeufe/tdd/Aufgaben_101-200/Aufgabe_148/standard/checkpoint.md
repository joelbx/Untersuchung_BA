# Checkpoint

Task: support Teleport-Proxy-prefixed SSH connections and forward ClientAddr.
Plan: inspect multiplexer and existing proxy format; add failing regression test; implement minimal fix; run relevant and full tests.
Tooling: `rg` is unavailable (`/bin/sh: rg: not found`); using local find/grep instead.

Regression: `go test ./lib/multiplexer -run '^TestDetectTeleportProxySSH$' -count=1` failed as expected before implementation (unknown protocol for Teleport prefix), then passed after implementation.
Package check: `go test ./lib/multiplexer -count=1` passed.
Repository check: `go test ./...` started; awaiting result.
Repository check outcome: `go test ./...` failed during compilation: `github.com/flynn/hid` requires missing `linux/hidraw.h`; `github.com/mattn/go-sqlite3` reported undeclared `pread64`/`pwrite64` and unknown `off64_t`. The run was interrupted after these build errors; other package results are unknown. No dependencies were downloaded.
Hostname regression: `go test ./lib/multiplexer -run '^TestDetectTeleportProxySSH/client_hostname$' -count=1` failed as expected (`client.example:4567` became `:4567`), then `go test ./lib/multiplexer -count=1` passed after preserving hostnames. `git diff --check` passed.
