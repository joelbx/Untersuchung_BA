# Checkpoint

Task: make startup reject incomplete GitHub and OIDC authentication configuration with the specified provider and field errors.

Status: implemented shared required-field validation for enabled GitHub and OIDC providers. GitHub scope errors now name the provider and field. The loader restores OIDC provider key spelling from YAML before validation because Viper lowercases map keys. Updated the existing scope fixture and added load-level cases for missing and blank fields, disabled methods, and provider names.

Verification: targeted `TestLoad` and `TestLoadAuthenticationProviderValidation` pass. `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local go test ./internal/config ./cmd/flipt -count=1` passes (`cmd/flipt` has no test files). `git diff --check` passes.

Status: complete; changes are in checked-out files for coordinator export.

Constraints: use local code and tests only; do not change git history, index baseline, or harness configuration.
