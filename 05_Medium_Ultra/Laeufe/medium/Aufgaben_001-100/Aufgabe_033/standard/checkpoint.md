# Checkpoint

Task: support authentication with any registered U2F device across server, CLI, and web while preserving legacy payloads. Keep MFA device management hidden.

Completed: `U2FAuthenticateChallenge` embeds a legacy challenge and includes all device challenges; server generates each challenge; auth client and CLI consume both formats; web endpoints pass the enhanced payload; tsh MFA management is hidden from help. Added JSON compatibility and multi-device web login tests.

Verification: `go test ./lib/auth ./lib/client ./lib/web ./tool/tsh -count=1` passed. `git diff --check` passed.
