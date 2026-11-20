# U2F multi-device authentication checkpoint

## Goal
Implement multi-device U2F authentication challenges with legacy compatibility across auth APIs, CLI, and web clients, while keeping MFA device management hidden until the flow is complete.

## Work plan
- Trace existing U2F challenge producers and consumers using repository code and tests.
- Add a public challenge wrapper containing the legacy challenge and all registered-device challenges.
- Update CLI and web authentication flows to accept both legacy and multi-device formats.
- Keep device management UI hidden as required, then run focused existing tests.

## Status
- Added `auth.U2FAuthenticateChallenge` with the legacy challenge embedded and a `challenges` list.
- Auth server now creates a stored challenge for each registered U2F device and returns them together.
- Updated auth API signatures and client decoding; the CLI consumes every challenge and falls back to the legacy embedded challenge when the list is absent.
- The web source in this checkout has no standalone frontend source tree; the web API preserves flattened legacy JSON and exposes the new list.
- MFA device registration and management code has not been changed.
- Validation: `gofmt` and `git diff --check` passed. `go test ./lib/web ./lib/client` passed. The combined auth/web/client run had a transient `PasswordSuite.TestTiming` threshold failure; a standalone rerun of `go test ./lib/auth` passed.
- Implementation and validation are complete.
