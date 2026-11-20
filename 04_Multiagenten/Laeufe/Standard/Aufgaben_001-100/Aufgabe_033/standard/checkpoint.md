# Multi-device U2F checkpoint

Implemented: U2FSignRequest creates a challenge for every registered U2F device. U2FAuthenticateChallenge embeds the legacy challenge and includes `challenges`; the auth client accepts legacy single-challenge responses. CLI signing passes all challenges to the token helper. Web endpoints forward the enhanced payload. Added a web login regression with two keys that verifies both the legacy fields and authentication with the second key.

Verification: `go test ./lib/auth ./lib/client ./lib/web -count=1` passed before the final test assertion adjustment; focused `go test ./lib/web -run '^TestWeb$' -check.f 'TestU2FLogin' -count=1` passed after adjustment. No MFA management UI source is present in this checkout; the checked-in web assets are compiled bundles.
