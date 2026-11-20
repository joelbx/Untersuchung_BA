Implemented multi-device U2F challenges. The auth server now generates a challenge for every registered U2F device and returns them in [U2FAuthenticateChallenge](</app/lib/auth/auth.go:828>), while preserving the legacy top-level challenge fields.

Updated auth and web client types plus the CLI signer to handle both the new list and legacy single-challenge responses. Added coverage for compatibility and successful authentication with either device in [grpcserver_test.go](</app/lib/auth/grpcserver_test.go:473>).

Verification passed:

- `go test ./lib/auth -run 'TestU2FSignRequestMultipleDevices|TestMFADeviceManagement' -count=1`
- `go test ./lib/client ./lib/web -run '^$'`
- `go test ./tool/tsh -run '^$'`
- `git diff --check`