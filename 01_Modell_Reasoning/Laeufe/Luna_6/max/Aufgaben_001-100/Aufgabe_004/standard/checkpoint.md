# PassAliases issue checkpoint

Implemented the dedicated `usePassAliasesSetup` hook and provider helper module. The provider now returns the typed `PassAliasesProviderReturnedValues` contract, renders a clear no-aliases heading, fetches alias data through the shared TTL helper, creates a default vault only when alias options are requested, and refreshes both state and memoized aliases after creation.

Updated PassBridge vault lookup/creation types and factory behavior: lookup returns the oldest eligible active vault or `undefined`; explicit creation checks with `maxAge: 0` before creating the Personal vault. Updated the existing PassBridge test mock and integration example for the new API.

Verification: focused PassAliases Jest suite passed (3 tests); `packages/components` and `packages/pass` TypeScript checks passed; `git diff --check` passed.
