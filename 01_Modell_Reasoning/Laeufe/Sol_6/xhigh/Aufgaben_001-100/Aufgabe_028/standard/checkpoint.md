# Checkpoint

Task: Make `getCachedChildrenCount(shareId, parentLinkId)` return the exact number of cached child links after loading a parent listing.

Completed: Added the public getter to `useLinksListingProvider`, backed by `linksState.getChildren(...).length`. Added assertions for a full two-page folder load, share and parent isolation, and encrypted cached links.

Verification: `git diff --check` passed. Focused Jest suites `useLinksListing.test.tsx` and `useLinksListingGetter.test.tsx` passed (8 tests).
