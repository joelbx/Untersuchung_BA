Added `getCachedChildrenCount(shareId, parentLinkId)` to [useLinksListing](/app/applications/drive/src/app/store/links/useLinksListing.tsx). It returns the number of children currently in that share and parent’s cache. The existing fetch test now checks the loaded count and share and parent isolation.

Validation passed: 2 focused Jest suites, 7 tests, Prettier, and `git diff --check`.