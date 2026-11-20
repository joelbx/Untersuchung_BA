# Touch ID registration and login

Goal: enable WebAuthn registration and passwordless login through macOS Touch ID when availability checks succeed.

Status: implemented public `DiagResult`/`Diag`, native macOS prerequisite checks, and a fix for allowed-credential selection when multiple local credentials exist. The existing WebAuthn registration/passwordless login test was extended to cover that selection case.

Validation: `GOPROXY=off GOSUMDB=off go test -count=1 ./lib/auth/touchid ./lib/auth/webauthn` passed; `git diff --check` and C header syntax check passed. Native Objective-C code cannot be compiled or exercised in this Linux workspace.
