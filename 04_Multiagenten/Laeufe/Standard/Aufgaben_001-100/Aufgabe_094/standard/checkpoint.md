# Touch ID WebAuthn flow

Added Touch ID diagnostics for signing, Keychain entitlements, biometric policy,
and Secure Enclave key creation. The existing WebAuthn round trip passes for
passwordless login and an allowed credential. `go test ./lib/auth/touchid
-count=1` passed on Linux. macOS native checks cannot run in this workspace.
