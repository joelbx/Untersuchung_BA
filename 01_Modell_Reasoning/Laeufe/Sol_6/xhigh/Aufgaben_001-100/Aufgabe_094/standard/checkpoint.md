Task: Enable Touch ID registration and passwordless login on macOS.
Status: Implemented DiagResult and Diag, macOS native signing/entitlement/biometric/Secure Enclave checks, and cached native availability. Expanded the existing WebAuthn round trip test to cover credential-filtered login as well as passwordless login. Added an untagged diagnostic test.
Validation: `go test -count=1 ./lib/auth/touchid ./lib/auth/webauthn` passes; `git diff --check` passes. Native Apple framework behavior cannot be exercised from this Linux workspace.
