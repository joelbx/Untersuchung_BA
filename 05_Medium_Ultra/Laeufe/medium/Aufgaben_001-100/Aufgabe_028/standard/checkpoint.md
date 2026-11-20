Task: Make `getCachedChildrenCount` in `useLinksListing` return the exact cached child count for a share and parent.
Status: Complete. Added `getCachedChildrenCount` using `linksState.getChildren(...).length` and integration checks for fetched counts and share/parent isolation. Three relevant Jest suites passed (32 tests); `git diff --check` passed.
