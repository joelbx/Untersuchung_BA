Added `DiagResult` and `Diag`, and wired macOS Touch ID availability to signing, entitlement, biometric policy, and Secure Enclave checks. Expanded the existing WebAuthn test to cover both passwordless and allowed-credential login.

`go test ./lib/auth/touchid` passes. The native macOS checks still need a run on macOS; this workspace is Linux.