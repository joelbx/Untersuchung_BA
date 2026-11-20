# Touch ID issue checkpoint

Goal: enable macOS Touch ID WebAuthn registration and login, including passwordless login and diagnostics.

Implemented: public DiagResult/Diag API; macOS checks for code signature, application entitlement, biometric LA policy, and Secure Enclave key creation; IsAvailable uses the aggregate result. Non-touchid builds return a zero diagnostic result. Expanded registration/login round trip test to cover allowlisted credentials alongside passwordless login.

Verification: `go test ./lib/auth/touchid -count=1` passed on Linux; `git diff --check` passed. macOS Security framework behavior cannot be exercised in this Linux environment.

No delegation used. No git history, index, or harness changes.
