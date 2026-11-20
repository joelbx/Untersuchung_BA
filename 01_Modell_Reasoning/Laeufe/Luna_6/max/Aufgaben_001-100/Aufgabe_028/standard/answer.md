Added `getCachedChildrenCount(shareId, parentLinkId)` to the listing provider. It returns the number of cached children from the share and parent scoped cache selector in [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx:554).

Both existing listing test suites passed: 2 suites, 7 tests. `git diff --check` passed.