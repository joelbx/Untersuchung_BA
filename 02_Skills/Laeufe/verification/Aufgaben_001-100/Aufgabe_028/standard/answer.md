Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the length of the cached children for that share and parent, including children that have not yet been decrypted.

Verified with the focused listing tests: **8 tests passed across 2 suites**. `git diff --check` also passed.