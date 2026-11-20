# Checkpoint

Task: add `getCachedChildrenCount(shareId, parentLinkId)` to `useLinksListing`.

Status: complete. The method returns the length of `useLinksState.getChildren` for the specified share and parent. The existing listing test now checks empty, first-page, full-cache, and other share/parent counts.

Verification: focused `useLinksListing.test.tsx` passed (5 tests); Prettier check and `git diff --check` passed.
