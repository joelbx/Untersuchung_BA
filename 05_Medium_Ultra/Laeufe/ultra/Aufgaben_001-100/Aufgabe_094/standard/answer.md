Added `Diag` and `DiagResult` in [api.go](/app/lib/auth/touchid/api.go:76). On macOS, [availability checks](/app/lib/auth/touchid/diag.m:17) now cover signing, entitlements, biometric policy, and Secure Enclave key creation. The result is cached per process so a successful check stays consistent through registration and login.

The existing Touch ID test confirms the full passwordless WebAuthn registration and login flow, including JSON parsing, credential validation, and the returned username. `GOMAXPROCS=2 go test -p 1 ./lib/auth/touchid ./lib/auth/webauthncli -count=1` passes.

I delegated the native diagnostics and an independent requirements review, then integrated and verified the patch. The native macOS path could not be run in this Linux workspace.