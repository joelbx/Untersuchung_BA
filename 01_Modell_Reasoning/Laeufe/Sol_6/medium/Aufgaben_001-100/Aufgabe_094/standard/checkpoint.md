Task: Enable Touch ID registration and login on macOS.
Status: Implemented public DiagResult and Diag, native macOS diagnostics for signing, Keychain entitlements, biometric policy, and Secure Enclave key creation. macOS IsAvailable now uses the aggregate result. Added non-Touch ID diagnostic test.
Verification: go test ./lib/auth/touchid ./lib/auth/webauthn passed; git diff --check passed. Existing touchid test covers registration, JSON parsing, credential creation, passwordless login, username, and assertion validation using a fake native provider.
Limitation: macOS native Objective-C code cannot be compiled or run in this Linux workspace.
