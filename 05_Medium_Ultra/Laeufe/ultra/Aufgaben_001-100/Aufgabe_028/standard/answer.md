Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx:554). It returns the number of cached children, including links still awaiting decryption.

Two read-only agents reviewed the cache path and test coverage. The relevant tests passed: **2 suites, 7 tests**.