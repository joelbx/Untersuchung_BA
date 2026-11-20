Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the length of the specified parent’s cached children.

Added tests for counts as pages load and for share and parent isolation. Both relevant test suites passed: 8 tests total.