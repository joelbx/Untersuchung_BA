Added the public `DiagResult` type and `Diag()` function. Compile support is reported per build; aggregate availability uses the native backend. The existing registration and login paths already support the requested WebAuthn round trips and passwordless login.

Verification: `go test ./lib/auth/touchid/...` passed.

The current native interface exposes only a single availability boolean, so `Diag()` leaves the individual signature, entitlement, LocalAuthentication, and Secure Enclave flags false. The checkpoint records this limitation in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md).