Implemented multi-device U2F challenges in [auth.go](/app/lib/auth/auth.go:828). The new response preserves the first challenge in the legacy flat JSON format and includes all device challenges in `challenges`. Updated the auth client, web session plumbing, and SSH-agent login flow to use the list, with a fallback for older servers.

Expanded the existing web login test to verify both response formats and successful authentication with either of two keys in [apiserver_test.go](/app/lib/web/apiserver_test.go:1424).

Verification passed: `go test ./lib/auth ./lib/client`, `go test ./lib/web -check.f TestU2FLogin`, and `go test ./lib/web`. An initial full web run hit a proxy startup timeout in an unrelated test; that test and the full suite passed on rerun. `git diff --check` passed.