Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It counts children directly from the cache, including links that have not been decrypted.

Regression tests cover paged fetches, parent and share isolation, and encrypted cached children. All 33 relevant tests passed across three suites.