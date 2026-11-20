Resolved the event delivery bug. The UI now sends a per-window UUID on API requests, and SSE subscriptions use that ID to exclude the originating window and other users’ sessions. The server also supports the required header and cookie fallback, and broker call sites use the new context-aware API.

Verification passed: focused Go tests, all 42 UI tests, Prettier, ESLint, and `git diff --check`.