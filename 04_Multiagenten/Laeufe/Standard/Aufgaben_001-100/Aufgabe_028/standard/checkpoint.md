Task: Fix getCachedChildrenCount in applications/drive/src/app/store/links/useLinksListing.tsx.
Status: Complete.
Implementation: Added public provider method that returns linksState.getChildren(shareId, parentLinkId).length. Counts encrypted and decrypted cached children alike.
Verification: Listing and getter Jest suites passed (2 suites, 8 tests). git diff --check passed.
Files changed: useLinksListing.tsx, useLinksListing.test.tsx, useLinksListingGetter.test.tsx.
