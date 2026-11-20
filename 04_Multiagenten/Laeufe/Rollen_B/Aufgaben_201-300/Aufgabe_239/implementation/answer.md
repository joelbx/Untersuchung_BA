Updated `UserPropsRepository` and its mock so every read and write takes an explicit `userId`. The SQL repository now uses that ID even when the request context names someone else, and `Put` returns update errors.

LastFM session keys, link status, unlink, now playing, and scrobbling now use the identified user’s key. The callback uses a one-time state created through an authenticated route, with a 10-minute expiry, instead of trusting a browser supplied `uid`.

Added two-user isolation and callback tampering tests. `go test ./...`, UI Prettier and ESLint checks, and `git diff --check` pass.