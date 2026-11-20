Fixed the artist image lookup to check the media directory and its parent, accept only image files, and update original and resized cache keys when the local image changes. Added regression coverage for direct artist folders, invalid files, and cache invalidation.

Both reviewer test commands and `git diff --check` pass. The migration package has no tests.