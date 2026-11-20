Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the cached children count, including links that have not decrypted.

Added coverage for an empty cache, multiple fetched pages, share and parent isolation, and decryption failure. The Drive listing suite passes: 7 tests.