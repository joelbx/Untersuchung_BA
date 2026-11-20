I traced the issue but did not edit project source or tests: this run’s fault-localization instruction limits me to a diagnosis.

- [authentication.go](/app/internal/config/authentication.go:291) has no `RequiresDatabase` field. Its five method definitions need explicit values: `false` for JWT and `true` for token, OIDC, GitHub, and Kubernetes. `AuthenticationConfig.RequiresDatabase()` should check enabled methods only.
- [authn.go](/app/internal/cmd/authn.go:55) uses `Authentication.Enabled()` to decide whether to call `getDB`, so JWT-only authentication on non-database storage still connects. The database-free path must retain JWT middleware setup; the current early return skips it.
- [authentication.go](/app/internal/config/authentication.go:85) and [cleanup.go](/app/internal/cleanup/cleanup.go:44) allow scheduled cleanup without checking database need. Cleanup should run only for enabled, database-requiring methods.
- [cleanup_test.go](/app/internal/cleanup/cleanup_test.go:61) expects JWT cleanup and will need its expectation updated.

I recorded the findings in [.codex-role-output/checkpoint.md](/app/.codex-role-output/checkpoint.md). No tests were run.