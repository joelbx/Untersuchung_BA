Added the public `DiagResult` and `Diag` API in [api.go](/app/lib/auth/touchid/api.go:43). macOS diagnostics check the code signature, required entitlements, biometric policy, and Secure Enclave key creation; builds without Touch ID report unavailable in [api_darwin.go](/app/lib/auth/touchid/api_darwin.go:82) and [api_other.go](/app/lib/auth/touchid/api_other.go:24).

The existing registration and login round-trip test covers response parsing, credential creation, passwordless login, and login validation. It passed with `go test -count=1 ./lib/auth/touchid`; `git diff --check` also passed.

The native Objective-C diagnostics could not be compiled or run in this non-macOS environment.