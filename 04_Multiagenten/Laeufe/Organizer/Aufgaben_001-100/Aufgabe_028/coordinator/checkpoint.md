Task: Fix getCachedChildrenCount in useLinksListing so it returns the exact cached child count for share ID and parent link ID.
Status: Complete.
Change: Added public getCachedChildrenCount to useLinksListingProvider, returning linksState.getChildren(shareId, parentLinkId).length. Added tests for empty cache, fetched multi-page count, and parent/share isolation.
Verification: Existing Jest suites useLinksListing.test.tsx and useLinksListingGetter.test.tsx passed (8 tests total). git diff --check passed.
Delegation: None; solved directly.
