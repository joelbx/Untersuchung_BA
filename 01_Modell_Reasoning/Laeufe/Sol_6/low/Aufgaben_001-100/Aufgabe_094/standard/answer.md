Added the public `DiagResult` and `Diag` interfaces, with macOS checks for signing, entitlements, biometric policy, and Secure Enclave access. The existing registration and passwordless login round trip test passes with `go test ./lib/auth/touchid`.

The macOS specific code could not be compiled in this Linux workspace.