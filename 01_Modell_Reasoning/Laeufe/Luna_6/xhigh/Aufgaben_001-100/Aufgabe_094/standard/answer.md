Implemented `DiagResult` and `Diag()`. The macOS diagnostics check code signing, entitlements, biometric policy availability, and Secure Enclave key creation; `IsAvailable()` now reflects those checks. The existing registration and passwordless login flow passes its end-to-end test.

Changed [api.go](/app/lib/auth/touchid/api.go), [api_darwin.go](/app/lib/auth/touchid/api_darwin.go), [api_other.go](/app/lib/auth/touchid/api_other.go), and added [diag.m](/app/lib/auth/touchid/diag.m) and [diag.h](/app/lib/auth/touchid/diag.h).

Verification passed: `go test ./lib/auth/touchid ./lib/auth/webauthn ./lib/auth/webauthncli` and `git diff --check`. The Darwin-only Objective-C code was not compiled in this environment.