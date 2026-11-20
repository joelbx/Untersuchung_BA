# Checkpoint

Task: resolve multi-device U2F authentication in `/app`.

Implementation: the legacy U2F sign-request path now returns challenges for every registered U2F device in a compatibility wrapper. Auth client types and the CLI signer accept both the wrapper and legacy single-challenge payloads. Added a focused auth test covering multiple challenges, legacy JSON compatibility, and signatures from both devices.

Verification complete:

- `go test ./lib/auth -run 'TestU2FSignRequestMultipleDevices|TestMFADeviceManagement' -count=1`
- `go test ./lib/client ./lib/web -run '^$'`
- `go test ./tool/tsh -run '^$'`
- `git diff --check`

All commands passed. Final status and diff review complete.
