# U2F multi-device authentication checkpoint

Implemented a backward-compatible U2F sign request with top-level legacy fields and a `challenges` array. The auth server creates and stores one challenge per U2F device. Auth client and CLI handle both legacy single-device responses and the new list. Web endpoints pass through the new payload. `tsh mfa` remains hidden in help.

Verification completed:
- `GOPROXY=off go test ./lib/auth ./lib/client ./lib/web ./tool/tsh -run '^$'` — exit 0; compilation only.
- `GOPROXY=off go test ./lib/web -run '^TestWeb$' -check.f TestU2FLogin -count=1` — exit 0.
- `GOPROXY=off go test ./lib/auth -run '^TestU2FAuthenticateChallengeJSON$' -count=1` — exit 0.
- `GOPROXY=off go test ./lib/client ./tool/tsh -run '^$'` — exit 0; compilation only.
- `git diff --check` — exit 0.

Initial search attempted `rg`, but the tool is unavailable (`/bin/bash: rg: command not found`); subsequent searches used `grep`. Two initial Go test invocations used the wrong `-run` name and reported `[no tests to run]`; the corrected `TestWeb` invocation above ran the U2F test.

- `GOPROXY=off go test ./lib/web -run '^TestWeb$' -check.f 'Test(U2FLogin|ChangePasswordWithTokenU2F)' -count=1` — exit 0 (1.260s).
