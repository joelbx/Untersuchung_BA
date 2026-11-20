User properties now require an explicit `userId` for every read and write. The SQL repository and mock use that ID, reject empty IDs, and keep users’ values separate.

LastFM now passes the user ID through session key, link status, unlink, now-playing, and scrobble operations. Its callback uses a short-lived signed state issued for the authenticated user instead of trusting a `uid` URL parameter.

Verification passed: `GOPROXY=off go test ./...`, the final focused Go tests, and UI Prettier and ESLint checks.