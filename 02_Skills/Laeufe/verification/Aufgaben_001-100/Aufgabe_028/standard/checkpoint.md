# Checkpoint

Task: make `getCachedChildrenCount(shareId, parentLinkId)` return the exact number of children cached for that share and parent.

Implementation: added the public provider method, counting `linksState.getChildren(shareId, parentLinkId).length`. Added checks for empty, first page, all pages, another parent/share, and encrypted-only cached links.

Verification: `yarn workspace proton-drive test src/app/store/links/useLinksListing.test.tsx src/app/store/links/useLinksListingGetter.test.tsx --runInBand` exited 0; 2 suites and 8 tests passed. `git diff --check` exited 0.

Local tooling: `rg` is unavailable (`/bin/bash: rg: command not found`); used local `find` and BusyBox `grep` for inspection. No check remains blocked.
