# Touch ID WebAuthn work

Implemented public `DiagResult` and `Diag`, with macOS checks for binary signature, required entitlements, biometric policy, and Secure Enclave key creation. The macOS native availability hook now uses the diagnostic result. The existing Register/Login flow remains usable when the native availability hook succeeds; its end-to-end test covers registration, JSON parsing, credential creation, passwordless assertion parsing, login validation, and owner username.

Verification:
- `GOTOOLCHAIN=local GOPROXY=off go test ./lib/auth/touchid -run TestRegisterAndLogin -count=1` — passed.
- `GOTOOLCHAIN=local GOPROXY=off go test ./lib/auth/touchid -count=1` — passed.
- `GOTOOLCHAIN=local GOPROXY=off go test ./lib/auth/touchid ./lib/auth/webauthn -count=1` — passed.
- `git diff --check` — passed.

Limitation: this workspace is Linux, so the macOS Objective-C diagnostic code could not be compiled or exercised here. Its Secure Enclave test may require validation on a signed macOS binary with Touch ID hardware.
