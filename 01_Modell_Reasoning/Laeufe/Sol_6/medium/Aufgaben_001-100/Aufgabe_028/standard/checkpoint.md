# Checkpoint

Task: make useLinksListing.getCachedChildrenCount return the exact cached child-link count for a share and parent.
Status: complete.
Implementation: count links returned by linksState.getChildren(shareId, parentLinkId); exposed on provider.
Verification: useLinksListing.test.tsx and useLinksListingGetter.test.tsx passed (7 tests); git diff --check passed.
