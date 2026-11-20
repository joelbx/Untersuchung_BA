# Checkpoint

Task: Preserve Kubernetes proxy authentication error classification in `authenticate` and provide the specified `httplib` wrapper interfaces.

Completed:
- `authenticate` keeps non-access authorization and context setup failures wrapped with their trace classification. Access failures remain `AccessDenied`.
- Added `MakeHandlerWithErrorWriter` and `MakeStdHandlerWithErrorWriter`; existing wrappers use `trace.WriteError` through them.
- Updated existing authentication table tests to check access and bad-parameter classifications.

Verification:
- `GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -run '^TestAuthenticate$' -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/kube/proxy -count=1` passed.
- `GOPROXY=off GOSUMDB=off go test ./lib/httplib -count=1` passed.
- `git diff --check` passed.
