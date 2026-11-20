Updated `UserPropsRepository` and its mock so every read and write requires an explicit `userId`. LastFM now uses that ID for session keys, link status, unlinking, now playing, and scrobbling. The auth callback uses a short-lived, single-use state created by an authenticated link request instead of trusting a `uid` query parameter.

Added two-user isolation tests. The relevant Go suites, UI Prettier and ESLint checks, and `git diff --check` pass.

Pending LastFM links are stored in the router process; a restart or callback sent to a different instance requires the user to start linking again.