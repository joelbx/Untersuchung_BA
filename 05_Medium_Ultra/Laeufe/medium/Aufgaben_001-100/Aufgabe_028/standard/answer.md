Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the length of the cached children for that share and parent.

The updated tests cover fetched counts and share and parent isolation. All 32 tests in the three relevant suites passed.