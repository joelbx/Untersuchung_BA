Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the length of the cached children array, including children that have not been decrypted.

Tests cover counts before fetching, after one page, after the full load, and for other shares and parents. Both relevant Jest suites passed: 8 tests.