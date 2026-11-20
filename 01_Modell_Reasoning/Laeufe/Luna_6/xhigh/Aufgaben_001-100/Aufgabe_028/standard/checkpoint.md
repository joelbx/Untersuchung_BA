# Checkpoint

Task: Fix `getCachedChildrenCount` in `applications/drive/src/app/store/links/useLinksListing.tsx` so it returns the exact count of cached children for a share and parent.

Completed: Added and exposed `getCachedChildrenCount(shareId, parentLinkId)`, implemented as the length of cached children returned by the share scoped link cache. Added regression assertions covering the fetched child count and zero counts for an absent parent and a different share.

Verification: `yarn workspace proton-drive test src/app/store/links/useLinksListing.test.tsx --runInBand` passed (1 suite, 5 tests). `git diff --check` passed.
