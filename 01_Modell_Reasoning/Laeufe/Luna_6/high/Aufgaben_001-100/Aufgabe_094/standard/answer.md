Added the public `DiagResult` type and `Diag()` function, with build specific results in [diag_darwin.go](/app/lib/auth/touchid/diag_darwin.go) and [diag_other.go](/app/lib/auth/touchid/diag_other.go).

The repository already had the registration and passwordless login flow. Its round trip test passes, including WebAuthn response parsing and validation.

Verification: `go test ./lib/auth/touchid` and the focused `TestRegisterAndLogin` test pass. The macOS diagnostic flags currently reflect the native availability stub, which reports available in Touch ID builds.