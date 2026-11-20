Task: support Teleport-Proxy-prefixed SSH connections in the SSH multiplexer.
State: implemented prefix classification, bounded JSON/NUL parsing, ClientAddr override on multiplexer Conn.RemoteAddr, and header replay for existing SSH server tracing parser. Added regression tests for prefixed hello with/without ClientAddr and ordinary SSH.
Verification: go test ./lib/multiplexer ./lib/sshutils passed; git diff --check passed.
Constraints: local code/tests only; no history/index/harness changes. No delegation used.
