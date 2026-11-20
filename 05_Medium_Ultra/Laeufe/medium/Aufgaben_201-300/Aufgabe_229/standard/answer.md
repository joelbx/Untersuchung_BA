Implemented disk cleanup for local group covers, user covers, and uploaded avatars. Explicit removal now clears the related fields and removes supported image variants; account deletion removes both user cover and avatar files. The socket handlers use the centralized user image functions and retain their removal hooks.

Verification passed: ESLint, `git diff --check`, and six focused Mocha tests.