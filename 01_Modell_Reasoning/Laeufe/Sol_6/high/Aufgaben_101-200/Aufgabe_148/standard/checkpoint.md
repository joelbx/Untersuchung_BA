Task: support Teleport-Proxy-prefixed inbound SSH connections.
Status: implemented prefix recognition, bounded JSON parsing, client address propagation, and byte replay for the SSH server. Added listener tests for IPv4, IPv6, absent ClientAddr, and standard SSH.
Verification: `GOTOOLCHAIN=local GOPROXY=off go test ./lib/multiplexer` passed; `git diff --check` passed.
