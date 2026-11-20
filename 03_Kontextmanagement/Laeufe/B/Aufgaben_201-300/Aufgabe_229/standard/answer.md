Implemented disk cleanup for group covers and thumbnails, user covers and avatars, and account deletion. Removal now clears the associated fields, limits deletion to local upload paths, and handles missing files.

Validation passed: 17 focused tests, ESLint, and `git diff --check`. This work item is complete.