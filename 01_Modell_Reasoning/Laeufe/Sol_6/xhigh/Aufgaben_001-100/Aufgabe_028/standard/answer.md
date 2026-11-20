Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the length of the cached children for that share and parent.

Added coverage for a two-page folder load, share and parent isolation, and children that are cached but not decrypted. Both focused Jest suites passed: 8 tests total.