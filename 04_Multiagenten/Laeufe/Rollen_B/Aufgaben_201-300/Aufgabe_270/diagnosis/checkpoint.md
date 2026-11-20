# Fault localization checkpoint

Inspected Drive public-session helper, provider, user hook, telemetry, active-ping hook, shared persisted-session storage, resumeSession, and existing tests. Project source and tests untouched.

- Root cause: `applications/drive/src/app/utils/lastActivePersistedUserSession.ts` manually scans localStorage, favors `LAST_ACTIVE_PING` over `persistedAt`, and derives UID and localID in separate passes. This can select an older session or inconsistent identifiers. Its fallback can return a UID from an invalid `ps-` key that `getPersistedSessions()` would reject.
- `applications/drive/src/app/store/_api/usePublicSession.tsx` calls both helpers independently, then only sets password and user after resume. It does not set auth UID/localID. SRP retrieves UID through the old helper again.
- `applications/drive/src/app/store/_user/usePublicSessionUser.ts` memoizes a storage-derived localID, which can be stale or differ from the resumed session. `applications/drive/src/app/utils/telemetry.ts` uses old UID helper.
- Required fix path: one selector returning `PersistedSessionWithLocalID | null`, highest `persistedAt`; provider uses its UID/localID, sets auth UID/localID/password and formatted user on successful resume; user hook reads `auth.getLocalID()`; telemetry uses selected session UID. Remove ping-based selection and its constant/code paths; update existing tests.
- Shared `getPersistedSessions()` validates localID and skips malformed JSON without throwing (`getPersistedSession` catches parse errors). Thus a selector catch can report storage enumeration failures, but cannot report individual parse failures unless shared behavior changes. Clarify desired malformed-entry semantics during implementation.
- `packages/drive-store` duplicates these Drive files via its sync script and may also need synchronized changes. Existing tests assume ping priority and old helpers. No provider/user-hook tests found.
