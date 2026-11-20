# Checkpoint

Implemented a backward-compatible U2F payload with top-level legacy fields and a challenge list. The auth server now issues a challenge per registered U2F device; the auth client, web path, and CLI consume the new payload with an old-server fallback. Added JSON compatibility and web login regression tests, and hid the MFA management command from help.

Verification: `go test ./lib/auth -run '^TestU2FAuthenticateChallengeJSON$' -count=1` passed; `go test ./lib/web -run '^TestWeb$' -check.f 'TestU2FLogin|TestU2FLoginMultipleDevices' -count=1` passed; `go test ./lib/client ./tool/tsh -run '^$'` passed compilation. The checked-in browser assets live in an external submodule and still use the legacy top-level challenge, so browser login remains compatible with one device; this patch enables the challenge list for clients that consume it.
