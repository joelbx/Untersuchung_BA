Task: validate required GitHub and OIDC authentication fields at startup.
Status: implemented required-field and GitHub scope validation with provider/field errors; config package tests pass.
Verification: go test ./internal/config
