# Touch ID WebAuthn flow

Status: implemented diagnostics and fixed allowed-credential selection. The registration and passwordless login round trip already passed the existing test; added a multiple-credential case.

Validation: `go test ./lib/auth/webauthn ./lib/auth/touchid -count=1` and `git diff --check` pass. macOS native diagnostics could not be run on this Linux host.
