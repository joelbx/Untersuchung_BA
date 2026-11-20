Task: Enable Touch ID registration and login flow on macOS in lib/auth/touchid.
Status: Implemented public DiagResult/Diag, macOS signature/entitlement/biometry/Secure Enclave checks, no-op diagnostics on untagged builds, and fixed allowed-credential selection. Expanded the existing WebAuthn round-trip test to cover multiple credentials.
Verification: go test ./lib/auth/touchid -count=1 passed; go test ./lib/auth/webauthn -run 'Test.*' -count=1 passed; git diff --check passed. macOS native code cannot be compiled or exercised in this Linux workspace.
Constraints: local repository only; no git history/index/harness changes.
