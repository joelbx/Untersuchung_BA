# Checkpoint

Task: Support `Teleport-Proxy`-prefixed SSH connections in the repository at `/app`.

Status: Implemented detection and parsing of the prefixed SSH hello in `lib/multiplexer/multiplexer.go`, address propagation in `wrappers.go`, and routing/replay tests in `multiplexer_test.go`. The hello is replayed so the SSH server can still read its tracing context.

Verification: `go test ./lib/multiplexer -run 'TestTeleportProxySSH|TestTeleportProxyInvalidPayload|TestProtocolString' -count=1` passed; `go test ./lib/multiplexer -count=1` passed; `git diff --check` passed.
