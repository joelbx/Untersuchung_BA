Added `getCachedChildrenCount(shareId, parentLinkId)` to the listing provider. It returns the length of the children currently stored in that share’s cache for the parent.

The test now checks the count after fetching two pages and confirms another share returns zero. `git diff --check` passed. The focused Jest run did not finish and was stopped after about two minutes.