Added `DiagResult` and `Diag` for Touch ID. On macOS, diagnostics check the code signature, entitlements, biometric policy, and Secure Enclave access; their combined result now determines availability.

The existing registration and passwordless login flow test passes, as does the full `lib/auth/touchid` test package. Native Secure Enclave behavior remains unverified because this host runs Linux.