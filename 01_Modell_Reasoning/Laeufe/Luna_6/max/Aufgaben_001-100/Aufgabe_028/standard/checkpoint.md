# Checkpoint

Implemented `getCachedChildrenCount` in `useLinksListingProvider` using the share and parent scoped `useLinksState.getChildren` selector. It returns the current number of cached children and is exposed through the provider's returned listing API.

Verification: existing `useLinksListing.test.tsx` and `useLinksListingGetter.test.tsx` passed (2 suites, 7 tests).
