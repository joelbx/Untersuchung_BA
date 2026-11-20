Added `getCachedChildrenCount(shareId, parentLinkId)` to the public `useLinksListing` value. It returns the count from the share’s cached children, and the multi-page fetch test now verifies the count after both pages load.

Both relevant test suites passed: 7 tests total. `git diff --check` passed.