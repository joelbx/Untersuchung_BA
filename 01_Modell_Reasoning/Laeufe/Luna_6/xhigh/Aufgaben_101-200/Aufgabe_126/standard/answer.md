Implemented the assistant Markdown/HTML fixes.

- Added [`fixNestedLists`]( /app/applications/mail/src/app/helpers/assistant/markdown.ts:104), preserved nested-list and code indentation, and enabled list rendering with configurable disabled Markdown rules.
- Scoped URL placeholders to the composer message, preserved link/image `class` and `style`, and removed unknown or cross-message links and images during restoration.
- Passed the message `localID` through model preparation, result rendering, and editor insertion.

**Verification:** Assistant URL tests (2) and text-to-HTML tests (4) pass. Targeted ESLint, Prettier, and `git diff --check` pass. The workspace type check is blocked by an OpenPGP type mismatch in `packages/crypto/lib/worker/api.ts:579`; it reported no errors in the changed Mail files.