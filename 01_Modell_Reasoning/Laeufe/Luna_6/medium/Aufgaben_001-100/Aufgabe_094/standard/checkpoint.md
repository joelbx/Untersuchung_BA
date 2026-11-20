# Checkpoint

Task: resolve macOS Touch ID WebAuthn registration and login support.

Inspection found the Touch ID API already constructs WebAuthn attestation/assertion data and handles passwordless discovery. Added the requested public `DiagResult` and `Diag` API and routed `IsAvailable` through its aggregate result. The diagnostic flags currently mirror the native implementation's single availability signal because the native interface does not yet expose the finer-grained checks.

Verification: `go test ./lib/auth/touchid ./lib/auth/webauthncli` passed.
