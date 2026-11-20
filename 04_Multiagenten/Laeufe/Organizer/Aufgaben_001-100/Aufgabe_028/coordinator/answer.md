Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing.tsx](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the length of the cached children for that share and parent.

The relevant Jest suites passed: 8 tests, including new coverage for fetched children and share and parent isolation. `git diff --check` passed. No delegation was used.