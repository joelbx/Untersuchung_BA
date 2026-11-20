# Checkpoint

Task: Fix cached children count accuracy in `useLinksListing`.

Implemented `getCachedChildrenCount(shareId, parentLinkId)` using the links cache's `getChildren` accessor, and exposed it through the listing provider. Added coverage for fetched cached children and share/parent scoping in `useLinksListing.test.tsx`.

Verification: `git diff --check` passed. The focused Jest command (`yarn workspace proton-drive test --runTestsByPath src/app/store/links/useLinksListing.test.tsx`) started but emitted no test results for over a minute and was interrupted.
