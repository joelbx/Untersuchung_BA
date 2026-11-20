Added `getCachedChildrenCount(shareId, parentLinkId)` to `useLinksListing`. It returns the length of the cached children for that share and parent. The updated test checks the count before loading, after the first page, and after all pages; it also checks that other shares and parents return zero.

The `useLinksListing` test suite passed (5 tests), and `git diff --check` passed.