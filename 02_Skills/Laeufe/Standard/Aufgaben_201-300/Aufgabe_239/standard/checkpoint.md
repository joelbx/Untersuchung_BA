# Checkpoint

Resolved explicit user scoping for user properties and LastFM.

- `UserPropsRepository` and SQL implementation now require `userId` on Put, Get, Delete, and DefaultGet. SQL predicates use that argument; Put propagates update errors.
- Mock uses a two-field composite map key and correctly implements DefaultGet and error propagation.
- LastFM agent, session keys, and router pass an explicit user ID. Link status and unlink use the authenticated request user.
- LastFM linking begins with an authenticated request that returns a signed, short-lived state. The callback verifies that state before saving a session key, replacing the untrusted `uid` query argument. The UI uses the new flow.
- Added isolation tests for session keys, link state, router unlink/status, and mock composite keys.

Checks run successfully:
- `GOPROXY=off go test ./core/agents/lastfm ./persistence ./tests ./core/scrobbler`
- `./node_modules/.bin/prettier -c src/personal/LastfmScrobbleToggle.js` (from `ui`)
- `./node_modules/.bin/eslint --max-warnings 0 src/personal/LastfmScrobbleToggle.js` (from `ui`)
- `git diff --check`

Initial inspection: `rg` is unavailable (`/bin/bash: rg: command not found`), so local search used `grep` and `find`.
