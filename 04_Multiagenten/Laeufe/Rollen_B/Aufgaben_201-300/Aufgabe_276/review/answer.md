VERDICT: ACCEPT

The patch validates required credentials for enabled GitHub and OIDC authentication during configuration loading and returns the specified provider and field errors. I found no demonstrated code defect.

Both existing test runs passed:

- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config -run '^(TestLoad|TestLoadOAuthCredentials)$' -count=1`
- `GOTOOLCHAIN=local GOPROXY=off go test ./internal/config -count=1`

The tests do not cover mixed-case OIDC provider keys. I made no project code or test changes.