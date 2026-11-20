Added `getCachedChildrenCount(shareId, parentLinkId)` to the listing provider. It returns the number of cached children for that share and parent.

Added regression assertions for fetched children and for missing parents or shares in [useLinksListing.test.tsx](/app/applications/drive/src/app/store/links/useLinksListing.test.tsx:104).

Verification passed: 5 focused tests and `git diff --check`.