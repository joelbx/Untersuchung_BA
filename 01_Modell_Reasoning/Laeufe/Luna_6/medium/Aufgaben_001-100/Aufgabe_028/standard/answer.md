Added `getCachedChildrenCount(shareId, parentLinkId)` to the listing provider. It returns the number of children currently in that share’s cache for the parent. Added tests for fetched children and share/parent scoping.

`git diff --check` passed. The focused Jest command produced no results after about a minute, so I stopped it; the tests remain unverified.