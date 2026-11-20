# Fault localization checkpoint

Authentication config validation reaches startup through `config.Load` (`internal/config/config.go`) and `buildConfig` (`cmd/flipt/main.go`). `AuthenticationConfig.validate` iterates method hooks only after session-domain validation. `AuthenticationMethod[C].validate` skips disabled methods.

Likely fault: `AuthenticationMethodOIDCConfig.validate` unconditionally returns nil; `AuthenticationMethodGithubConfig.validate` only checks organization scope and emits an unqualified message. Both are in `internal/config/authentication.go`. Required credential checks should use the actual OIDC provider map key or `github`, exact snake-case field names, and existing `errValidationRequired`/`errFieldWrap` helpers or equivalent wrapping. Preserve the `read:org` condition with the required provider/field-qualified message.

Existing `TestLoad` has the GitHub scope fixture but expects the old error text. That fixture omits GitHub credentials, so a fix that checks credentials first will need the fixture updated to include them; add missing-field cases for GitHub and named OIDC providers, including disabled-method behavior. The advanced fixture has complete credentials for both.

No project source or tests modified; no tests run. This is a diagnosis-only role.
