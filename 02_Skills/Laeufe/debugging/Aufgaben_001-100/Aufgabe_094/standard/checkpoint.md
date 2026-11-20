# Touch ID WebAuthn work

Status: investigating existing registration, login, diagnostics, and tests.

Evidence: `go test ./lib/auth/touchid -run TestRegisterAndLogin -count=1 -v` passed, including passwordless JSON parsing and WebAuthn validation. The current macOS `touchIDImpl.IsAvailable` unconditionally returns true. No `Diag` interface exists. Build assets contain application identifier and keychain access group entitlements. Root cause of inaccurate availability reporting is the unconditional macOS implementation; existing response construction is already validated by its local fake native test.

Hypothesis: detailed macOS checks exposed by `Diag`, with `IsAvailable` derived from their aggregate, will prevent false availability while keeping the established response flow intact.

Reproduction: Added `TestDiag` before implementation. `go test ./lib/auth/touchid -run TestDiag -count=1` failed with `undefined: touchid.Diag` and `undefined: touchid.DiagResult`, confirming the missing public API.

Implementation: `DiagResult` and `Diag` now expose compile, signature, entitlement, biometric policy, Secure Enclave, and aggregate status. The macOS native check validates the current code signature and the entitlements used by both tsh build profiles, checks biometric policy, and probes Secure Enclave key creation with registration's access control, deleting the probe key afterward. `IsAvailable` caches the aggregate check. The existing Register/Login response path remains unchanged; the test now covers both allowed-credential and passwordless login.

Verification: `go test ./lib/auth/touchid -count=1 -v` passed (Register/Login scenarios and Diag); `go test ./lib/auth/webauthn -count=1` passed; `git diff --check` passed.

macOS verification limit: `GOOS=darwin CGO_ENABLED=1 go test -tags touchid ./lib/auth/touchid -run '^TestDiag$' -count=1` failed on this Linux host with `# runtime/cgo` and `gcc: error: unrecognized command-line option '-arch'`. Native Objective-C compilation and hardware behavior remain unverified here.

Environment: `rg` is unavailable (`/bin/bash: rg: command not found`); use local `find` and `grep` for repository inspection.

