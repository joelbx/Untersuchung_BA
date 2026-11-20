# Checkpoint

Task resolved: `useLinksListingProvider` now exposes `getCachedChildrenCount(shareId, parentLinkId)` and returns the length of `linksState.getChildren` for that pair. A regression test fetches children for two parents and two shares, then checks exact cached counts.

TDD: `yarn workspace proton-drive test useLinksListing.test.tsx --runInBand` first failed as expected with `TypeError: hook.current.getCachedChildrenCount is not a function` (5 passed, 1 failed); after implementation it passed (6 passed).

Verification: `yarn workspace proton-drive test` passed (34 suites, 282 tests); `yarn workspace proton-drive check-types` passed; Prettier check and `git diff --check` passed. Jest emitted existing `caniuse-lite`, console, and openpgp/V8 warnings; no test failures. No downloads attempted.

Tooling: `rg` unavailable (`/bin/bash: rg: command not found`); used `find` and `grep`.
