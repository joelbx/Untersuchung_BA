Task: Fix ACP email validation for expired/missing confirmation data.
Status: Implementation complete; focused existing tests and new regression tests pass.
Changes: Dual confirmation keys with explicit expiry, pending/fallback/expiry utilities, ACP four-state display, admin missing-email errors, cleanup on confirmation/reset/deletion.
Verification: test/user.js focused email confirmation + profile update (8 passing); test/socket.io.js validation emails (5 passing); ESLint and git diff --check passed.
Delegation: None; solved directly.
